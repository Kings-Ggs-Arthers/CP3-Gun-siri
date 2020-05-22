usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "gun" and passwordInput == "asd":
    print("Done !")
    print(" ----- Amazing stones Shop -----")
    print("Stone Collection")
    print("1.Marble      100 USD")
    print("2.Obsidain    200 USD")
    print("3.limestone   50  USD")
    print("4.slate       180 USD")
    print("5.quartz      150 USD")
    types = int(input("Type of stone :"))
    marble = 100
    obsidain = 200
    limestone = 50
    slate = 180
    quartz = 150
    if types == 1:
        item1 = int(input("How many marble you want? :"))
        print("Total :", marble * item1, "USD")
    elif types == 2:
        item2 = int(input("Hpw many obsedian you want? :"))
        print("Total :", obsedian * item2, "USD")
    elif types == 3:
        item3 = int(input("How many limestone you want? :"))
        print("Total :", limestone * item3, "USD")
    elif types == 4:
        item4 = int(input("How many slate you want? :"))
        print("Total :", slate * item4, "USD")
    elif types == 5:
        item5 = int(input("How many quartz you want? :"))
        print("Total :", quartz * item5, "USD")
    else:
        print("Incorrect product code")
else:
    print("ERROR!!", "Please check you Username or Password")