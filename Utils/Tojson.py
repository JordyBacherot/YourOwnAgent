import json
import os


# look if a dictionary groqkey is present in yourkeys.json, if present return the dictionnary
def get_key(apibase):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        if len(data[apibase]) != 0:
            return data[apibase]
        else:
            return None

def add_key(apibase, keyname, key):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        # verify if the key already exist
        if keyname in data[apibase]:
            return False
        data[apibase][keyname] = key
    with open('YourAgents/yourkeys.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def create_an_agent(apibase, agentname, agentkey, agentmodel):
    # verify if the file already exist
    if not os.path.exists(f'YourAgents/Agents/{agentname}.json'):
        return "This agent already exist"
    data = {"agentname" : agentname, "apibase" : apibase, "agentkey" : agentkey, "agentmodel" : agentmodel, "historique" : []}
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return None

