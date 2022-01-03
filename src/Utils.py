import json
from discord_slash.utils.manage_commands import create_choice

def get_node_ips():
    with open("config.json", encoding = 'utf-8') as f:
        data = json.load(f)
        f.close()
        return data

def get_discord_choices():
    node_ips = get_node_ips()
    cluster_choice = create_choice(name="cluster", value="cluster")
    choices = [cluster_choice]
    for node_name in node_ips:
        new_choice = create_choice(name=node_name, value=node_name)
        choices.append(new_choice)
    return choices
