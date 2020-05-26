def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "gun" and passwordInput == "siri":
        return True
    else:
        return False
def showMenu():
    print(" ----- A shop ----- ")
    print("Select Menu")
    print("1.Vat calculate")
    print("2.Price calculate")
def selectMenu():
    userSelect = int(input("Menu :"))
    if userSelect == 1:
        price = int(input("price :"))
        vatCalculate(price)
    elif userSelect == 2:
        priceCalculate()
def vatCalculate(Prices):
    vat = 7
    result = Prices + (Prices * vat / 100)
    return print(result)
def priceCalculate():
    price1 = int(input("1st Price :"))
    price2 = int(input("2nd Price :"))
    return print(vatCalculate(price1 + price2))

if login() == True :
    showMenu()
    selectMenu()
else:
    print("Invalid Username or Password")