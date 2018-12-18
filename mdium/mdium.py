import requests
import os
import json
import frontmatter
import sys

def init(token):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    r = requests.get('https://api.medium.com/v1/me', headers=headers)
    try:
        user_data = r.json()['data']
    except KeyError:
        print('error: invalid integration token')
        sys.exit(1)

    conf = {
            'token': token,
            'id': user_data['id']
           }
    with open(os.path.expanduser('~/.mdium'), 'w') as f:
        json.dump(conf, f)

    print('Saved token and author ID at {}'.format(os.path.expanduser('~/.mdium')))


def read_conf():
    try:
        with open(os.path.expanduser('~/.mdium'), 'r') as f:
            conf = json.load(f)
            return conf
    except FileNotFoundError:
        print('error: the `~/.mdium` file is missing. Have you run `mdium init <token>`?')
        sys.exit(1)


def publish(mdfile):
    conf = read_conf()
    try:
        with open(mdfile, 'r') as f:
            content = frontmatter.load(f)
    except FileNotFoundError:
        print('error: the file specified was not found')
        sys.exit(1)
    try: 
        headers = {'Authorization': 'Bearer {}'.format(conf['token'])}
        body = {
                'title': content['title'],
                'contentFormat': 'markdown',
                'content': content.content,
                'tags': content['tags'],
                'publishStatus': content['status']
               }
    except KeyError:
        print('error: check the frontmatter in your markdown doc')
        sys.exit(1)
    r = requests.post(
            'https://api.medium.com/v1/users/{}/posts'.format(conf['id']), 
            headers=headers,
            json=body
        )
    print('Done! Your post has been published at {}'.format(r.json()['data']['url']))

