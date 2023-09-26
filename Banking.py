#Bank Operation using Oops
from Validations import *
class bank_account:
    #Create Account
    def _init_(self,b_name,b_ifsc,b_accnum,b_acchname,b_age,b_gender,b_dob,b_addr,b_city,b_type,b_bal,b_pan,b_aadhar):
        self.b_name=b_name
        self.b_ifsc=b_ifsc
        self.b_accnum=b_accnum
        self.b_acchname=b_acchname
        self.b_age=b_age
        self.b_gender=b_gender
        self.b_dob=b_dob
        self.b_addr=b_addr
        self.b_city=b_city
        self.b_type=b_type
        self.b_bal=b_bal
        self.b_pan=b_pan
        self.b_aadhar=b_aadhar

    def display_acc(self):
        print("NAME : ",self.b_name)
        print("IFSC CODE : ",self.b_ifsc)
        print("ACCOUNT NUMBER : ",self.b_accnum)
        print("AGE : ",self.b_age)
        print("GENDER : ",self.b_gender)
        print("DOB : ",self.b_dob)
        print("ADDRESS : ",self.b_addr)
        print("CITY : ",self.b_city)
        print("TYPE : ",self.b_type)
        print("BALANCE : ",self.b_bal)
        print("PAN NUMBER ",self.b_pan)
        print("AADHAR : ",self.b_aadhar)


accounts=[]
print("_______________________________________________________\n")
print("  <<<<<<<<<<< Banking Operating System >>>>>>>>>>>>>> \n ")
print("_________________________________________________________")
print("")

while True:
    print('1. Creating Account ')
    print('2. Delete Account ')
    print('3. Update Acount ')
    print('4. Deposit ')
    print('5. WithDraw')
    print('6. Funds Transfer')
    print('7. Search details of account holder')
    print('8. Balance Enquiry')
    print('9. Exit')
    print('10. display')
    print("--------------------------------------------------------- ")
    

    ch=int(input('Enter your Choice : '))
    print("---------------------------------------------------------\n")
    

    if ch==1:#Creating Account
        num=int(input('Enter number of Accounts you want to ADD : '))

        for n in range(num):
            while True:   

                b_name=input('Enter Bank Name : ')
                if isNameValid(b_name):
                    break
                else:
                    print("Invalid Name")


                b_ifsc=input('Enter IFSC Code : ')
                if (isIFSCValid(b_ifsc)):
                    break
                else:
                    print("Invalid IFSC Code")

                b_accnum=input('Enter Account Number : ')
                b_acchname=input('Enter Acount Holder Name : ')
                if isNameValid(b_acchname):
                    break
                else:
                    print("Invalid Name")
                b_age=input('Enter Age of Acount Holder : ')

                b_gender=input('Enter your Gender : ')
                if isGenderValid(b_gender):
                    break
                else:
                    print("Invalid input")

                b_dob=input('Enter your DOB : ')
                if isDOBValid(b_dob):
                    break
                else:
                    print("Invalid DOB")
                    
                b_addr=input('Enter your Address : ')
                b_city=input('Enter City : ')
                b_type=input('Enter Type of Account : ')
                b_bal=input('Enter Balance : ')

                b_pan=input('Enter your Pan Card number : ')
                if isPanValid(b_pan):
                    break
                else:
                    print("Invalid PAN no.")

                b_aadhar=input('Enter Aadhar Card number : ')
                if isAadharValid(b_aadhar):
                    break
                else:
                    print("Invalid Aadhar No.")

                ob=bank_account(b_name,b_ifsc,b_accnum,b_acchname,b_age,b_gender,b_dob,b_addr,b_city,b_type,b_bal,b_pan,b_aadhar)
                accounts.append(ob)     

    elif ch==2:#Delete Account
        accnum=int(input("Enter account number you want to delete : "))
        flag=False
        for i in accounts:
            if i.b_accnum == accnum:
               accounts.remove(i)
               print("Account deleted successfully.")
               flag=True
               break
        if not flag:
            print("Account number not found")
        
    elif ch==3:
        #Update Acount
        account_number= input("Enter Account Number : ")
        for i in accounts:
            if i.b_accnum == account_number:
                print("Options to Update : ")
                print("1. Update name ")
                print("2. Update address")
                print("3. Update DOB")
                 
                select=input("Enter your option : ")
                 
                if select=='1':
                    nm = input("Enter new Name : ")
                    i.b_acchname = nm
                    print("Updated new Name")
                elif select =='2':
                    addr=input("Enter new Address : ")
                    i.b_addr = addr
                    print("Updated new Name")
                elif select =='3':
                    dob=input("Enter new DOB : ")
                    i.b_dob = dob 
                    print("Updated new DOB")
                    
                else:
                    print("Invalid Entry")
                
                
        
    
    elif ch==4:#Deposit
        account_number = input("Enter Account Number : ")
        amount = float(input("Enter deposit amount: "))
            
        for i in accounts:
            if i.b_accnum == account_number:
                if amount > 0:
                    i.b_bal = float(i.b_bal)+amount
                    print("Deposited : ",amount)
                    print("New Bal : ",i.b_bal)
                    
                else:
                    print("Invalid Deposited amount.")
                break

        print("Account not found.")
        


    elif ch==5:#WithDraw
        account_number = input("Enter Account Number : ")
        amount = float(input("Enter amount to WithDraw: "))
            
        for i in accounts:
            if i.b_accnum == account_number:
                if amount > 0:
                    i.b_bal = float(i.b_bal)-amount
                    print("WithDrawn : ",amount)
                    print("New Bal : ",i.b_bal)
                    
                else:
                    print("Invalid WithDraw amount.")
                break

        print("Account not found.")

    elif ch==6:#Funds Transfer
        pass

    elif ch==7:
        #Search details of account holder
        print("")
        print("Press A to search by Account Number")
        print("Press B to search by Account Name")
        print("Press C to search by Account Type")
        
        S_ch=input('Enter your Choice : ')
        
        if S_ch=='A':
            n=int(input("Enter the Account Number to be searched "))
            for i in accounts:
                if i.b_accnum == n:
                    i.display_acc()
    
        elif S_ch=='B':
            n=input("Enter the Account Name to be searched ")
            for i in accounts:
                if i.b_acchname == n:
                    i.display_acc()
                    
        elif S_ch=='C':
            n=input("Enter the Account Name to be searched ")
            for i in accounts:
                if i.b_type == n:
                    i.display_acc()
        else:
            print("Invalid Input")


    elif ch==8:#Balance Enquiry
        pass
        
    elif ch==9: #Exit

        break
    
    elif ch==10:  #Display
       ''' for i in studlist:
            i.display( )'''
    for i in accounts:
            i.display_acc()

    else:
        print("Invalid Input")


       