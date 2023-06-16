import os
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

with open('.secret', encoding='utf-8') as f:
    HUGGINGFACEHUB_API_TOKEN = f.read().strip()
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

model_id = "togethercomputer/RedPajama-INCITE-7B-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)
local_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100
)

local_llm = HuggingFacePipeline(pipeline=local_pipeline)

from langchain import PromptTemplate

template = """Question: {question}\
Answer: in less than 100 words."""

prompt = PromptTemplate(template=template, input_variables=["question"])

from langchain import LLMChain
llm_chain = LLMChain(
    prompt=prompt,
    llm=local_llm,
)

question = "could you answer a math question: 1+1=?"

print(llm_chain.run({question}))