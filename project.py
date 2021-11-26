from os.path import exists
import os
from colorama import *
import colorama
import sys

details = ['Name', 'Age', 'Gender','Phone', 'Bloodgroup', 'Diabetic','BloodPressure','Vaccine','VaccineName']
detailsType = ['str','num','str','num','str','str','num','num','str']
validLength = { "Phone":10,"Vaccine":1,"BloodPressure":[50,170]}

def open_file(filename,mode):
    if exists(filename):
        fp = open(filename,mode)
        return fp
    else:  
        print("File doesn't exist")
        return None

def check_bp(bp):
	if int(bp) > validLength['BloodPressure'][0] and int(bp) < validLength['BloodPressure'][1]:
		return True
	else:
		return False

def show_error(filename):
	error = []
	fp = open_file(filename,'r')

	lines = fp.readlines()
	count = 0
	for line in lines:
		error_value = []
		dataStudent = line.split(',')
		for i,l in enumerate(details):
			if detailsType[i] == 'num':
				dataStudent[i] = dataStudent[i].strip('\n')
				if dataStudent[i].isnumeric():
					if l == 'Phone' or l == 'Vaccine':
						if len(dataStudent[i]) != validLength[l]:
							error_value.append(i)
					if l == 'Vaccine' and dataStudent[i] == '0':
						if dataStudent[i+1] != "NA":
							error_value.append(i)
					if l == "BloodPressure":
						dataStudent[i] = dataStudent[i].strip('\n')
						if check_bp(dataStudent[i]):
							pass
						else:
							error_value.append(i)
				else:
					error_value.append(i)
			if detailsType[i] == 'str':
				if dataStudent[i].isalpha():
					
					if l == 'Gender':
						if dataStudent[i] == 'M' or dataStudent[i] == 'F':
							pass
						else:
							error_value.append(i)
					if l == 'Diabetic':
						if dataStudent[i] == 'Y' or dataStudent[i] == 'N':
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

def check_patient(): 
	filename = 'patient.txt'
	while True:
		print(Style.RESET_ALL)
		title = "\n\n\t------------------------------------------\n\t----------------- MENU -------------------  \n\t------------------------------------------\n"
		print(title)
		print(" 1. Overview of all errors")
		print(" 2. Check for error line by line")
		print(" 3. Correct errors")
		print(" 4. Exit")
		choice = int(input("Enter choice : "))
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