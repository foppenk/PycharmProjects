import time
from datetime import datetime as dt
from tkinter import *
#Getting Address To Block From
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

#Making GUI
Window = Tk()
Window.title("Kelvin's Website Blocker")
Window.configure(width=700, height=500)

#List Of Blocked Websites
sites_list = []

#Making Blocker

while True:
    sites_list = input("What websites would you like blocked?: ")
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Sorry not allowed...")
    with open(hostsPath,'r+') as file:
        content = file.read()
    for site in sites_list:
        if site in content:
            pass
    else:
        file.write(redirect+" "+site+"\n")
else:
        with open(hostsPath,'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in websites):
                file.write(line)
                file.truncate()
                print ("Allowed access!")
time.sleep(5)






Window.mainloop()



