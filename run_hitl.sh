#!/bin/bash

#SBATCH --time=72:00:00
#SBATCH --job-name=panoptic_segement
#SBATCH --partition=mundus
#SBATCH --gres=gpu:1
#SBATCH --output=slurm/panoptic_output_with_hitl.log
#SBATCH --error=slurm/panoptic_error_with_hitl.log

export PYTHONUNBUFFERED=TRUE
python ./run.py --model_key=2311Pretrained --class_map=basichalosnocompanions --checkpoint_dir /mundus/wketrungs511/panoptic-lsb/models/2311Pretrained/ver13