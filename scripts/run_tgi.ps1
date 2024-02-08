# $model = 'TheBloke/CodeLlama-70B-Instruct-AWQ'
$model = 'ybelkada/Mixtral-8x7B-Instruct-v0.1-AWQ'
Test-Connection -ComputerName huggingface.co -Count 4
if (-not (Test-Path .env)) {
    Write-Host "The .env file does not exist"
} elseif ($null -eq (Get-Content .env | Select-String -Pattern "MODEL_DIR")) {
    Write-Host "The .env file does not contain MODEL_DIR"
} else {
    $volume =  (Get-Content .env | Select-String -Pattern "MODEL_DIR").ToString().Split("=")[1].Trim()
    $volume
}

docker run --gpus all --shm-size 1g -p 13000:13000 -v "${volume}:/data" ghcr.io/huggingface/text-generation-inference:1.4 --model-id "${model}" --port 13000 --quantize awq --max-input-length 3696 --max-total-tokens 4096 --max-batch-prefill-tokens 4096 
