from typing import Annotated
from fastapi import FastAPI, Body
from transformers import pipeline
from pydantic import BaseModel

MODEL = "gpt2"

app = FastAPI()


class RequestData(BaseModel):
    prompt: str


class ResponseData(BaseModel):
    response: str


model = pipeline("text-generation", model=MODEL)


@app.post("/chat")
def chat(request_data: Annotated[RequestData, Body()]) -> ResponseData:
    prompt = request_data.prompt
    response = model(prompt)[0]["generated_text"]
    return ResponseData(response=response)
