drink = ["Coca Cola", "Orange Juice", "Coffe", "Milk Tea", "Yogurt"]
drinkPrice = [2,10,5,4,8]
malaysiaMoney = [100, 50, 20, 10, 5, 1]

print("Welcome to our vending machine!")
print("We have the following items available:")
for i in range(len(drink)):
    print([i+1], drink[i], "- MYR", drinkPrice[i])

inputDrink = int(input("Please select the drink you want: "))
if inputDrink > len(drink):
    print("Invalid selection")
    exit()

inputMoney = int(input("Please insert your money in MYR: "))
if inputMoney not in malaysiaMoney:
    print("Invalid money, we just accept 1, 5, 10, 20, 50, 100 MYR")
    exit()
    
if inputMoney < drinkPrice[inputDrink-1]:
    print("Not enough money")
else:
    print("Here is your", drink[inputDrink-1])
    change = inputMoney - drinkPrice[inputDrink-1]
    # print("Here is your change:", change, "MYR")
    
    # try better way to print change
    print("Here is your change:")
    for money in malaysiaMoney:
        count = change // money
        if count > 0:
            print(count, "MYR", money)
            change %= money
    
    print("Thank you for using our vending machine!")

