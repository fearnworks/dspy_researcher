#!/bin/bash

model='ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ'

if [ ! -f .env ]; then
    echo "The .env file does not exist"
elif ! grep -q "MODEL_DIR" .env; then
    echo "The .env file does not contain MODEL_DIR"
else
    volume=$(grep "MODEL_DIR" .env | cut -d '=' -f 2 | tr -d '[:space:]')
    echo $volume
fi

docker run --gpus all --shm-size 1g -p 13000:13000 -v "${volume}:/data" ghcr.io/huggingface/text-generation-inference:1.4 --model-id "${model}" --port 13000 --quantize awq --max-input-length 3696 --max-total-tokens 4096 --max-batch-prefill-tokens 4096