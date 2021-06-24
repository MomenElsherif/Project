def Blood_Donation_System():
        c = "y"
        while c == "y":
            print("1- Add new Donar")
            print("2- View all Donars")
            print("3- Search a Donar")
            print("4- Delete Donar")
            print("5- Edit Donar")
            c = input("Enter the number of operation :")
            if c == "1":
                WriteDonar()
            elif c == "2":
                ReadDonar()
            elif c == "3":
                SearchDonar()
            elif c == "4":
                DeleteDonar()
            elif c == "5":
                UpdateDonar()
            c = input("Do you want another Operation (y/n)? ") 
            
def WriteDonar():
    with open("Donar.txt","a") as file :
        c = "y"
        while c == "y":
            ID = input("Enter Donar ID: ");
            Name = input("Enter Donar Name: ");
            Blood_Group= input("Enter Donar Blood Group: ");
            Medical_report = input("Enter Donar Medical Report: ");
            Address = input("Enter Donar Address: ");
            Contact_Number = input("Enter Donar Number: ");
            file.write(ID+"\t"+Name+"\t"+Blood_Group+"\t\t"+Medical_report+"\t\t"+Address+"\t"+Contact_Number+"\n")
            c = input("Do you want to add another record (y/n)? ")
            
def ReadDonar():
    with open("Donar.txt","r") as file :
        print("ID\tName\tBlood Group\tMedical report\tAddress\tContact Number")
        for line in file:
            print(line,end="")

def SearchDonar():
    ID = input("Enter Donar ID: ")
    with open("Donar.txt","r") as file :
        flag = False
        for line in file:
            fields = line.split('\t')
            if ID == fields[0] :
                flag = True
                print("ID : ", fields[0])
                print("Name: ", fields[1])
                print("Blood Group: ", fields[2])
                print("Medical report: ", fields[3])
                print("Address: ", fields[4])
                print("Contact Number: ", fields[5])
        if not flag :
            print("No Records Found")

def DeleteDonar():
    import os
    ID = input("Enter Donar ID: ")
    TempFile = open("TempFile.txt","w")
    flag = False
    with open("Donar.txt","r") as file :
        for line in file:
            fields = line.split()
            if ID == fields[0] and flag == False :
                flag = True
            else :
                TempFile.write(line)
                
        TempFile.close()
    os.remove("Donar.txt")
    os.rename("TempFile.txt", "Donar.txt")
     
    if not flag :
        print("No Records Found")
    else :
        print("Donar are deleted successfully")
                  
def UpdateDonar():
        import os
        ID = input("Enter Donar ID: ")
        with open("Donar.txt","r") as file :
                TempFile = open("TempFile.txt","w")
                flag = False
                for line in file :
                        fields = line.split("\t")
                        if ID == fields[0] :
                                flag = True
                                ID = input("Enter Donar ID: ");
                                Name = input("Enter Donar Name: ");
                                Blood_Group= input("Enter Donar Blood Group: ");
                                Medical_report = input("Enter Donar Medical Report: ");
                                Address = input("Enter Donar Address: ");
                                Contact_Number = input("Enter Donar Number: ");
                                line = ID+"\t"+Name+"\t"+Blood_Group+"\t"+Medical_report+"\t"+Address+"\t"+Contact_Number+"\n"
                        TempFile.write(line)
                if not flag :
                        print("No Record matches")
                else :
                        print("Record has updated")
                TempFile.close()
        os.remove("Donar.txt")
        os.rename("TempFile.txt", "Donar.txt")

Blood_Donation_System()
