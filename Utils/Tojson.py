import json


# look if a dictionary groqkey is present in yourkeys.json, if present return the dictionnary
def get_key(apibase):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        if apibase in data.keys():
            return data[apibase]
        else:
            return None

def add_key(apibase, keyname, key):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        data[apibase][keyname] = key
    with open('YourAgents/yourkeys.json', 'w') as file:
        json.dump(data, file, indent=4)

def create_an_agent(apibase, agentname, agentkey, agentmodel):
    data = {"agentname" : agentname, "apibase" : apibase, "agentkey" : agentkey, "agentmodel" : agentmodel}
    with open(f'YourAgents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
