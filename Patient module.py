def Blood_Donation_System():
        c = "y"
        while c == "y":
            print("1- Add new patient")
            print("2- View all patients")
            print("3- Search a patient")
            print("4- Delete patient")
            print("5- Edit patient")
            c = input("Enter the number of operation :")
            if c == "1":
                WritePatient()
            elif c == "2":
                ReadPatient()
            elif c == "3":
                SearchPatient()
            elif c == "4":
                DeletePatient()
            elif c == "5":
                UpdatePatient()
            c = input("Do you want another Operation (y/n)? ") 
            
def WritePatient():
    with open("patient.txt","a") as file :
        c = "y"
        while c == "y":
            Patient_ID = input("Enter Patient ID: ");
            Patient_Name = input("Enter Patient Name: ");
            Patient_Blood_Group = input("Enter Patient Blood Group: ");
            Patient_Disease = input("Enter Patient Disease: ");
            file.write(Patient_ID+"\t"+Patient_Name+"\t"+Patient_Blood_Group+"\t\t"+Patient_Disease+"\n")
            c = input("Do you want to add another record (y/n)? ")
            
def ReadPatient():
    with open("patient.txt","r") as file :
        print("ID\tName\tBlood Group\tDisease")
        for line in file:
            print(line,end=(""))

def SearchPatient():
    Patient_ID = input("Enter Patient ID: ")
    with open("patient.txt","r") as file :
        flag = False
        for line in file:
            fields = line.split('\t')
            if Patient_ID == fields[0] :
                flag = True
                print("Patient ID: ", fields[0])
                print("Patient Name: ", fields[1])
                print("Patient Blood Group: ", fields[2])
                print("Patient Disease: ", fields[3])
        if not flag :
            print("No Records Found")

def DeletePatient():
    import os
    Patient_ID = input("Enter Patient ID: ")
    TempFile = open("TempFile.txt","w")
    flag = False
    with open("patient.txt","r") as file :
        for line in file:
            fields = line.split()
            if Patient_ID == fields[0] and flag == False :
                flag = True
            else :
                TempFile.write(line)
                
        TempFile.close()
    os.remove("patient.txt")
    os.rename("TempFile.txt", "patient.txt")
     
    if not flag :
        print("No Records Found")
    else :
        print("patient are deleted successfully")
                  
def UpdatePatient():
        import os
        Patient_ID = input("Enter Patient ID: ")
        with open("patient.txt","r") as file :
                TempFile = open("TempFile.txt","w")
                flag = False
                for line in file :
                        fields = line.split("\t")
                        if Patient_ID == fields[0] :
                                flag = True
                                Patient_ID = input("Enter Patient ID: ");
                                Patient_Name = input("Enter Patient Name: ")
                                Patient_Blood_Group = input("Enter Patient Blood Group: ")
                                Patient_Disease = input("Enter Patient Disease: ")
                                line = Patient_Name+"\t"+Patient_Blood_Group+"\t"+Patient_Disease+"\n"
                        TempFile.write(line)
                if not flag :
                        print("No Record matches")
                else :
                        print("Record has updated")
                TempFile.close()
        os.remove("patient.txt")
        os.rename("TempFile.txt", "patient.txt")

Blood_Donation_System()
