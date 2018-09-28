# import the time and datetime modules to use time/date functions
import time
from datetime import datetime as dt

# paths to our hosts file and to the redirect url which happens to be our local host address
hosts_path = r"/etc/hosts"
redirects = "127.0.0.1"
# a list of wesbites that we want to block to prevent us from being able to access
websites_list = ["www.facebook.com", "facebook.com"]

# create a loop that will continuously run, it will check to see if the current time is considered work hours
# work hours are being defined here from 8 AM to 4 PM
while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Time to work!")
	else:
		print("This is not during work hours")
	time.sleep(5)