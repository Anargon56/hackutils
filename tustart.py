import os
import time


def stress_test_install():
	ans = ""
	
	while True:
		os.system('clear')

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
			print("\n[MODoS] DONE")
			input("Press ENTER to continue")
		elif ans == '2':
			print("[SFlooder] Starting installation\n")
			os.system("sh ./lib/install_sflooder.sh")
			print("\n[SFlooder] DONE")
			input("Press ENTER to continue")
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def fishing_install():
	ans = ""
	
	while True:
		os.system('clear')

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
			print("[SFish] Starting installation\n")
			os.system("sh ./lib/install_sfish.sh")
			print("\n[SFish] DONE")
			input("Press ENTER to continue")
		elif ans == '2':
			print("[Weeman] Starting installation\n")
			os.system("sh ./lib/install_weeman.sh")
			print("\n[Weeman] DONE")
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def gathering_tools_install():
	ans = ""
	
	while True:
		os.system('clear')

		print("""
	   TERMUX UTILS
	 (Info gathering)
	/================/
	/1/ RED HAWK
	/Q/ Main menu
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			print("[RED_HAWK] Starting installation\n")
			os.system("sh ./lib/install_rhawk.sh")
			print("\n[RED_HAWK] DONE")
			input("Press ENTER to continue")
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def exploits_install():
	ans = ""
	
	while True:
		os.system('clear')

		print("""
	   TERMUX UTILS
	 (Exploits usage)
	/================/
	/1/ Metasploit-framework
	/2/ Routersploit
	/3/ Websploit
	/Q/ Main menu
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			print("[Metasploit] Starting installation\n")
			os.system("sh ./lib/install_msf.sh")
			print("\n[Metasploit] DONE")
			input("Press ENTER to continue")
		elif ans == '2':
			print("[Routersploit] Starting installation\n")
			os.system("sh ./lib/install_rsploit.sh")
			print("\n[Routersploit] DONE")
			input("Press ENTER to continue")
		elif ans == '3':
			print("[Websploit] Starting installation\n")
			os.system("sh ./lib/install_wsploit.sh")
			print("\n[Websploit] DONE")
			input("Press ENTER to continue")
		elif ans.lower() == 'q':
			break
			main_menu()
		else:
			print("Wrong input!")
			time.sleep(2)

def main_menu():
	ans = ""
	
	while True:
		os.system('clear')

		print("""
	   TERMUX UTILS
	   (Main  menu)
	/================/
	/1/ Stress testing
	/2/ Fishing
	/3/ Info gathering
	/4/ Exploitation
	/Q/ Exit
	/================/
			""") 

		ans = input("> ")

		if ans == '1':
			stress_test_install()
		elif ans == '2':
			fishing_install()
		elif ans == '3':
			gathering_tools_install()
		elif ans == '4':
			exploits_install()
		elif ans.lower() == 'q':
			break
		else:
			print("Wrong input!")
			time.sleep(2)

if __name__ == '__main__':
	main_menu()
