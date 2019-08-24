#user
print("1. Send money")
print("2. Withdraw Money")
phone_number = "0704487563"
user = input("Select Choice:\n")
if(user == "1"):
    print("Send Money")
    print("1. MTN User")
    print("2. Airtel User")
    x = input("Choice:\n")
    if(x =="1"):
        print("MTN User:")
        number = input("Enter Mobile Number\n")
        if(number == phone_number):
            amount = input("Enter Amount to send\n")
            print(amount," sent successfully to number",phone_number)
        else:
            print("Wrong phone number or input details")
            exit()
    elif(x == "2"):
        print("Airtel User:")
        number = input("Enter Mobile Number\n")
        if(number == phone_number):
            amount = input("Enter Amount to send\n")
            print(amount," sent successfully to number",phone_number)
        else:
            print("Wrong phone number or input details")
            exit()
    
elif(user == "2"):
    print("Withdraw Money")
    number = input("Enter phone number:\n")
    if(number == phone_number):
        am = 20000
        amount = input("Enter amount to withdraw\n")
        balance = (float(am) - float(amount))
        if(float(amount) > float(am)):
            print("Insaficialte fund, deposit and try again")
            exit()
        else:
            print("You have withdrawn",amount,",by",phone_number,". Thank you!")
    else:
        print("Wrong phone number or input details")
else:
    print("Invalid input")
