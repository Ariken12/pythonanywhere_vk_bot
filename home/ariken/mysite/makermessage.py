import os
import importlib
import vkapi
from classcom import command_list
from random import randint


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost,
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)
    return d[lenstr1 - 1, lenstr2 - 1]


def load_modules():
    files = os.listdir("mysite/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def send_answer(text, attachment, user_id):
    print('Request:', text)
    body = text.split()[0]
    message = "Прости, не понимаю"
    distance = len(body)
    command = None
    key = ''
    for c in command_list:
        for k in c.keys:
            d = damerau_levenshtein_distance(body.lower(), k)
            if d < distance:
                distance = d
                command = c
                key = k
                if distance == 0:
                    message, attachment = c.process(text, attachment, user_id)
    if distance < len(body) * 0.3:
        message, attachment = command.process(text, attachment, user_id)
        print('Correct:', key)
    print('Answer:', message)
    if message != 'Прости, не понимаю':
        vkapi.send_message(user_id, message, attachment)


def create_answer(data):
    data = data['message']
    load_modules()
    user_id = data['peer_id']
    if data['text'][0] == '[':
        data['text'] = data['text'][data['text'].index(']')+2::]
    send_answer(data['text'], data['attachments'], user_id)


