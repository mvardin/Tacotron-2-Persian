# Tacotron 2 - Persian

1- Change the tac2persian/data_preprocessing/preprocess_commonvoice_fa.py lines 119 (target_speakers) for youe speaker id

2- install ffmpeg, librosa, segments and the others

3- run sh preprocess.sh

4- run wc -l metadata.txt for getting lines and then run below command

5- shuf metadata.txt >> metadata_shuf.txt

6- head -n 9000 metadata_shuf.txt > metadata_train.txt

7- tail -n 1000 metadata_shuf.txt > metadata_eval.txt

8- run sh train.sh

9- run generate.sh

10- done


** in windows client , use this line 

with open(os.path.join(dataset_path, "validated.tsv"), encoding="utf8") as f:

in tac2persian/data_preprocessing/preprocess_commonvoice_fa.py line 50
