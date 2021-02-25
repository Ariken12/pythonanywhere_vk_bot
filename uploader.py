import requests as rq
import os

token = 'a358ef31a7b3820708688da20b65703c97e7c291'

url = 'https://www.pythonanywhere.com'
method1 = '/api/v0/user/ariken/files/path{path}'
method2 = '/api/v0/user/ariken/webapps/ariken.pythonanywhere.com/reload/'
files = []

need_way = 'home'
path = os.getcwd() + '\\' + need_way

queue = []

for i in os.listdir(path):
    queue.append(path + '\\' + i)

while queue:
    way = queue.pop(0)
    way_is_file = os.path.isfile(way)
    way_is_directory = not way_is_file
    if way_is_directory:
        for i in os.listdir(way):
            queue.append(way + '\\' + i)
    elif way_is_file and (way not in files):
        files.append(way)
    else:
        continue

for name in files:
    path = '/' + name[name.index(need_way)::].replace('\\', '/')
    print(url + method1.format(path=path))
    os.system('copy ' + name + ' content')
    content = open('content', 'rb')
    a = rq.post(url + method1.format(path=path), headers={'Authorization': 'Token {}'.format(token)}, files={'content':content})
    print(a.status_code)


a = rq.post(url+method2, headers={'Authorization': 'Token {}'.format(token)})
print(a.status_code)

