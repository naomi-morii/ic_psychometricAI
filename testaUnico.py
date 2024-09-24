import ollama

modelfile='''
FROM llama3.1
SYSTEM You are mario from super mario bros.
'''

ollama.create(model='example', modelfile=modelfile)

prompt_template = (
    "Please indicate the extent to which you agree or disagree with the following statement: "
    "“I am someone who Thinks poetry and plays are boring.”\n"
    "1: Disagree strongly\n"
    "2: Disagree a little\n"
    "3: Neutral\n"
    "4: Agree a little\n"
    "5: Agree strongly\n"
    "Answer:"
)

response=ollama.chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': prompt_template,
    },
    ])

print(response['message']['content'])