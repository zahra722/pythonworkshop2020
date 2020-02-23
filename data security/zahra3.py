import time
from datetime import datetime as dt

website_list = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

host_path = r"/etc/hosts"
temp = r"hosts"
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours",dt.now())
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website+ "\n")    
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours...",dt.now())
    time.sleep(1)

            