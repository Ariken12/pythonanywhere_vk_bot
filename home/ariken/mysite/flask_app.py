from flask import Flask, request, json
from params import confirmation_token, token
from makermessage import create_answer

print('Fuck Emperor!')

app = Flask(__name__)

def ifin(data, text):
    return True if text in data["object"]["body"].lower() else False


@app.route('/')
def hello_world():
    return 'Hi, I am bot!!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():

        return 'not vk'

    if data['type'] == 'confirmation':

        return confirmation_token

    elif data['type'] == 'message_new':

        create_answer(data['object'])

        return 'ok'

    else:
        print(data['type'])
