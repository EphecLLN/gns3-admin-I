import os
import docker
images = ["base","client", "server", "dhcp", "dns", "web", "mail","router","super-server" ] 
client = docker.from_env()
for image_name in images :
    if os.path.isdir("./"+image_name) and os.path.exists(f"./{image_name}/Dockerfile") : 
        print(image_name)
        client.images.build(tag=f"labo-admin-1/{image_name}", path=f"./{image_name}/")
