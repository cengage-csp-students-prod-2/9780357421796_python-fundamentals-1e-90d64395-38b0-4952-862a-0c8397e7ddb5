# Write your code here
import csv

# Read input from employees.csv and calculate pay
with open('employees.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    
    # Prepare to write to wages.csv
    with open('wages.csv', mode='w', newline='') as outfile:
        fieldnames = ['employee_name', 'hours_worked', 'pay_rate']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write header to output file
        writer.writeheader()
        
        # Process each row and calculate the pay rate
        for row in reader:
            # Use 'employee_name' instead of 'name'
            employee_name = row['employee_name']
            hours_worked = int(row['hours_worked'])  # Convert to integer for calculation
            pay_rate = hours_worked * 15  # Calculate pay
            
            # Write the data to wages.csv
            writer.writerow({'employee_name': employee_name, 'hours_worked': hours_worked, 'pay_rate': pay_rate})

print("wages.csv has been generated successfully.")