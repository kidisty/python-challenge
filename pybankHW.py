# Import modules
import os
import csv

#Create a path for the CSV file
PyBank = os.path.join('..', 'Resources', 'budget_data.csv')
#Read the CSV file
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
	##Read the header
    header = next(csvreader)

    #Create a list to store value
    Months= []
    Profit = []
    Changes = []


    #Loop through each row after the header
    for row in csvreader:
        Months.append(row[0])
        Profit.append(int(row[1]))
    for x in range(len(Profit)-1):
        Changes.append(Profit[x+1]-Profit[x])

#The greatest increase and decrease in profits (date and amount) over the entire period
Greatest_increase = max(Changes)
Greatest_decrease = min(Changes)
Month_increase = Changes.index(max(Changes))+1
Month_decrease = Changes.index(min(Changes))+1

#Print out the results in terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(Months)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(Changes)/len(Changes),2)}")
print(f"Greatest Increase in Profits: {Months[Month_increase]} (${(str(Greatest_increase))})")
print(f"Greatest Decrease in Profits: {Months[Month_decrease]} (${(str(Greatest_decrease))})")

#Export file
with open("Analysis_bank.txt", "w") as text:
	text.write("Financial Analysis"+"\n")
	text.write("------------------------\n")
	text.write(f"Total Months:{len(Months)}"+"\n")
	text.write(f"Total: ${sum(Profit)}"+"\n")
	text.write(f"Average Change: {round(sum(Changes)/len(Changes),2)}"+"\n")
	text.write(f"Greatest Increase in Profits:{Months[Month_increase]} (${(str(Greatest_increase))})"+"\n")
	text.write(f"Greatest Decrease in Profits:{Months[Month_decrease]} (${(str(Greatest_decrease))})"+"\n")
