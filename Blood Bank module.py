def Blood_Donation_System():
        c = "y"
        while c == "y":
            print("1- Add new Blood Bank")
            print("2- View all Blood Banks")
            print("3- Search a Blood Bank")
            print("4- Delete Blood Bank")
            print("5- Edit Blood Bank")
            c = input("Enter the number of operation :")
            if c == "1":
                WriteBlood_Bank()
            elif c == "2":
                ReadBlood_Bank()
            elif c == "3":
                SearchBlood_Bank()
            elif c == "4":
                DeleteBlood_Bank()
            elif c == "5":
                UpdateBlood_Bank()
            c = input("Do you want another Operation (y/n)? ") 
            
def WriteBlood_Bank():
    with open("Blood Bank.txt","a") as file :
        c = "y"
        while c == "y":
            Blood_Bank_Name = input("Enter Blood Bank Name: ");
            Donars_Name = input("Enter Donar Name: ");
            Contant_Number = input("Enter Contact Number: ");
            Blood_Bank_Address = input("Enter Blood Bank Address: ");
            file.write(Blood_Bank_Name+"\t"+Donars_Name+"\t\t"+Contant_Number+"\t"+Blood_Bank_Address+"\n")
            c = input("Do you want to add another record (y/n)? ")
            
def ReadBlood_Bank():
    with open("Blood Bank.txt","r") as file :
        print("Name\tDonar Name\tContact Number\tAddress")
        for line in file:
            print(line,end="")

def SearchBlood_Bank():
    Blood_Bank_Name = input("Enter Blood Bank Name: ")
    with open("Blood Bank.txt","r") as file :
        flag = False
        for line in file:
            fields = line.split('\t')
            if Blood_Bank_Name == fields[0] :
                flag = True
                print("Blood Bank Name: ", fields[0])
                print("Enter Donar Name: ", fields[1])
                print("Enter Contact Number: ", fields[2])
                print("Blood Bank Address: ", fields[3])
        if not flag :
            print("No Records Found")

def DeleteBlood_Bank():
    import os
    Blood_Bank_Name = input("Enter Blood Bank Name: ")
    TempFile = open("TempFile.txt","w")
    flag = False
    with open("Blood Bank.txt","r") as file :
        for line in file:
            fields = line.split("\t")
            if Blood_Bank_Name == fields[0] and flag == False :
                flag = True
            else :
                TempFile.write(line)
                
        TempFile.close()
    os.remove("Blood Bank.txt")
    os.rename("TempFile.txt", "Blood Bank.txt")
     
    if not flag :
        print("No Records Found")
    else :
        print("Blood Bank are deleted successfully")
                  
def UpdateBlood_Bank():
        import os
        Blood_Bank_Name = input("Enter Blood Bank Name: ")
        with open("Blood Bank.txt","r") as file :
                TempFile = open("TempFile.txt","w")
                flag = False
                for line in file :
                        fields = line.split("\t")
                        if Blood_Bank_Name == fields[0] :
                                flag = True
                                Blood_Bank_Name = input("Enter Blood Bank Name: ");
                                Donars_Name = input("Enter Donar Name: ");
                                Contant_Number = input("Enter Contact Number: ");
                                Blood_Bank_Address = input("Enter Blood Bank Address: ");
                                line = Blood_Bank_Name+"\t"+Donars_Name+"\t"+Contant_Number+"\t"+Blood_Bank_Address+"\n"
                        TempFile.write(line)
                if not flag :
                        print("No Record matches")
                else :
                        print("Record has updated")
                TempFile.close()
        os.remove("Blood Bank.txt")
        os.rename("TempFile.txt", "Blood Bank.txt")

Blood_Donation_System()
