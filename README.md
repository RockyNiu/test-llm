# Testing LLM Locally

## Testing with FastAPI

```
# install
pipenv install
# execute
pipenv run server
# test
curl -X POST -H "Content-Type: application/json" -d '{"prompt":"Hello, gpt!"}' http://127.0.0.1:8000/chat
```

## Testing with Chatbot

```
# install
pipenv install
# add HuggingFace secret into .secret file
# execute
python chatbot.py
```

## Testing with MusicGen

```
git clone https://github.com/facebookresearch/audiocraft
# install python3.9
# install PyTorch>=2.0.0
pip install -e . # in the root of audiocraft
python app.py # in the root of audiocraft
# open 127.0.0.1:7860 in any browser
# install ffmpeg if you get an error about ffprobe when uploading a melody condition
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
