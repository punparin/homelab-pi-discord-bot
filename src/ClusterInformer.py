import os
import requests
from discord import Embed
from Utils import *

class ClusterInformer:
    def __init__(self):
        self.node_ips = get_node_ips()

    def get_node_info(self, node_ip):
        r = requests.get('http://' + node_ip + ':3000/api/stats')
        result = r.json()
        return result

    def get_nodes_info(self):
        nodes_info = []
        for node_name in self.node_ips:
            node_ip = self.node_ips[node_name]
            node_info = self.get_node_info(node_ip)
            node_info["name"] = node_name
            nodes_info.append(node_info)
        return nodes_info

    def get_nodes_embeds(self):
        embeds = []
        nodes_info = self.get_nodes_info()
        for node_info in nodes_info:
            embed = Embed(title=node_info["name"], color=0x00A300)
            embed.add_field(name="CPU", value="Temperature: {0}°C\nUsage: {1}%".format(
                node_info["cpu_temp"],
                node_info["cpu_percent"]
                )
            )
            embed.add_field(name="Memory", value="Usage: {0} GB / {1} GB ({2}%)".format(
                node_info["memory_used"],
                node_info["memory_total"],
                node_info["memory_percent"]
                )
            )
            embed.add_field(name="Disk", value="Usage: {0} GB / {1} GB ({2}%)".format(
                node_info["disk_used"],
                node_info["disk_total"],
                node_info["disk_percent"]
                )
            )
            embeds.append(embed)
        return embeds
