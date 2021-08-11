# Tacotron 2 - Persian

1- Install these reuirements

!apt install espeak
!pip install segments


2- Install ffmpeg, librosa, segments and the others if needed

3- Change and run "sh preprocess.sh"

4- run wc -l metadata.txt for getting lines and then run below command

5- shuf metadata.txt >> metadata_shuf.txt

6- head -n 9000 metadata_shuf.txt > metadata_train.txt

7- tail -n 1000 metadata_shuf.txt > metadata_eval.txt

8- Change and run "sh train.sh"

9- Change and run "generate.sh"

10- done
