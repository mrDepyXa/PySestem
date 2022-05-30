import os
import fnmatch
import shutil

os.chdir(r'PySestem:/User/')
NoRoot = 'PySestem:/User/'

def full_file():
        for file in os.listdir('.'):
        	if fnmatch.fnmatch(file, '*.py'):
        		print(file)

def open_file(pute):
	"""Откриваем файл"""
	OpenenFile = open(f"{NoRoot}")

def my_files(pute):
	"""Получаем все файли"""
	

def create_pack(pute):
	"""Создаем папку r"put"""
	os.makedirs(pute)

def delete_pack(pute):
	"""Удаления папки r"put"""
	shutil.rmtree(pute)

def create_new_file(pute):
	"""Создаем новий файл"""
	open(f"{NoRoot}{pute}", w)
	sleep(1)

def delete_file(pute):
	"""Удаляем файл"""
	os.remove(rf"{NoRoot}{pute}")
