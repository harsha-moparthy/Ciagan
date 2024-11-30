from train import ciagan_exp
import argparse

def update_config(args):
    new_config = {
        'TRAIN_PARAMS': {
            'ARCH_NUM': args.arch_num,
            'ARCH_SIAM': args.arch_siam,
            'EPOCH_START': args.epoch_start,
            'EPOCHS_NUM': args.epochs_num,
            'LEARNING_RATE': args.learning_rate,
            'FILTER_NUM': args.filter_num,
            'ITER_CRITIC': args.iter_critic,
            'ITER_GENERATOR': args.iter_generator,
            'ITER_SIAMESE': args.iter_siamese,
            'GAN_TYPE': args.gan_type,
            'FLAG_GPU': args.flag_gpu,
            'FLAG_SIAM_MASK': args.flag_siam_mask,
        },
        'DATA_PARAMS': {
            'DATA_PATH': args.data_path,
            'DATA_SET': args.data_set,
            'LABEL_NUM': args.label_num,
            'BATCH_SIZE': args.batch_size,
            'WORKERS_NUM': args.workers_num,
            'IMG_SIZE': args.img_size,
        },
        'OUTPUT_PARAMS': {
            'SAVE_EPOCH': args.save_epoch,
            'SAVE_CHECKPOINT': args.save_checkpoint,
            'LOG_ITER': args.log_iter,
            'COMMENT': args.comment,
            'EXP_TRY': args.exp_try,
            'RESULT_PATH': args.result_path,
            'MODEL_PATH': args.model_path,
            'VIZ_PORT': args.viz_port,
            'VIZ_HOSTNAME': args.viz_hostname,
            'VIZ_ENV_NAME': args.viz_env_name,
            'SAVE_IMAGES': args.save_images,
            'PROJECT_NAME': args.project_name,
        }
    }
    return new_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run CIAGAN training')
    
    # Training parameters
    parser.add_argument('--arch_num', type=str, default='unet_flex', help='Architecture number')
    parser.add_argument('--arch_siam', type=str, default='resnet_siam', help='Siamese architecture')
    parser.add_argument('--epoch_start', type=int, default=0, help='Starting epoch')
    parser.add_argument('--epochs_num', type=int, default=2001, help='Number of epochs')
    parser.add_argument('--learning_rate', type=float, default=0.0001, help='Learning rate')
    parser.add_argument('--filter_num', type=int, default=16, help='Number of filters')
    parser.add_argument('--iter_critic', type=int, default=1, help='Iterations for critic')
    parser.add_argument('--iter_generator', type=int, default=3, help='Iterations for generator')
    parser.add_argument('--iter_siamese', type=int, default=1, help='Iterations for siamese')
    parser.add_argument('--gan_type', type=str, default='lsgan', help='Type of GAN')
    parser.add_argument('--flag_gpu', type=bool, default=True, help='Flag for GPU usage')
    parser.add_argument('--flag_siam_mask', type=bool, default=False, help='Flag for Siamese mask')

    # Data parameters
    parser.add_argument('--data_path', type=str, default='../dataset/', help='Path to the dataset')
    parser.add_argument('--data_set', type=str, default='celeba', help='Dataset name')
    parser.add_argument('--label_num', type=int, default=5, help='Number of labels')
    parser.add_argument('--batch_size', type=int, default=1, help='Batch size')
    parser.add_argument('--workers_num', type=int, default=4, help='Number of workers')
    parser.add_argument('--img_size', type=int, default=128, help='Image size')

    # Output parameters
    parser.add_argument('--save_epoch', type=int, default=1, help='Save epoch interval')
    parser.add_argument('--save_checkpoint', type=int, default=100, help='Save checkpoint interval')
    parser.add_argument('--log_iter', type=int, default=1, help='Log iteration interval')
    parser.add_argument('--comment', type=str, default='Something here', help='Comment')
    parser.add_argument('--exp_try', type=str, default='check', help='Experiment try')
    parser.add_argument('--result_path', type=str, default='../results/', help='Path to save results')
    parser.add_argument('--model_path', type=str, default='../models/', help='Path to save models')
    parser.add_argument('--viz_port', type=int, default=8098, help='Port for visualization')
    parser.add_argument('--viz_hostname', type=str, default='http://localhost', help='Hostname for visualization')
    parser.add_argument('--viz_env_name', type=str, default='main', help='Environment name for visualization')
    parser.add_argument('--save_images', type=bool, default=True, help='Flag to save images')
    parser.add_argument('--project_name', type=str, default='ciagan', help='Project name')

    args = parser.parse_args()
    new_config = update_config(args)
    r = ciagan_exp.run(config_updates=new_config)
