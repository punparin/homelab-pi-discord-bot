import os
import subprocess
from Utils import *

class ClusterController:
    def __init__(self):
        self.node_ips = get_node_ips()
        self.master_node_ip = os.getenv('MASTER_NODE_IP')

    def reboot_node(self, ip):
        subprocess.call(['ssh', '-o', 'StrictHostKeyChecking=no', '-i', './id_rsa', 'root@{0}'.format(ip), 'reboot || true'])

    def reboot(self, target):
        if target == "cluster":
            for node_name in self.node_ips:
                node_ip = self.node_ips[node_name]
                if self.master_node_ip == node_ip:
                    continue
                self.reboot_node(node_ip)
            self.reboot_node(self.master_node_ip)
        else:
            node_ip = self.node_ips[target]
            self.reboot_node(node_ip)
