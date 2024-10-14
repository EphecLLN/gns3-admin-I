FROM labo-admin-1/base:latest

# DHCP
RUN DEBIAN_FRONTEND=noninteractive apt install -y isc-dhcp-client

# IP routing activation
RUN sed -i 's/^#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf

# NAT
RUN DEBIAN_FRONTEND=noninteractive apt install -y iptables
COPY startup.sh /usr/local/bin/startup.sh 
RUN chmod +x /usr/local/bin/startup.sh

RUN apt clean

ENTRYPOINT ["/usr/local/bin/startup.sh"]
