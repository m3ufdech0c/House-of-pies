
# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0]

# Pie list
pie_menu = ["pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale","Steak"]

# Display initial message
print("Welcome to the house of Pies! Here are our pies:")

# While we are still shopping...
while shopping == 'y':
    # Show pie selection prompt
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("(1) pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak)")

    pie_choice = input("Which would you like?")

    # Add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases[int(pie_choice)-1] = pie_purchases[int(pie_choice)-1] + 1

    print("------------------------------------------------------------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_menu[int(pie_choice) - 1] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)0? ")

# Once the pie list is complete
print("----------------------------------------------------------------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_menu)):

    # Gather the count of each pie in the pie list and print them alongside the pies
    print(str(pie_purchases[pie_index]) + " " + str(pie_menu[pie_index]))