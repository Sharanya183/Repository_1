#LOGICAL OPERATORS#
#If applicant has high income AND good credit, he/she is eligible for loan. Write the code for this statement.#

income = input(bool("High Income(True/False): "))
credit = input(bool("Good Credit(True/False)"))
if income and credit == True:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

#If applicant has high income OR good credit, he/she is eligible for loan. Write the code for this statement.#

income = input(bool("High Income(True/False): "))
credit = input(bool("Good Credit(True/False)"))
if income or credit == True:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")

#If applicant has good income and credit, no criminal record, eligible for a loan. Write the code for this statement.#

income = input(bool("High Income(True/False): "))
credit = input(bool("Good Credit(True/False)"))
criminal_record = input(bool("Criminal Records(True/False): "))
if income and credit == True and criminal_record == False:
    print("Eligible for loan")
    

