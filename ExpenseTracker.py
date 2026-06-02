#Expense tarcker code
expensesList = []#list of all expenses
print("Welcome to Expense tracker!")
while True:
    print("======MENU======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    choice = int(input("Please enter your choice (1-4): "))
    #choice 1
    if(choice == 1 ):
        Date = input("Enter the date of the expense (YYYY-MM-DD): ")
        Category = input("Enter the category of the expense (e.g., Food, Transport, etc.): ")
        Description = input("Enter a description for the expense: ")
        Amount = float(input("Enter the amount of the expense: "))
        
        expense ={
            "Date" : Date,
            "Category": Category,
            "Description" : Description,
            "Amount" : Amount
        }
        expensesList.append(expense)
        print("Expense added successfully!")
    #choice two
    elif(choice == 2):
        if(len (expensesList) == 0):
            print("No expenses to show.")
        else:
            print("Your Expenses:")
            count = 1
            for eachExpense in expensesList:
                print(f"Expense Number: {count} -> {eachExpense['Date']},{eachExpense['Category']},{eachExpense['Description']},{eachExpense['Amount']}")
                count += 1
    #expense total
    elif(choice == 3):
       total = 0
       for eachExpense in expensesList:
        total = total + eachExpense["Amount"]
        print(f"\n Total Expenses: {total}")

    #exit garna
    elif(choice == 4):
        print("Thankyou tatabyebye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
    
