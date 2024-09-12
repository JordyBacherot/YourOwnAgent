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
        return False
    data = {"agentname" : agentname, "apibase" : apibase, "agentkey" : agentkey, "agentmodel" : agentmodel, "conversation" : {"Default Conversation": {"historique" : [], "context" : "Tu es un chatbot d'assistance à un humain."}}}
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
        return data['conversation'][nameconversation]['historique']

def addtohistorique(agentname, nameconversation, role, content):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        data['conversation'][nameconversation]['historique'].append({"role" : role, "content" : content})
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def getconversations(agentname):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        return data['conversation']

def addconversation(agentname, nameconversation, context):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        data['conversation'][nameconversation] = {"historique" : [], "context" : context}
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)

def getfirstconversation(agentname):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        return list(data['conversation'].keys())[0]

def delete_agent(agentname):
    os.remove(f'YourAgents/Agents/{agentname}.json')
    return True

def deleteconversation(agentname, nameconversation):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        del data['conversation'][nameconversation]
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True