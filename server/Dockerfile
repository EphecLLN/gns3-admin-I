FROM labo-admin-1/base:latest

# Install journalctl
RUN apt install -y systemd

# Use systemctl replacement for docker
RUN apt install -y python3
COPY systemctl.py /usr/bin/systemctl

RUN apt clean


