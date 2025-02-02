import traceback
import argparse
import os
import shutil
import librosa
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import partial
from tac2persian.utils.generic import load_config
from tac2persian.utils.g2p.g2p import Grapheme2Phoneme
from tac2persian.utils.audio import log_melspectrogram, trim_silence


def log_traceback(ex):
    tb_lines = traceback.format_exception(ex.__class__, ex, ex.__traceback__)
    tb_text = ''.join(tb_lines)
    # I'll let you implement the ExceptionLogger class,
    # and the timestamping.
    print(tb_text)
    
def normalize_text(text):
    if text[-1] not in [".", "!", "?"]:
        text = text + "."
    return text


def compute_features(source_audio_path, 
                     file_name, 
                     text, 
                     speaker_name, 
                     out_melspecs_path, 
                     g2p,
                     itr,
                     count_files):
    print(f"Processing file {itr}/{count_files}")
    try:
        text = normalize_text(text)
        out_mel_path = os.path.join(out_melspecs_path, file_name + ".npy")
        phoneme = g2p.text_to_phone(text, language="fa")
        phoneme_idx = g2p.phone_to_sequence(phoneme)
        phoneme_idx = ','.join(map(str, phoneme_idx))
        audio, _ = librosa.core.load(source_audio_path, sr=config["mel_params"]["sample_rate"])
        audio = trim_silence(audio, config["ref_level_db"])
        melspec = log_melspectrogram(audio, **config["mel_params"])
        np.save(out_mel_path, melspec)
        meta_line = f"{file_name}|{speaker_name}|{text}|{phoneme}|{melspec.shape[1]}|{phoneme_idx}"
        
        return meta_line
    except Exception as ex:
        print("=======================")
        print(f"Error in processing {file_name}")
        log_traceback(ex)
        print("=======================")
        return None

def preprocess(dataset_path, output_path, target_speakers, config, num_workers):
    r"""Preprocesses audio files in the dataset."""
    with open(os.path.join(dataset_path, "validated.tsv"), "r") as f:
        all_lines = f.readlines()

    all_lines = [l.split('\t') for l in all_lines[1:]]
    all_lines = [(l[0], l[1], l[2]) for l in all_lines]
    
    # Load G2P module
    g2p = Grapheme2Phoneme()

    # Keep only the traget speakers
    all_lines_final = {}
    for speaker in target_speakers:
        all_lines_final[speaker] = [(l[1], l[2]) for l in all_lines if l[0]==speaker]

    executor = ProcessPoolExecutor(max_workers=num_workers)
    
    # Create metafile and copy files
    metafile = []
    for itr_spk, speaker in enumerate(all_lines_final.keys()):
        speaker_name = f"speaker_fa_{itr_spk}"
        
        # Create final directory
        out_melspecs_path = os.path.join(output_path, "melspecs")
        os.makedirs(out_melspecs_path, exist_ok=True)
        print(f"Preprocessing files for speaker {itr_spk}/{len(all_lines_final.keys())}")
        lines = all_lines_final[speaker]
        count_files = len(lines)

        for itr, line in enumerate(lines):
            file_name, text = line
            file_name_ = speaker_name + "_" + file_name.split(".")[0]
            source_audio_path = os.path.join(dataset_path, "clips", file_name)
            meta_line = executor.submit(partial(compute_features, 
                                                source_audio_path, 
                                                file_name_, 
                                                text, 
                                                speaker_name, 
                                                out_melspecs_path, 
                                                g2p,
                                                itr,
                                                count_files))
            metafile.append(meta_line)

    metafile = [metaline.result() for metaline in metafile if metaline is not None]
    print(metafile)
    
    # Write metafile
    # Ardin
    with open(os.path.join(output_path, "metadata.txt"), "w") as final_meta:
        for l in metafile:
            final_meta.write(str(l) + "\n")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--config_path", type=str, required=True)
    parser.add_argument("--num_workers", type=int, default=5)
    parser.add_argument("--speaker", type=str, default="c02a93dd88299382b1f6efb2e26be36c9080c26ceafaae4f3d02f6f052a24f011ab053ea0ec2cc6e81a3f07fcaa6c8e23be42f8cb3e695176c99b5aba1f3fdd4")
    args = parser.parse_args()
 
    target_speakers = [args.speaker]

    config = load_config(os.path.join(args.config_path, "config_preprocess.yml"))
    preprocess(args.dataset_path, args.output_path, target_speakers, config, args.num_workers)
