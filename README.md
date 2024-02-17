# langchain-small-project

A small project using langChain

It takes a language and task and outputs a function that writes you code and test for that task.

## Setup and Running

add a `.env` file to your base directory that includes your `OPENAI_API_KEY` e.g:

```
OPENAI_API_KEY=[YOUR KEY HERE]
```

to make an environment use `python -m venv env`, then if you're on mac or linux use `source env/bin/activate` or on windows use the command corresponding to your terminal type.

to install required packages run `pip install -r requirements.txt`

to run just type `python main.py` optional arguments available as follows `python main.py --language Lua --task "take a number and print the Fibonacci till that index"`
