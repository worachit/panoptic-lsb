#!/bin/bash

srun --partition=mundus --job-name=bash --gres=gpu:1 --time=10:00:00 --pty bash -i