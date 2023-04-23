import socket
import pandas as pd
import graphviz

domain = pd.read_csv('domains.tsv', sep = '\t')['domain']
#print(domains)

dict = {}
ip = {}
fwd_dict = {}

plot_dict = {}
try:
    for domain in domain:
        dict[domain] = socket.getaddrinfo(domain, 443, type = socket.SOCK_STREAM)
        clean_ips = []

        for ip in dict[domain]:
            #print(f"{domain} : {ip[4][0]}")

            clean_ips.append(ip[4][0])

            fwd_dict[domain] = clean_ips


except:
    # print("n/a")
    pass


# print(fwd_dict)




i = 1






for key in fwd_dict:
    rev_dns = []
    for ip in fwd_dict[key]:
        try:
            
            # print(ip)
            rev_dns.append(socket.gethostbyaddr(str(ip))[0])

            plot_dict[key] = rev_dns
            print(plot_dict)


            
            # print(rev_dns)

        
            # for keys in rev_dns:
            #     for dns in rev_dns[keys]:
            #         weird_names = []



            



            # print(rev_dns)


        except socket.herror:
            # print('n/a' , i)
            # i+=1
            pass


