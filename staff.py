from os.path import exists
import os
from colorama import *
import colorama
import datetime
from datetime import date
from datetime import datetime
import sys


details = ['ID','Name', 'Age', 'Gender','Date of Joining', 'Designation', 'Phone','Salary']
detailsType = ['num','str','num','str','date','str','num','num']
validLength = { "Phone":10,"Salary":[999,9999999]}



def info(fp):
	for i in details:
		data = input("Enter "+ i + " :")
		fp.write(data + ",")
	fp.write("\n")
	return

def open_file(filename,mode):
    if exists(filename):
        fp = open(filename,mode)
        return fp
    else:  
        print("File doesn't exist")
        error.update({'NoFile':"NotFound"})
        return None


def check_salary(salary):
	if int(salary) > validLength['Salary'][0] and int(salary) < validLength['Salary'][1]:
		return True
	else:
		return False

def validate(date_string):
    format = "%Y/%m/%d"
    try:
        res = bool(datetime.strptime(date_string, format))
    except ValueError:
        res = False
    return res

def show_error(filename):
	error = []
	fp = open_file(filename,'r')

	lines = fp.readlines()
	# print(lines)
	#print(lines)
	count = 0
	for line in lines:
		#print(line)
		error_value = []
		dataStaff = line.split(',')
		for i,l in enumerate(details):
			if detailsType[i] == 'num':
				dataStaff[i] = dataStaff[i].strip('\n')
				if dataStaff[i].isnumeric():
					if l == 'Phone':
						if len(dataStaff[i]) != validLength[l]:
							error_value.append(i)

					if l == 'Salary':
						if check_salary(dataStaff[i]):
							pass
						else:
							error_value.append(i)
				else:
					error_value.append(i)
				
			if detailsType[i] == 'str':
				if dataStaff[i].isalpha():
					if l == 'Gender':
						if dataStaff[i] == "M" or dataStaff[i] == "F":
							pass
						else:
							error_value.append(i)
					if l == 'Designation':
						if dataStaff[i] == "D" or dataStaff[i] == "N":
							pass
						else:
							error_value.append(i)
				else:
					error_value.append(i)

			if l == 'Date of Joining':
				if detailsType[i] == 'date':
					if validate(dataStaff[i]):
						pass
					else:
						error_value.append(i)
				else:
					error_value.append(i)
		error.append(error_value)
	for i in range(len(error)):
		if len(error[i]) == 0:
			print("Entry ",i+1," : ",end = "")
			print("\033[0;32m",end = "")
			print(colorama.Back.WHITE + "All clear"+Style.RESET_ALL)
			print('\n')
		else:
			print("Entry ",i+1," : ",end = "")
			print("\033[0;31m",end = "")
			print(colorama.Back.WHITE + "Not clear"+Style.RESET_ALL)
			print("Has ",len(error[i])," errors\n")
	return error

def check(error,filename):
	for i in range(len(error)):
		print("For ",i+1, " Entry")
		ok = 1
		for j in range(len(details)):
			if j in error[i]:
				print("\033[0;31m")
				print("Failed : PLEASE CHECK THE " +details[j].upper())
				ok = 0
			else:
				print("\033[0;32m")
				print("Passed : OK")
		if ok:
			print("\033[0;32m")
			print(colorama.Back.WHITE + "All clear"+Style.RESET_ALL)
		else:
			print("\033[0;31m")
			print(colorama.Back.WHITE + "Not clear"+Style.RESET_ALL)
		print("*******************")


def update_error(error,filename):
	fp = open_file(filename,'r')
	lines = fp.readlines()
	fp.close()
	fp = open_file(filename,'w')
	for i,line in enumerate(lines):
		if len(error[i]) == 0:
			fp.write(line)
		else:
			print("For entry ",i+1)
			lineList = line.split(',')
			for k in error[i]:
				strg = "Enter valid " + details[k] + ":"
				value = input(strg)
				lineList[k] = value
			changedLine = ','.join(lineList)
			changedLine = changedLine
			fp.write(changedLine)
	fp.close()

def check_staff():
	filename = 'staff.txt'
	while True:
		print(Style.RESET_ALL)
		title = "\n\n\t------------------------------------------\n\t----------------- MENU -------------------  \n\t------------------------------------------\n"
		print(title)
		print(" 1. Overview of all errors")
		print(" 2. Check for error line by line")
		print(" 3. Correct errors")
		print(" 4. Exit")
		choice = int(input("Enter: "))
		if choice == 1:
			error_list = show_error(filename)
		elif choice == 2:
			try:
				check(error_list,filename)
			except:
				print("Generate all error first")
		elif choice == 3:
			try:
				update_error(error_list,filename)
			except:
				print("Generate all error first")
		elif choice == 4:
			sys.exit(1)		

		else:
			print("Exit")
			break