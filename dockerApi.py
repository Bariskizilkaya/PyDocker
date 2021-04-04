import docker
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

client =docker.from_env()
#It pulls any images
#print(client.images.pull("selenium/standalone-firefox"))
#Images list
#print(client.images.list())
#It runs container and it ll add the created container to containers list
print("[*]Containers are starting.")

def walkThroughContainers(port):
    ts=webdriver.Remote("http://localhost:"+str(port)+"/wd/hub", DesiredCapabilities.FIREFOX)
    ts.get('http://www.google.com:80/')
    print("Port:"+str(port)+" Title of Website: "+ts.title) 

containers=[["selenium/standalone-firefox",{'4444/tcp': 1230}],
            ["selenium/standalone-firefox",{'4444/tcp': 1231}],
            ["selenium/standalone-firefox",{'4444/tcp': 1232}]]



for con in containers:
    client.containers.run(con[0],detach=True,ports=con[1])

print(client.containers.list())

sleep(7)
for con in containers:
    walkThroughContainers(con[1]['4444/tcp'])


for container in client.containers.list():
    container.stop()

print("[*]After The Stopping of Containers.")
print(client.containers.list())

