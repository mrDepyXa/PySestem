import os
import defer

print("Hello World")
while True:
	DIA = input("PySestem > ")
	if DIA == "open_file":
		print("Locate the file...")
		pute = input("PySestem:/User/")
		defer.open_file()
	elif DIA == "create_new_file":
		print("""Specify an existing folder, followed by a file with the format.
For example: (PySestem:/User/pack/file.fomat)""")
		pute = input("PySestem:/User/")
		defer.create_new_file()
	else:
		print(f""""{DIA}" the command does not exist in the pysestem!""")
