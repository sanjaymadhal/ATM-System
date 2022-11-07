#ATM System
#Time module to show real time process
import time as t
import os

clear = lambda: os.system('cls')
clear()

print("\n~~~~~~~~~~Welcome~~~~~~~~~~\n\n")
t.sleep(1)

#Balance as m
m = 25000

#Pin number
p = int(input("Enter Your 4 digit Pin: "))
t.sleep(1)

if(p == 1234):
    #Account type Choice
    clear = lambda: os.system('cls')
    clear()
    print("\n\nSelect Your Account Type: \n")
    print("1-Savings\n")
    print("2-Current\n")
    
    A = int(input("[1/2]: "))
    
    clear = lambda: os.system('cls')
    clear()
    if(A == 1):
        print("\n~~~~~~Savings Account~~~~~~")
    elif(A == 2):
        print("\n~~~~~~Current Account~~~~~~")
    else:
        print("\n\n~~~~Invalid Account type~~~~")        
    
    
    #Choices
    t.sleep(1)
    print("\n\n\t1 Withdraw\n")
    print("\t2 Balance Enquiry\n")
    print("\t3 Fast Cash\n")
    print("\t4 Change Pin\n")
    print("\t5 Cancel\n\n")
     
    c = int(input("Please Enter the number to Proceed: "))

    
    #Withdraw Condition 
    if(c == 1):
        t.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        print("\nAvailable Amount = 500")
        w = int(input("\nEnter the Withdraw Amount: ")) 
        if(w<m or w==m and w%100 == 0):
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("\n~~~Transaction Successfull~~~\n")
            t.sleep(1)
            print("\n~~~Please Collect your Cash and Card~~~\n")
            t.sleep(1)
            print("\nYour Available Balance is:", m-w)
            t.sleep(1)
            print("\n\n~~~Thank You Visit Again~~~\n")
        else:
            t.sleep(1)
            clear = lambda: os.system('cls')
            clear()
            print("\n~~Entered Amount Unavailable~~\n")
    
    
    #Balance Enquiry Condition
    elif(c == 2):
        t.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        print("Your Avaliable Balance is: ", m) 
    
    
    #Fast Cash Condition
    elif(c == 3):
        print("5000")              
        print("10,000")              
        print("15,000")              
        print("20,000")

        f = int(input("Enter the Fast Cash Amount: "))
        #If required amount is 5000
        if(f == 5000 and 5000<m):
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("\n~~~Transaction Successfull~~~\n")
            t.sleep(1)
            print("\n~~~Please Collect your Cash and Card~~~\n")
            t.sleep(1)
            print("\nYour Available Balance is:", m-f)
            t.sleep(1)
            print("\n\n~~~Thank You Visit Again~~~\n")
        #If required amount is 10000
        elif(f == 10000 and 10000<m):
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("\n~~~Transaction Successfull~~~\n")
            t.sleep(1)
            print("\n~~~Please Collect your Cash and Card~~~\n")
            t.sleep(1)
            print("\nYour Available Balance is:", m-f)
            t.sleep(1)
            print("\n\n~~~Thank You Visit Again~~~\n")                  
        #If required amount is 15000
        elif(f == 15000 and 15000<m):
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("\n~~~Transaction Successfull~~~\n")
            t.sleep(1)
            print("\n~~~Please Collect your Cash and Card~~~\n")
            t.sleep(1)
            print("\nYour Available Balance is:", m-f)
            t.sleep(1)
            print("\n\n~~~Thank You Visit Again~~~\n")                  
        #If required amount is 20000
        elif(f == 20000 and 20000<m):
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("\n~~~Transaction Successfull~~~\n")
            t.sleep(1)
            print("\n~~~Please Collect your Cash and Card~~~\n")
            t.sleep(1)
            print("\nYour Available Balance is:", m-f)
            t.sleep(1)
            print("\n\n~~~Thank You Visit Again~~~\n")
        #If required amount is Invalid
        else:
            clear = lambda: os.system('cls')
            clear()
            t.sleep(1)
            print("~~Invalid Fast Cash Amount~~")
    
    
    #Change Pinn Condition
    elif(c == 4):
        clear = lambda: os.system('cls')
        clear()
        op = int(input("\n\nEnter your Old Pin: "))
        if(op == 1234):
            np = int(input("\n\nEnter New Pin: "))
            if(np == 1234):
                t.sleep(0.8)
                print("\n                 ~~~Try Again Your Old Pin is Similar~~~\n")
            else:
                t.sleep(1)
                ("~~~~Pin Changed Successfully~~~~")    
        else:
            t.sleep(1)
            print("~~Wrong Pin~~")
    

    #Exit Condition
    elif(c == 5):
        clear = lambda: os.system('cls')
        clear()
        t.sleep(0.5)
        print("Exiting...\n")
        t.sleep(0.5)
        print("\n\n~~~Thank You Visit Again~~~\n")
        exit()


    #If the entered choice is Wrong
    else:
        t.sleep(1)
        print("\n\n~~~~Wrong Choice~~~~\n\n")        


#If the entered Pin is wrong 
else:
    t.sleep(1)
    print("\n\n~~~~Wrong Pin Number~~~~")                                      
    print("\n~~~~TRY-AGAIN~~~~\n\n")                                      
