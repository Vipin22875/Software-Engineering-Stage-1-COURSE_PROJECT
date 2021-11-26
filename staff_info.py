from os.path import exists
import os

"""
1. Enter details of Staff 
2. View Staff details 
3. Search for Staff 
4. Remove a Staff's entry 
5. Delete previos Staff data 
6. Exit

"""

details = ['ID','Name', 'Age', 'Gender','Date of Joining', 'Designation', 'Phone','Salary']

def open_file(filename,mode):
    if exists(filename):
        fp = open(filename,mode)
        return fp
    else:  
        print("File doesn't exist")
        error.update({'NoFile':"NotFound"})
        return None

def info(fp):
	for i in details:
		data = input("Enter "+ i + " :")

		fp.write(data + ",")
	fp.write("\n")
	return
	
	
def readFile (filename):
	if exists(filename):
		f = open(filename, "r")
		lines = f.readlines()
		for line in lines:
			print("\n")
			dataStaff = line.split(',')
			for i,l in enumerate(details):
				print("\t"+details[i]+" : ",dataStaff[i])
		print("------------------------------------------")
		f.close()
	else:
		print("\nNo entries are added until now\n")
		
def add_staff():
	choice = 1
	title = "\n\n\t------------------------------------------\n\t----------------- MENU -------------------  \n\t------------------------------------------\n"
	print(title)
	while (choice != 6):
		
		menu = "\n\n------------------------------------------\n1. Enter details of Staff \n2. View Staff details \n3. Search for Staff \n4. Remove a Staff's entry \n5. Update Staff data \n6. Delete previos Staff data \n7. Exit\n \nEnter choice here :"
		choice = int(input(menu))
		print("------------------------------------------")
		filename = "staff.txt"
		
		if choice ==1:
			add_info = 1
			while add_info == 1:

				print("\n\nEnter the Staff information:")
				if exists(filename):
					fp = open(filename, "a")
				else:
					fp = open(filename, "w")
				info(fp)
				

				x = input("\n\nDo you want to continue?(yes/no):")
				if(x.upper() == "YES" or x.upper() == "Y"):
					continue
				else:
					add_info = 0
					fp.close()
				
					
		if choice == 2:
			readFile(filename)  # function instead of following lines
			
		if choice == 3:
			found = 0
			name = input("Enter Staff name:")
			if exists(filename):
				f = open(filename, "r")
				lines = f.readlines()
				for line in lines:
					if (line.find(name) !=-1 or line.find(name.lower()) !=-1 or line.find(name.upper()) !=-1):
						print("Staff Record Found")
						dataStaff = line.split(',')
						for i,l in enumerate(details):
							print(details[i]+" : ",dataStaff[i])
						found = 1
						break
				if found == 0:
					print("Record not found for the Staff")
				print("------------------------------------------")
				f.close()
			else:
				print("\nNo entries are added until now\n")

		if choice == 4:
			if exists(filename):
				f = open(filename, "r")
				lines = f.readlines()
				name = input("Enter name of Staff:")
				Age = input("Enter Age of Staff:")
				f.close()
				f = open(filename, "w")
				for line in lines:
					if Age in line and name in line:
						pass
					else:
						f.write(line)
				f.close()
				print("\nStaff's entry removed successfully")
			else:
				print("\nNo entries are added until now\n")

		if choice == 6:
			os.remove(filename)
			
		if choice == 7:
			print("\n\tThank you")
			print("------------------------------------------")
			break
		if choice == 5:
			found = 0
			name = input("Enter Staff ID :")
			if exists(filename):
				f = open_file(filename, "r")
				lines = f.readlines()
				for j,line in enumerate(lines):
					data = line.split(',')
					if name == data[0] or name.upper() == data[0] or name.lower() == data[0]:
						print("Staff Record Found")
						dataStaff = line.split(',')
						for i,l in enumerate(details):
							print(details[i]+" : ",dataStaff[i])
						found = 1
						f.close()
						break
						# print("Do you want to change it ? (Y/N)")
				if found == 1:
					choice = input("Do you want to change it ? (Y/N)")
					if choice.upper() == 'Y':
						f = open(filename, "r")
						lines = f.readlines()
						f.close()
						fp = open_file(filename,'w')
						for i in range(len(lines)):
							if i == j:
								info(fp)
							else:
								fp.write(lines[i])
						fp.close()
					else:
						print("Thank you")
						break
				elif found == 0:
					print("Record not found for the Staff")
				print("------------------------------------------")
				f.close()
			else:
				print("\nNo entries are added until now\n")