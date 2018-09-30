# import the time and datetime modules to use time/date functions
import time
from datetime import datetime as dt

# paths to our hosts file and to the redirect url which happens to be our local host address
hosts_temp = "hosts-example"
hosts_path = r"/etc/hosts"
redirect = "127.0.0.1"
# a list of wesbites that we want to block to prevent us from being able to access
websites_list = ["www.facebook.com", "facebook.com"]

# create a loop that will continuously run, it will check to see if the current time is considered work hours
# work hours are being defined here from 8 AM to 4 PM
while True:
  if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):	
		print("Working Hours!")
		# open and read the sample host file
		with open(hosts_temp, "r+") as file:
			content = file.read()
			print(content)
			# iterate through website list and add website to the hosts file to be blocked if it is not already on there
			for website in websites_list:
				if website in content:
					pass
				else: 
					file.write(redirect + " " + website + "\n")
	else:
		# if the current time is not work hours, then read the hosts file and delete any trace of the blocked websites
		with open(hosts_path, "r+") as file:
			content = file.readlines()
			# print(content)  
			file.seek(0)
			# we check to see if any websites exist in the hosts file
			# if they do exist in the hosts file, rewrite every line that does not have a website (from website_list) name and delete any text that was there previously
			# This updates the hosts file with text that does not include a website name, therefore no websites will be blocked
			for line in content:
				if not any(website in line for website in websites_list):
					file.write(line)
			file.truncate()
		print("Not work hours")
	# wait 5 seconds before checking to see it the current time is during work hours or not
	time.sleep(5)