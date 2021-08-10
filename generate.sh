#! /bin/bash

wavernn_config_path="/home/mvardin/Workarea/speakers/Tools/config_wavernn.yml"
wavernn_checkpoint_path="/home/mvardin/Workarea/speakers/Tools/ckpt_wavernn_libritts.pt"
tacotron_config_path="/home/mvardin/Workarea/speakers/Tools/config_tacotron.yml"
tacotron_checkpoint_path="/home/mvardin/Workarea/speakers/Checkpoints/Woman1.pt"
lang="fa"
output_path="/home/mvardin/Workarea/speakers/outputs"
filename="03"
inp_text="سلام آریا؛ من ربات هستم؛ توسط بابات ساخته شدم."

python -m tac2persian.generate --wavernn_config_path="$wavernn_config_path" \
                                                --wavernn_checkpoint_path="$wavernn_checkpoint_path" \
                                                --tacotron_config_path="$tacotron_config_path" \
                                                --tacotron_checkpoint_path="$tacotron_checkpoint_path" \
                                                --lang="$lang" \
                                                --output_path="$output_path" \
                                                --filename="$filename" \
                                                --inp_text="$inp_text" \
