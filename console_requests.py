import requests as rq
from params import console_id, token


token = 'a358ef31a7b3820708688da20b65703c97e7c291'
console_id = '16080615'


url = 'https://www.pythonanywhere.com'
method = '/api/v0/user/ariken/consoles/{}/send_input/'.format(console_id)

console_input = 'ls\n'

answer = rq.post(url+method, headers={'Authorization': 'Token {}'.format(token)}, json={'input': console_input})

