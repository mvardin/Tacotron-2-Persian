#! /bin/bash

# get path to config file
full_path=$0
CONFIG_PATH=$(dirname "$full_path")
echo $CONFIG_PATH

output_path="/home/mvardin/Workarea/speakers/man1"
checkpoint_path="/home/mvardin/Workarea/speakers/man1/trained/checkpoints/checkpoint_0K.pt"
dataset_path="/home/mvardin/Workarea/speakers/man1/ppoutput"
batch_size=10


python -m tac2persian.train --config_path="$CONFIG_PATH" \
                            --output_path="$output_path" \
                            --checkpoint_path="$checkpoint_path" \
                            --dataset_path="$dataset_path" \
                            --batch_size="$batch_size"
