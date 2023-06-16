# Testing LLM Locally

## Testing with MusicGen
```
# install pytorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 #CUDA118
or
pip install torch torchvision torchaudio #CPU
# install package
pip install -e . 
# add HuggingFace secret into .secret file
# execute
python chatbot.py
```

## Testing with Dalai
```
npm i
npm run install
npm run backup
npm run appaca
npm run serve
```

## References
- https://beebom.com/how-run-chatgpt-like-language-model-pc-offline/