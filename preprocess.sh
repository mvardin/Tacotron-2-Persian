#! /bin/bash

DATASET_PATH="/home/mvardin/Tacotron-2-Persian/Corpus/fa"
OUTPUT_PATH="/home/mvardin/Workarea/speakers/man1/ppoutput"
CONFIG_PATH="/home/mvardin/Workarea/Tacotron-2-Persian"
NUM_WORKERS=32
SPEACKER="045313dea664e9b5cfc4bd4b0211b1517740f736ca6204255180d0216644a3b23da079514e084f3562fb92e41f853d14c82bb8c8b9241aa190c7509133573655"

python -m tac2persian.data_preprocessing.preprocess_commonvoice_fa --dataset_path="$DATASET_PATH" \
                                                                   --output_path="$OUTPUT_PATH" \
                                                                   --config_path="$CONFIG_PATH" \
                                                                   --num_workers="$NUM_WORKERS" \
                                                                   --speaker="$SPEACKER" \
