__author__ = 'saipc'

import requests

data_store = 'my_repo_data.json'
# enter password here
# get my repo
r = requests.get("https://api.github.com/user/repos", auth=('tda', ''))
print r.status_code

# get repos of any user
username = 'tda'
r = requests.get("https://api.github.com/users/" + username + "/repos", auth=('tda', ''))

print r.status_code
print r.text

with open(data_store, 'a') as file:
    file.write(r.text)