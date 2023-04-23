Hello,

The code I used for getting the pcap files for the different nodes:
```
tcpdump -i eth0 -w filename.pcap
```

This was the mergecap code in the docker shell for merging the pcap files:
```
mergecap -w full-take.pcap wuserver.pcap wuclient.pcap taskvent.pcap taskwork.pcap tasksink.pcap
```

To parsing out the different pcaps I used this code and separated the two based on port number:
```
tcpdump -n -r full-take.pcap port 7776 -w weather.pcap:
```
and,
```
tcpdump -n -r full-take.pcap port 5557 or port 5558 -w task.pcap
```

