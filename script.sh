export CUDA_VISIBLE_DEVICES=0,1
cd $HOME/harsha/ciagan/source  # Change the path to the source directory (where the code is present)

# Check and create directories if they do not exist
for dir in ../frames/0/ ../models ../results ../mydata; do
    [ ! -d "$dir" ] && mkdir -p "$dir"
done

# # # Make the video into frames
python3 video2frames.py --input ../video.mp4 --output ../frames/0/ --width 512 --height 512

# # # Preprocessing the data
python3 process_data.py --input ../frames/ --output ../mydata/custom/ 

# # Training the model
python3 run_training.py --data_path ../mydata/  --data_set custom  --label_num 1 --img_size 128   --epochs_num 1001 --log_iter 1 --workers_num 128 --flag_gpu True 

# # Testing the model
python3 test.py --model "modelG_ciagan" --data ../mydata/custom/ --out ../results/

# # Make the video from frames and temporally not consistent take it as a video
# python3 frames2video.py 
