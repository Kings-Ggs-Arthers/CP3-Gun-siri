menuList = []
def showBill():
    print("----- my Food -----")
    for number in range(len(menuList)):
        print(menuList[number])

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

print(menuList)
showBill()