__author__ = 'saipc'

import json
from collections import OrderedDict

# almost the same as pretty_print_json, but sorts the keys
def sort_json(data, file = None):
    parsed_json = json.loads(data, object_pairs_hook=OrderedDict)
    print parsed_json
    pretty_json = json.dumps(parsed_json, indent=4, sort_keys=True)
    print pretty_json
    if file:
        with open(file, 'w') as wfile:
            wfile.write(pretty_json)
    else:
        print pretty_json

with open('languages_data.json', 'r') as data:
    sort_json(data.read(), 'languages_data_sorted.json')