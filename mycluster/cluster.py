from mininet.topo import Topo


class MyCLusterTopo(Topo):

    def create_vm_hosts(self, hostname1, hostname2):
        return self.addHost(hostname1), self.addHost(hostname2)

    def create_vm_switches(self, switchname1, switchname2):
        return self.addSwitch(switchname1), self.addSwitch(switchname2)

    def create_vm_nodes(self, nodename1, nodename2, nodename3):
        return self.addSwitch(nodename1), self.addSwitch(nodename2), self.addSwitch(nodename3)

    def create_vm_links(self, host1, host2, switch1, switch2, node1, node2, node3):
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(switch1, node1)
        self.addLink(switch1, node2)
        self.addLink(switch2, node2)
        self.addLink(switch2, node1)
        self.addLink(node1, node3)
        self.addLink(node2, node3)

    def build(self):
        # HOSTS
        # vm1
        vm1_host1, vm1_host2 = self.create_vm_hosts('vm1_host1', 'vm1_host2')
        # vm2
        vm2_host1, vm2_host2 = self.create_vm_hosts('vm2_host1', 'vm2_host2')

        # Switches
        # vm1
        vm1_switch1, vm1_switch2 = self.create_vm_switches('vm1_switch1', 'vm1_switch2')

        # vm2
        vm2_switch1, vm2_switch2 = self.create_vm_switches('vm2_switch1', 'vm2_switch2')

        # Nodes
        # vm1
        vm1_node1, vm1_node2, vm1_node3 = self.create_vm_nodes('vm1_node1', 'vm1_node2', 'vm1_node3')

        # vm2
        vm2_node1, vm2_node2, vm2_node3 = self.create_vm_nodes('vm2_node1', 'vm2_node2', 'vm2_node3')

        # Links
        # vm1
        self.create_vm_links(vm1_host1, vm1_host2, vm1_switch1, vm1_switch2, vm1_node1, vm1_node2, vm1_node3)

        # vm2
        self.create_vm_links(vm2_host1, vm2_host2, vm2_switch1, vm2_switch2, vm2_node1, vm2_node2, vm2_node3)

        # create links between vm1 and vm2
        self.addLink(vm1_node1, vm2_node3)
        self.addLink(vm1_node2, vm2_node3)
        self.addLink(vm2_node1, vm1_node3)
        self.addLink(vm2_node2, vm1_node3)


topos = { 'mycluster': ( lambda: MyCLusterTopo() ) }