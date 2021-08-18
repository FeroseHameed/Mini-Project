import csv

with open('company.csv', newline='') as file
	
	data = csv.reader(file)

	print("CSV file as a dictionary:\n")
	
	for row in data:
   		print(row)
