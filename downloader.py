import requests as rq
import os
import json


token = 'a358ef31a7b3820708688da20b65703c97e7c291'


def get_names(path):
    url = 'https://www.pythonanywhere.com/'
    method1 = '/api/v0/user/ariken/files/tree/?path={path}'
    site = rq.get(url + method1.format(path=path), headers={'Authorization': 'Token {}'.format(token)})
    files = json.loads(site.content)
    return files


def download_file(name):
    text = rq.get(url + method2.format(path=i), headers={'Authorization': 'Token {}'.format(token)})
    if not text.ok:
        raise ConnectionError
    directory = path + i[:i.rindex('/') + 1:]
    file = path + i
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass
    else:
        print('Error to make directory')
    file = open(file, 'wb')
    file.write(text.content)
    file.close()


url = 'https://www.pythonanywhere.com/'
method2 = '/api/v0/user/ariken/files/path{path}'

path = os.getcwd().replace('\\', '/')

directories = ['/home/ariken']
files = []

for i in directories:
    names = get_names(i)
    for name in names:
        if name[-1] == '/' and name in directories:
            continue
        elif name[-1] == '/':
            directories.append(name)
        elif name in files:
            continue
        else:
            files.append(name)
    print(i)


for i in files:
    download_file(i)
    print(i)
