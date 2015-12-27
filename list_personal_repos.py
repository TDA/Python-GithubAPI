__author__ = 'saipc'

import json
from collections import OrderedDict
from pretty_print_json import pretty_print_json

data_store = 'my_repo_data.json'
data_store2 = 'my_personal_repo_data.json'

with open(data_store, 'r') as wfile:
    personalRepos = []
    reposJSON = json.loads(wfile.read(), object_pairs_hook=OrderedDict)
    print len(reposJSON)
    for repo in reposJSON:
        if (repo['fork'] == False):
            print repo['name']
            personalRepos.append(repo)

    print len(personalRepos)
    pretty_print_json(json.dumps(personalRepos), data_store2)
