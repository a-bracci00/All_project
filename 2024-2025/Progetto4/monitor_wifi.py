
#!/usr/bin/env python

import subprocess
import time
import curses

modem_ip = "192.168.1.1"

wifi_interface = "wlan1"

stdscr = curses.initscr()

def get_signal_quality():
	result = subprocess.run(["iw", "dev", wifi_interface, "link"], capture_output=True, text=True)
	lines = result.stdout.split("\n")
	for line in lines:
		if "signal" in line:
			return line.split(" ")[1]
		
def get_link_quality():
	link_quality_result = subprocess.run(["iwconfig", wifi_interface], capture_output=True, text=True)
	link_quality_line = [line for line in link_quality_result.stdout.split("\n") if "Link Quality" in line][0]
	link_quality = link_quality_line.split('=')[1].split('/')[0]
	return link_quality

while True:
	signal_quality = get_signal_quality()

	link_quality = get_link_quality()
	
	ping_result = subprocess.run(["ping", "-c", "1", modem_ip], capture_output=True, text=True)
	ping_output = ping_result.stdout[98:110] + ping_result.stdout[110:]

	stdscr.clear()	
	stdscr.addstr(f" | Link Quality: {link_quality}\n | Qualità del segnale: {signal_quality}\n | Risultato del ping: {ping_output}\n")
	stdscr.refresh()

	time.sleep(0.1)

curses.endwin()
