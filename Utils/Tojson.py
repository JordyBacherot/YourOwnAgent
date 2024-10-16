import json
import os
from datetime import datetime, timedelta

import pandas as pd


# look if a specific dictionary is present in yourkeys.json, if present return the content of the dictionnary
def get_key(apibase):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        if len(data[apibase]) != 0:
            return data[apibase]
        else:
            return None

def get_keys():
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
    tab_keys=[]
    for base in data:
        for key in data[base]:
            tab_keys.append(key)
    return tab_keys

def delete_key(keyname):
    with open('YourAgents/yourkeys.json', 'r') as file:
        data = json.load(file)
        for base in data:
            if keyname in data[base]:
                del data[base][keyname]
    with open('YourAgents/yourkeys.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

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

def create_an_agent(apibase, agentname, agentmodel, agentkey=None):
    # verify if the file already exist

    if os.path.isfile(f'YourAgents/Agents/{agentname}.json'):
        return False
    if agentkey is None:
        data = {"agentname": agentname, "apibase": apibase, "agentmodel": agentmodel, "conversation": {"Default Conversation": {"historique": [], "context": "Réponds en Français. Tu es un chatbot d'assistance à un humain."}}}
    else :
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

def get_context(agentname, nameconversation):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        return data['conversation'][nameconversation]['context']

def set_context(agentname, nameconversation, context):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        data['conversation'][nameconversation]['context'] = context
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def delete_last_elmt_conversation(agentname, nameconversation):
    with open(f'YourAgents/Agents/{agentname}.json', 'r') as file:
        data = json.load(file)
        data['conversation'][nameconversation]['historique'].pop()
    with open(f'YourAgents/Agents/{agentname}.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def get_first_access():
    with open('YourAgents/moreconfig.json', 'r') as file:
        data = json.load(file)
        return data["first_access"]

def set_first_access():
    with open('YourAgents/moreconfig.json', 'r') as file:
        data = json.load(file)
        data["first_access"] = False
    with open('YourAgents/moreconfig.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def get_calendar_data():
    with open('YourAgents/data_schedule.json', 'r') as file:
        data = json.load(file)
        return data

def add_event_calendar(name, startDate, endDate, startTime, endTime):
    to_add_start = startDate + "T" + startTime
    to_add_end = endDate + "T" + endTime
    with open('YourAgents/data_schedule.json', 'r') as file:
        data = json.load(file)
        data['calendar_events'].append({"name": name, "start": to_add_start, "end": to_add_end})
    with open('YourAgents/data_schedule.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def add_task(name, description, warning_level, points):
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
        data['tasks'].append({"name": name, "description": description, "status": "To Do", "warning_level": warning_level, "points": points})
    with open('YourAgents/data_tasks.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def change_task_warning_level(name, warning_level):
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
        for task in data['tasks']:
            if task['name'] == name:
                task['warning_level'] = warning_level
    with open('YourAgents/data_tasks.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def change_task_status(name, status):
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
        for task in data['tasks']:
            if task['name'] == name:
                if status == "Done" and task['status'] != "Done":
                    date_du_jour = datetime.today().date()
                    add_point_day(str(date_du_jour), task['points'], data)
                task['status'] = status
    with open('YourAgents/data_tasks.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def get_tasks():
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
        return data['tasks']

def delete_task(name):
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
        for task in data['tasks']:
            if task['name'] == name:
                data['tasks'].remove(task)
    with open('YourAgents/data_tasks.json', 'w') as file:
        json.dump(data, file, indent=4)
    return True

def add_point_day(date, points, data):
    if date in data['points_on_week']:
        data['points_on_week'][date] += points
    else :
        data['points_on_week']= {date : points}
    return True

def get_data_week_points():
    with open('YourAgents/data_tasks.json', 'r') as file:
        data = json.load(file)
    # récupère le jour actuelle, les 3 jours précédents et les 3 jours suivants
    date_du_jour = datetime.today().date()
    tab_recap = []
    jours = [date_du_jour - timedelta(days=i) for i in range(3, 0, -1)]

    jours += [date_du_jour]

    jours += [date_du_jour + timedelta(days=i) for i in range(1, 4)]

    for jour in jours:
        if str(jour) in data['points_on_week']:
            tab_recap.append({"date": str(jour), "points": data['points_on_week'][str(jour)]})
        else :
            tab_recap.append({"date": str(jour), "points": 0})

    # transform the date by the day of the week (Monday, ...)
    for day in tab_recap:
        day["date"] = datetime.strptime(day["date"], '%Y-%m-%d').strftime('%A')

    # transform la data pd.dataframe
    tab_recap = pd.DataFrame(tab_recap)

    return tab_recap
