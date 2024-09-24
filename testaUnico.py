import ollama

modelfile='''
FROM llama3.1
SYSTEM For the following task, respond in a way that matches this description:  'I love kids and dogs. I like to go shopping with my daughters. I like to cook. I love to chat with my friends'.  Please respond only with the single number that represents your answer. Answer based on the description.
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
