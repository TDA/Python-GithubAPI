__author__ = 'saipc'

import requests
from pretty_print_json import pretty_print_json
from passfile import password

data_store = 'my_repo_data.json'
# enter password here
# get my repo
# r = requests.get("https://api.github.com/user/repos", auth=('tda', ''))
# print r.status_code

# get repos of any user
username = 'tda'
# this needs to be changed once u get past 100 repos :)
r = requests.get("https://api.github.com/users/" + username + "/repos?page=1&per_page=100", auth=('tda', password))

print r.status_code
print r.text

pretty_print_json(r.text, data_store)
