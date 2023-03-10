#!/usr/bin/env python

from daemonize import Daemonize
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import paho.mqtt.publish as publish

pid = "/tmp/pi-rfid"

def main():
	while True:
		sleep(1)
		reader = SimpleMFRC522()
		try:
			id, text = reader.read()
			print(id)
			print(text)
			if id == "219303712431":
				print("Match, sending turn on/turn off signal")
				publish.single("BaTaTaAdb/pc","turn_on",hostname="test.mosquitto.org")
				sleep(8)
		except KeyboardInterrupt:
			print("\nTerminated")
			exit()
		finally:
			GPIO.cleanup()

daemon = Daemonize(app="pi-rfid", pid=pid, action=main)
daemon.start()