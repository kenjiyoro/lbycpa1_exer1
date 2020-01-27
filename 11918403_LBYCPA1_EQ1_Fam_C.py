#Familiarization Exercise C
def start():
    while True:
        print("*****Welcome to our automated milk tea ordering system*****")
        print(" ")
        print("For today's milk tea, we offer: ")
        print(" ")

        print("[1] Original Milk Tea ")
        print("[2] Pearl Milk Tea ")
        print("[3] for Coffee Milk Tea ")
        print("[Q] to quit")

        choice = input(" Select your Milk Tea of Choice: ")

        if choice == '1':
            print(" Original Milk Tea costs 60 pesos")
        elif choice == '2':
            print(" Pearl Milk Tea costs 65 pesos ")
        elif choice == '3':
            print(" Coffe Milk Tea costs 70 pesos ")
        elif choice =='Q':
            print("Exit.")
        else:
            input("Sorry, please choose from 1,2,3, or Q")
start ()