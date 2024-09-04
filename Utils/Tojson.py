import json


# look if a dictionary groqkey is present in yourkeys.json, if present return the dictionnary
def get_key(basename):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        if basename in data.keys():
            return data[basename]
        else:
            return None

def add_key(basename, keyname, key):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        data[basename][keyname] = key
    with open('YourAgents/yourkeys.json', 'w') as file:
        json.dump(data, file, indent=4)