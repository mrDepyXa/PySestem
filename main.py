import os
from defer import *
from Data import *

if User == "None":
	new_name_user()
else:
	pass

Version_pySestem = "0.0.2"
print(f"PySestem >> Welcom to pyses, {User}!")

while True:
	DIA = input("PySestem >> ")
	if DIA == "open_file":
		print("Locate the file...")
		pute = input(f"{NoRoot}")
		open_file(pute)
	elif DIA == "create_new_file":
		print("""Specify an existing folder, followed by a file with the format.
For example: (PySestem:/User/pack/file.fomat)""")
		pute = input(f"{NoRoot}")
		create_new_file(pute)
	elif DIA == "create_pap":
		print("Enter the location of an existing folder, and enter the folder you want to create.")
		pute = input(f"{NoRoot}")
		create_pap(pute)
	elif DIA == "delete_file":
		print("""Maintain the location of the file with the file format...""")
		pute = input(f"{NoRoot}")
		delete_file(pute)
	elif DIA == "delete_pap":
		print("Enter the location of the folder to delete")
		pute(f"{NoRoot}")
	elif DIA == "full_file":
		full_file()
	elif DIA == "open_internet":
		print("""Keep a link to the site you want to open...""")
		adrisat = input("open_internet http://")
		open_internet(adrisat)
	elif DIA == "download_file":
		print("""Keep a link to the site you want to download file...""")
		adrisat = input("download_file http://")
		download_file(adrisat)
	elif DIA == "seput_google":
		editGmail = input("Enter your email...\n")
		editPass = input("Enter your passwsrd to email...\n")
		editSignature = input("Enter your signature: ")
		google_date(editGmail, editPass, editSignature)
	elif DIA == "help":
		print(f"""PySestem version: {Version_pySestem}
 open_file - command that opens the file to read the code.
 create_new_file - command that creates a new file.
 create_new_pap - a team that creates a new folder in the city you specify.
 delete_file - command that starts deleting the file.
 delete_pap - command that opens the file to read the code.
 open_internet - the launching team opens the site.
 download file - command that starts downloading a file from the site.
 seput_google - google gmail settings.
""")
	else:
		print(f""""{DIA}" the command does not exist in the pysestem!""")
