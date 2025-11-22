import csv

filename = "Expence"

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    Category = input("Category: ")
    amount = float(input("amount: "))

    with open("Expence.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, Category, amount])
    print("Expence added")

def show_expence():
    try:
        with open("Expence.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expence recorded yet")

while True:
    print("Expence_Tracker")
    print("1. Add expence \n2. Show expence \n3. Exit")

    ch = input("Enter choise(1-3): ")

    if ch == '1':
        add_expense()
    
    elif ch == '2':
        show_expence()
    elif ch == '3':
        print("Exiting")
        break
    else:
        print("invalid choise!!!")