__author__ = 'saipc'

import requests
import json
from pretty_print_json import pretty_print_json
from passfile import password
from collections import OrderedDict

data_store = 'my_personal_repo_data.json'
data_store2 = 'languages_data.json'

with open(data_store, 'r') as wfile:
    language_data = {}
    username = 'tda'
    reposJSON = json.loads(wfile.read(), object_pairs_hook=OrderedDict)
    print len(reposJSON)
    for repo in reposJSON:
        # print repo['name']
        r = requests.get("https://api.github.com/repos/" + username + "/" + repo['name'] + "/languages", auth=('tda', password))
        print r.status_code
        print r.text

        # create a dictionary of repo => languages in said repo
        language_data[repo['name']] = r.text
    print language_data

    pretty_print_json(json.dumps(language_data), data_store2)
