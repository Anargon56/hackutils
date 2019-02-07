import os
import time


def stress_test_install():
	ans = ""
	
	while True:
		os.system('cls')

		print("""
	   TERMUX UTILS
	 (Stress testing)
	/================/
	/1/ MODoS (http/tcp/udp)
	/2/ SFlooder (http)
	/Q/ Main menu
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			print("[MODoS] Starting installation\n")
			os.system("sh ./lib/install_modos.sh")
			print("\nDONE")
		elif ans == '2':
			print("[SFlooder] Starting installation\n")
			os.system("sh ./lib/install_sflooder.sh")
			print("\nDONE")
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def fishing_install():
	ans = ""
	
	while True:
		os.system('cls')

		print("""
	   TERMUX UTILS
	    (Fishing)
	/================/
	/1/ Social Fish
	/2/ Weeman
	/Q/ Main menu
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			pass
		elif ans == '2':
			pass
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def fishing_install():
	ans = ""
	
	while True:
		os.system('cls')

		print("""
	   TERMUX UTILS
	 (Info gathering)
	/================/
	/1/ RED HAWK
	/2/ 
	/Q/ Main menu
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			pass
		elif ans == '2':
			pass
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def main_menu():
	ans = ""
	
	while True:
		os.system('cls')

		print("""
	   TERMUX UTILS
	   (Main  menu)
	/================/
	/1/ Stress testing
	/2/ Fishing
	/3/ Info gathering
	/4/ Exploits
	/Q/ Exit
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			stress_test_install()
		elif ans == '2':
			pass
		elif ans == '3':
			pass
		elif ans == '4':
			pass
		elif ans.lower() == 'q':
			break
		else:
			print("Wrong input!")
			time.sleep(2)

if __name__ == '__main__':
	main_menu()
