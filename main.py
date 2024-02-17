import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse
from dotenv import load_dotenv

load_dotenv()
parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="Python")
args = parser.parse_args()

llm = OpenAI()

# prompts
code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"],
)

test_prompt = PromptTemplate(
    template="Write a test for the following {language} code:\n{task}",
    input_variables=["language", "code"],
)

# chains
code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")

test_chain = LLMChain(llm=llm, prompt=test_prompt, output_key="test")

# combining chains
chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["language", "task"],
    output_variables=["code", "test"],
)


result = chain.invoke({"language": args.language, "task": args.task})

print(">>>>>>>>>>>>Code")
print(result["code"])
print(">>>>>>>>>>>>Test")
print(result["test"])
