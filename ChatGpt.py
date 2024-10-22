from token import token        # импорт токена для работы ChatGpt
from openai import OpenAI      # для работы с chat Gpt

#если вы просто хотите задать вопрос ChatGpt напишите свой вопрос в переменную vopr

def chat(vopr):
    '''Функция подключается к chatGpt и отвечает на вопрос пользователя'''
    vopr = vopr

    client = OpenAI(

        api_key=token, # ваш токен
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": vopr,
            }
        ],
        model="gpt-3.5-turbo",
    )

    content = chat_completion.choices[0].message.content
    mytext = str(content)
    print(mytext)


chat(vopr='') # ваш ворос