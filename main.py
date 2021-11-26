from patient_info import *
from staff_info import *
from project import *
from staff import *
import sys

title = "\n\n\t------------------------------------------\n\t----------------- MENU -------------------  \n\t------------------------------------------\n"
print(title)
print(" 1. Add new patient details\n")
print(" 2. Add new staff details\n")
print(" 3. Check patient details\n")
print(" 4. Check staff details\n")
print(" 5. Exit\n")
choice = int(input("Enter: "))

if choice == 1:
    add_patient()
elif choice == 2:
    add_staff()
elif choice == 3:
    check_patient()
elif choice == 4:
    check_staff()
elif choice == 5:
    sys.exit(1)