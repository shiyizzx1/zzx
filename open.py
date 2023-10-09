import openai

openai.api_key = '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'


def gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user',
             'content': prompt}
        ],
        temperature=0,
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


gpt("hello")
