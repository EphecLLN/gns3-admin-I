# GNS3 Lab for the Admin I course

During the practice session of the Admin I course, students use a GNS3 lab to configure several linux services (DHCP, DNS, Web and Mail). This repository hosts the files used to build the devices used by the GNS3 simulator.  


<img width="835" alt="Capture d’écran 2024-10-14 à 20 35 05" src="https://github.com/user-attachments/assets/f27d7956-1cf5-424a-9d0e-3a83696a28db">

To setup the lab, you have to build the Docker images.  You can use the build.py script, provided you installed the docker python module.  

In GNS3, you add new devices to the pool by going into the following menu : ```Edit > Preference > Docker > Docker Containers```. 

For this lab, you need to create the following devices : 

- a router
- a client
- a DHCP server
- a DNS server
- a web server
- a mail server.

For each, select the appropriate Docker image, and configure the device with the following parameters : 

- Use one network adapter for client and servers, two for the router
- Use ```/bin/bash``` as startup command
- In the Advanced tab, add the ```/etc/``` directory to the persistent folders.  This way, all configurations in /etc/ will be saved between work sessions.
- If you wish, you can change the device icon.

You should get a screen similar to this one after configuring each node.  

<img width="985" alt="Capture d’écran 2024-10-14 à 20 33 15" src="https://github.com/user-attachments/assets/ca872a3e-e53d-422d-92b6-6670bfe49d0f">
