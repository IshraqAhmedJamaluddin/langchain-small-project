# langchain-small-project

A small project using langChain

It takes a language and task and outputs a function that writes you code and test for that task.

## Setup and Running

add a `.env` file to your base directory that includes your `OPENAI_API_KEY` e.g:

```
OPENAI_API_KEY=[YOUR KEY HERE]
```

to run just type `python main.py` optional arguments available as follows `python main.py --language Lua --task "take a number and print the Fibonacci till that index"`
