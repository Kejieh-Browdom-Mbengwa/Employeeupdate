""""This is a project that updates all emails in a list employees database in excel and as .csv with 30 entries and each
 has different employee names, same email address and different phone numbers.
"""

import csv
import pandas as pd
#this line "import pandas" permits the script to read files comming from the "openpyxl"
# library which is a library that permits the usage and
# manipulation of xlsx and csv files

# def fetch_csv():
#     employee_details = pd.read_csv('input\employeedata.csv', encoding="unicode_escape")
#     return employee_details
#

userDetails = pd.read_csv('input/employeedata.csv', encoding="unicode_escape")
#This helps to read data from the file
oldEmail = userDetails['Email'].tolist()
new_emails = []
for email in oldEmail:
    new_emails.append(email.replace("@helpinghands.cm", "@handsinhands.org"))
print(new_emails)
#the for condition comes in cause while going through the sheet, if the script finds the 'helpinghands.cm' in
#any of the cells, it will update it and replace it by 'handsinhands.org'

names = userDetails['Name'].tolist()
phone = userDetails['Phone'].tolist()

header = ['Name', 'Email', 'Phone']
my_dict = {"Name": names, "Email": new_emails, "Phone": phone}
with open('output/updatedemployeedata.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(my_dict.keys())
    writer.writerows(zip(*my_dict.values()))
#Finally after updating and replacing it the script creates a new excel sheet and saves it using the
#workbook class and save attribute
