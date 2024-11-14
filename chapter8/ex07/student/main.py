# Write your code here
import csv

with open('employees.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    
    with open('wages.csv', mode='w', newline='') as outfile:
        fieldnames = ['employee_name', 'pay_rate']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            employee_name = row['employee_name']
            hours_worked = int(row['hours_worked'])
            pay_rate = hours_worked * 15
            
            writer.writerow({'employee_name': employee_name, 'pay_rate': pay_rate})

print("wages.csv has been generated successfully.")
