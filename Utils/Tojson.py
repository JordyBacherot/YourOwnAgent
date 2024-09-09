import json
import os


# look if a specific dictionary is present in yourkeys.json, if present return the content of the dictionnary
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

    if os.path.isfile(f'YourAgents/Agents/{agentname}.json'):
        print("This agent already exist")
        return False
    data = {"agentname" : agentname, "apibase" : apibase, "agentkey" : agentkey, "agentmodel" : agentmodel, "historique" : {"1": {"conversation" : [], "context" : "Tu es un chatbot d'assistance à un humain."}}}
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True


def get_all_agents():
    agents = []
    for file in os.listdir('YourAgents/Agents'):
        if file.endswith('.json'):
            with open(f'YourAgents/Agents/{file}', 'r') as f:
                data = json.load(f)
                agents.append(data)
    return agents

def gethistorique(agentname, nameconversation):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        print(data)
        return data['historique'][nameconversation]['conversation']