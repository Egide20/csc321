import netifaces
import ipaddress

netiface = netifaces.interfaces()
# for i in netiface:
#     print(netifaces.ifaddresses(i))

mkeys = {}



for i in netiface:
    try:
        
        addrs = netifaces.ifaddresses(i)
        ipv4 = (addrs[netifaces.AF_INET])
        #print((ipv4)[0]['addr'])
        mkeys[i] = ipv4
    except (KeyError):

        ipv6 = (addrs[netifaces.AF_INET6])
        #print(ipv6)
        mkeys[i] = ipv6

       

def get_interfaces():
    
    #returns a list of all interfaces on this host
    return netiface


def get_mac(interface):
    nkeys = {}
    for i in netiface:
        addrs = netifaces.ifaddresses(i)
        mac = addrs[netifaces.AF_LINK][0]['addr']
        if mac == "":
            pass
        else:    
            mkeys[i] = mac
        
    addrs = netifaces.ifaddresses(interface)
    
    return ('the mac adress of' + interface + 'is: ' + mkeys[interface])



    

def get_ips(interface):
    ip_dict = {}
    try:

        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['addr']
        #print(ipv4i)
        ip_dict['v4'] = ipv4i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print('does not have ipv4')

    try: 
        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['addr']
        ip_dict['v6'] = ipv6i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print('does not have ipv6') 

    print("the ip addresses are; ")
    print(ip_dict)       



def get_netmask(interface):
    netmask = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        #print(ipv4i)
        netmask['v4'] = ipv4i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print()

    try: 
        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['netmask']
        netmask['v6'] = ipv6i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print() 
    print("the netmasks are; ")
    print(netmask)


def get_network(interface):
    network = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        #print(ipv4i)
        network['v4'] = ipv4i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print()

    try: 
        addrs = netifaces.ifaddresses(interface)
        #print(mkeys[interface][0]['addr'])
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['broadcast']
        network['v6'] = ipv6i
        # print(addrs[netiface.AF_INET6[0]['addr']])
    except:
        print() 

    print(network)


get_interfaces()

net = input("which one do you want to see")

get_mac(net)

get_ips(net)

get_netmask(net)

get_network(net)


# for i in netiface:
#     get_ips(i)