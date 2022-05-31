import os
import fnmatch
import shutil
import requests
import html2text
from Data import *

NoRoot = 'PySestem/User/'

def full_file():
        for file in os.listdir('.'):
        	if fnmatch.fnmatch(file, '*.py'):
        		print(file)


def open_file(pute):
	ryel = os.path.exists(f"{NoRoot}{pute}")
	if ryel == True:
		OpenenFile = open(f"{NoRoot}{pute}", 'r')
		textfile = OpenenFile.read()
		print(textfile)
		exit = input(f"{NoRoot}{pute} >? Close file? [y/n]: ")
		if exit == "y":
			OpenenFile.close()
			print(f"{NoRoot}{pute} >!  File close!")
		elif exit == "n":
			print("okey...")
		else:
			print("pySestem, blat what?! >> Cancel to start.")
	else:
		print(f"{NoRoot}{pute} >! does not exist.")
		print("pySestem >> Cancel to start.")


def my_files(pute):
	"""Получаем все файли"""


def create_pap(pute):
	os.makedirs(pute)
	print(f"{NoRoot}{pute} >! Folder created")


def delete_pap(pute):
	reale = input("Are you sure you want to delete the folder? [y/n]: ")
	if reale == "y":
		shutil.rmtree(pute)
		print(f"{NoRoot}{pute} >! Pep deleted")
	elif reale == "n":
		print("pySestem >> Cancel to start.")
	else:
		print("pySestem, blat what?! >> Cancel to start.")


def create_new_file(pute):
	files = open(f"{NoRoot}{pute}", "w")
	print(f"{NoRoot}{pute} >! File created")
	testfile = input(f"{NoRoot}{pute} >... Edit text file\n")
	files.write(f"""{testfile}""")
	files.close()
	print(f"{NoRoot}{pute} >! Save file")


def delete_file(pute):
	ryel = os.path.exists(f"{NoRoot}{pute}")
	if ryel == True:
		reale = input("Are you sure you want to delete the file? [y/n]: ")
		if reale == "y":
			os.remove(rf"{NoRoot}{pute}")
			print(f"{NoRoot}{pute} >! File deleted.")
		elif reale == "n":
			print("pySestem >> Cancel to start.")
		else:
			print("pySestem, blat what?! >> Cancel to start.")
	else:
		print(f"{NoRoot}{pute} >! does not exist.")
		print("pySestem >> Cancel to start.")


def open_internet(adrisat):
	s = requests.get(f"http://{adrisat}/")
	d = html2text.HTML2Text()
	d.ignore_links = True
	c = d.handle(s.text)
	print(c)


def download_file(adrisat):
	site = f"http://{adrisat}/"
	(dirname, filename) = os.path.split(site)
	r = requests.get(s, stream=True)
	if r.status_code == 200:
	       with open(f"{NoRoot}Download/filename", 'wb') as f:
	       	r.raw.decode_content = True
	       	shutil.copyfileobj(r.raw, f)

def gmail_send(Meta):
	if Meta == "seput":
		pass
	else:
		pass

def gmail_date(editGmail, editPass, editSignature):
	if myGmail == "None":
		realSignature = f"{editmySignature}\nSent with pysestem."
		SeputData = open(f"Data.py", 'w')
		SeputData.write(f"""User = "{User}"
myGmail = "{editGmail}"
myPass = "{editPass}"
mySignature = "{realSignature}" """)
		SeputData.close()
		print("Data.py >! Save your data")
	else:
		reale = input("You already have data entered, do you want to change it? [y/n]: ")
		if reale == "y":
			realSignature = f"{editmySignature}\nSent with pysestem."
			SeputData = open(f"Data.py", 'w')
			SeputData.write(f"""User = "{User}"
myGmail = "{editGmail}""
myPass = "{editPass}""
mySignature = "{realSignature}" """)
			SeputData.close()
			print("Data.py >! Save your data")
		elif reale == "n":
			print("pySestem >> Cancel to start.")
		else:
			print("pySestem, blat what?! >> Cancel to start.")

def new_name_user():
	user_name = input("Enter your name or login: ")
	Gabt = f"{user_name}-PyS"
	SeputData = open(f"Data.py", 'w')
	SeputData.write(f"""User = "{Gabt}"
myGmail = "{myGmail}"
myPass = "{myPass}"
mySignature = "{mySignature}" """)
	SeputData.close()
