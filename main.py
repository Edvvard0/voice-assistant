import os                      # для запуска файлов
import speech_recognition      # для распознавания голоса
import webbrowser              # для открытия сайтов
from openai import OpenAI      # для работы с chat Gpt

import time                    # для создания пауз между голосовыми ответами
import pyttsx3                 # для озвучки текста

from translate import Translator # для функции переводчик
from token import token        # импорт токена для работы ChatGpt

# Это словарь с названиями функций и фразами, которыми их можно вызвать
commands_dict = {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
        'play_music': ['включить музыку', 'дискотека'],
        'cook_buter': ['бутерброд'],
        'youtube': ['открой youtube', 'youtube'],
        'wether': ['какая погода', 'погода'],
        'chat': ['чат', 'спроси у чата'],
        'google': ['спроси у гугла', 'найди в гугле'],
        'translate': ['переводчик', 'переведи']
}

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def saing(my_text):
    '''Функция для озвучки текста и вывода его в консоль'''

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)

    engine.say(my_text)
    engine.runAndWait()

    print(my_text)


def lisen(f_main=False) -> str:
    '''Фунция служит для считывания голоса '''

    query = ''

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(query)

            return query


    except:
        print('не получилось распознать речь')

        if f_main:
            time.sleep(1)
            main()


def greeting():
    """Greeting function"""

    saing('Привет Edward')
    time.sleep(1)
    main()


def create_task():
    """Создание файла со списком дел"""

    print('Что добавим в список дел?')

    query = lisen()

    with open('todo-list.txt', 'a') as file:
        file.write(f'!!! {query}\n')

    saing(f'Задача {query} добавлена в todo-list!')

    time.sleep(1)
    main()


def play_music():
    """Функция включает музыку"""

    saing('Танцуем')
    os.startfile('D:/kisskold-kogda-ty-ulybaeshsya-dnevnik-dzhessiki-remix-mp3.mp3')

    main()


def youtube():
    '''Функция открывает ютуб'''

    webbrowser.open('https://www.youtube.com')
    mytext = 'открыт youtube'
    saing(mytext)


def wether():
    '''Функция открывает сайт с погодой'''
    webbrowser.open('https://www.gismeteo.ru/weather-bakhchisaray-11364/?ysclid=ltydlid3no566608890')
    mytext = 'открыт сайт с погодой'
    saing(mytext)
    time.sleep(1)
    main()


def chat():
    '''Функция подключается к chatGpt и отвечает на вопрос пользователя'''

    saing('чат слушает')

    vopr = lisen()
    print(vopr)
    client = OpenAI(
        # This is the default and can be omitted
        # git ignore
        api_key = token,
    )

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": vopr,
            }
        ],
        model = "gpt-3.5-turbo",
    )

    content = chat_completion.choices[0].message.content
    mytext = str(content)

    saing(mytext)

    time.sleep(7)
    main()


def google():
    '''Функция ищет в google вопрос пользователя'''

    saing('что найти')
    query = lisen()
    zapros = str(query).replace(' ', '+')
    ssilka = f'https://www.google.com/search?q={zapros}'
    webbrowser.open(ssilka)
    saing('готово')
    main()


def translate():
    '''Функция переводит фразу пользователя на английский'''

    print('что перевести')
    text_translate = lisen()
    # перевод

    text_translate = str(text_translate).replace(' ', ', ')
    translator = Translator(from_lang="ru", to_lang="en")

    result = translator.translate(text_translate)

    text_en = result
    print(text_en)
    engine = pyttsx3.init()

    engine.setProperty('rate', 115)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text_en)
    engine.runAndWait()


def main():
    '''Основная функция, которая вызывает фунции,
     если нашла совпадение в списке фраз'''

    query = lisen(f_main=True)
    print(query)

    for k, v in commands_dict.items():
        if query in v:
            print('yes')
            print(globals()[k]())
    else:
        print('команда не распознана')
        lisen(f_main=True)


if __name__ == '__main__':
    main()



