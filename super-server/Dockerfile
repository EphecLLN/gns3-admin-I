FROM labo-admin-1/server:latest
RUN apt update

#--------------------------------
# DHCP
RUN apt install -y isc-dhcp-server
RUN sed -i "s/INTERFACESv4=\"\"/INTERFACESv4=\"eth0\"/g" /etc/default/isc-dhcp-server
# Create lease file
RUN touch /var/lib/dhcp/dhcpd.leases

#--------------------------------
# DNS
RUN apt install -y bind9 bind9utils
# Setup for bind
RUN chmod +r /etc/bind/rndc.key
RUN mkdir /var/log/named/
RUN chown -R bind:bind /var/log/named/
RUN touch /var/log/named/misc.log
RUN touch /var/log/named/query.log

#--------------------------------
# Web
RUN apt install -y apache2

#--------------------------------
# Mail
RUN apt install -y postfix mutt mailutils
RUN apt install -y dovecot-imapd dovecot-pop3d

# Cleanup
RUN apt clean


