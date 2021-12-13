import ctypes
import os
import sys
import random
import time
import shutil
from ctypes import *

def isAdmin():
	try:
		is_admin = (os.getuid() == 0)
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
	return is_admin

def main():
	if(len(sys.argv) != 2):
		print("Error usage is: python russian_roulette.py [Number of bullets (1 to 6)]")
	else:
		if(sys.argv[1].isdigit() and int(sys.argv[1]) > 0 and int(sys.argv[1]) < 7):
			bullet = random.randint(1,6)
			revolver = []

			for i in range(1, int(sys.argv[1]) + 1):
				revolver.append(i)

			if(bullet in revolver):
				print("Your computer is kill, say goodbye")
				#time.sleep(2)
				if os.name == 'nt':
					print("Insert Delete system 32 here")
					#!!! DO NOT UNCOMMENT THIS --> while(True):
						#!!! DO NOT UNCOMMENT THIS --> disable_input = ctypes.windll.user32.BlockInput(True)
						#!!! DO NOT UNCOMMENT THIS --> os.system('takeown /f C:\\Windows\\System32')
						#!!! DO NOT UNCOMMENT THIS --> os.system('cacls C:\\Windows\\System32')
						#!!! DO NOT UNCOMMENT THIS --> shutil.rmtree("C:\\Windows\\System32", ignore_errors=True)
						#!!! DO NOT UNCOMMENT THIS --> os.system('shutdown /s /t 1')
				else:
					print("Sudo rm -rf --no-preserve-root /")
					#!!! DO NOT UNCOMMENT THIS --> os.system('sudo rm -rf --no-preserve-root /')
			else:
				print("Your computer lives... for now")

		elif (not sys.argv[1].isdigit()):
			print("Error usage is: python russian_roulette.py [Number of bullets (1 to 6)]")
		elif (int(sys.argv[1]) < 1 or int(sys.argv[1]) > 6):
			print("Error usage is: python russian_roulette.py [Number of bullets (1 to 6)]")
		else:
			print("Error usage is: python russian_roulette.py [Number of bullets (1 to 6)]")

if __name__ == "__main__":
	if(isAdmin()):
		main()
	else:
		print("This program can only be run with administrator privileges, please try again")