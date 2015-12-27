__author__ = 'saipc'

import requests
# enter password here
r = requests.get("https://api.github.com/user/repos", auth=('tda', ''))
print r.status_code

print r.text

with open('my_repo_data.json', 'a') as file:
    file.write(r.text)