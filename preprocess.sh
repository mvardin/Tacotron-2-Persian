#! /bin/bash

DATASET_PATH="/home/mvardin/Tacotron-2-Persian/fa"
OUTPUT_PATH="/home/mvardin/Tacotron-2-Persian/ppoutput"
CONFIG_PATH="/home/mvardin/Tacotron-2-Persian"
NUM_WORKERS=10

python -m tac2persian.data_preprocessing.preprocess_commonvoice_fa --dataset_path="$DATASET_PATH" \
                                                                   --output_path="$OUTPUT_PATH" \
                                                                   --config_path="$CONFIG_PATH" \
                                                                   --num_workers="$NUM_WORKERS"
