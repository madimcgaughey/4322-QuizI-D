'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
employee_file = open('employee_data.csv', 'r')

#create an empty dictionary
employee_dict = {}
list1 = employee_dict['employee']


#use a loop to iterate through the csv file

        #employee_dict['Name'] = firstname, lastname
        #employee_dict['Salary'] = newsalary
        #print(employee_dict)


for employee in employee_file:
  fn = employee['First Name']
  ln = employee['Last Name']
  salary = employee['Salary']
  newsalary = salary*(salary*.1)
  if newsalary != 0:
    employee_dict['Name'] = fn, ln
    employee_dict['New Salary'] = newsalary
    print(employee_dict)



  
    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    
