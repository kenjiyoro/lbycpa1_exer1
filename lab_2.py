#Laboratory Activity 2
print("Verification of ID Number")
ID = input("Please input your ID Number: ")
ID1st = int(ID[0]) * int(8)
ID2nd = int(ID[1]) * int(7)
ID3rd = int(ID[2]) * int(6)
ID4th = int(ID[3]) * int(5)
ID5th = int(ID[4]) * int(4)
ID6th = int(ID[5]) * int(3)
ID7th = int(ID[6]) * int(2)
ID8th = int(ID[7]) * int(1)
IDComplete = int(ID1st)+int(ID2nd)+int(ID3rd)+int(ID4th)+int(ID5th)+int(ID6th)+int(ID7th)+int(ID8th)

if IDComplete % 11 ==0:
    IDType = IDComplete/11
    if IDType < 16:
        print("STUDENT")
    elif IDType >= 16:
        print("FACULTY")
else:
    print("INVALID")
    

    