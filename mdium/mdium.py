import requests
import os
import json
import frontmatter

def init(token):
    headers = {'Authorization': 'Bearer {}'.format(token)}
    r = requests.get('https://api.medium.com/v1/me', headers=headers)
    user_data = r.json()['data']
    conf = {
            'token': token,
            'id': user_data['id']
           }
    with open(os.path.expanduser('~/.mdium'), 'w') as f:
        json.dump(conf, f)


def read_conf():
    with open(os.path.expanduser('~/.mdium'), 'r') as f:
        conf = json.load(f)
        return conf


def post(mdfile, public=False):
    conf = read_conf()
    with open(mdfile, 'r') as f:
        content = frontmatter.load(f)

    if public:
        status = "public"
    else:
        status = "draft"

    headers = {'Authorization': 'Bearer {}'.format(conf['token'])}
    body = {
            'title': content['title'],
            'contentFormat': 'markdown',
            'content': content.content,
            'tags': content['tags'],
            'publishStatus': status
           }
    r = requests.post(
            'https://api.medium.com/v1/users/{}/posts'.format(conf['id']), 
            headers=headers,
            json=body
        )
    print('Done! Your post has been published at {}'.format(r.json()['data']['url']))

