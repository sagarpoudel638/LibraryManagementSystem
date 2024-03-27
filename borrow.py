def borrow(): #function for borrowing books 
    import read #importing module read
    dictionary1=read.reading() #calling function of module read
    application11=False #initiazing boolean value for runnning loop 
    while application11==False: #loop for repeating string of line 6 ifuser gives wrong value 
        asking = input("Do you want to borrow or return? (b/r)")
        if asking =="b" or asking=="B":
            application=False
            while application==False: # loop for repeating program from line 15 
                right=False
                while right==False: # loop for repeating if user gives number of book out of bound 
                    check2=False
                    while check2==False: # loop for prevent crashing and repeating if user gives wrong input
                        try:
                            book_id=int(input("Enter Book Id from above list"))
                            check2=True
                        except:
                            print("Enter valid book id")
                    if book_id<1 and book_id>int(dictionary1):
                        print("Enter valid Book id")
                    else:
                        right=True
                
                amount=False
                while amount==False:# loop for repeating asking of quantity if quantity ask is out of stock 
                    check3=False
                    while check3==False: # loop for preventing crash if user gives wrong input 
                        try:
                         borrow_quantity=int(input("Enter Quantity:"))
                         check3=True
                        except:
                            print("enter valid quantity")
                    if borrow_quantity>int(dictionary1[book_id][2]):
                        print("out of stock")
                    else:
                        amount=True
                to_be_continue=False
                while to_be_continue==False: # loop for asking user if they want to continue or not 
                    check4=False
                    while check4==False: # loop for preventing crash if user gives wrong format other than Y or N 
                        try:
                            continue1=input("Do you want to change your mind? (Y/N)")
                            check4=True
                        except:
                            print("Enter valid Alphabet")
                    if continue1=="N" or continue1=="n":
                        to_be_continue=True
                        application=True
                    elif continue1=="Y" or continue1=="y":
                        to_be_continue=True
                        application=False
                        
                    
                        
            application11=True

        elif asking =="r" or asking=="R": # here codes for returning of books starts and all loops are similar
            application1=False
            while application1==False:
                right1=False
                while right1==False:
                    check21=False
                    while check21==False:
                        try:
                            book_id=int(input("Enter Book Id from above list"))
                            check21=True
                        except:
                            print("enter valid book id")
                    if book_id<1 and book_id>int(dictionary1):
                        print("Enter valid Book id")
                    else:
                        right1=True
                amount1=False
                while amount1==False:
                    check31=False
                    while check31==False:
                        try:
                             returned_quantity=int(input("Enter Quantity:"))
                             check31=True
                        except:
                            print("enter valid quantity")
                
                    if returned_quantity>int(dictionary1[book_id][2]):
                        print("Out of Stock")
                    else:
                        amount1=True
                to_be_continue1=False
                while to_be_continue1==False:
                    check41=False
                    while check41==False:
                        try:
                            continue11=input("Do you want to change your mind ? (Y/N)")
                            check41=True
                        except:
                            print("Enter valid Alphabet")
                    if continue11=="N" or continue11=="n":
                        to_be_continue1=True
                        application1=True
                    elif continue11=="Y" or continue11=="y":
                        to_be_continue1=True
                        application1=False
            application11=True
        else:
            application11=False

                #creating bill of borrow and return
    import datetime # importing datetime 
    real_name=input("Enter Your Name:")
    date_received=str(datetime.datetime.now())
    virtual_name=str(datetime.datetime.now())
   
    #printing of bill 
    print("--------------------------------------------------------------------------------------------")
    print("Name:" +real_name+"                             " +" Date :"+ date_received)
    print("--------------------------------------------------------------------------------------------")
    if asking=="b" or asking=="B": # printing if borrowed 
        quantity_borrowed=str(borrow_quantity)
        quantity_borrowed1=borrow_quantity
        print("name of book borrowed          quantity           per price ")
        print(dictionary1[book_id][0]+"                     "+ quantity_borrowed+"          " + dictionary1[book_id][3])
        totalprice=str(borrow_quantity*float(dictionary1[book_id][3]))
        print("                                                                      ")
        print("                                                                      ")
        print("                                                                      ")
        print("                                                                      ")
        print("                                                                      ")
        print("----------------------------------------------------------------------")
        print("                                                          ------------")
        print("                                                          "+"net total")
        print("                                                          $"+totalprice)
                                           
    elif asking=="r" or asking=="R":#printing if returned
        quantity_returned=str(returned_quantity)
        print("name of book returned          Quantity           per price in $")
        print(dictionary1[book_id][0] +  "                     "  + quantity_returned+ "              " + dictionary1[book_id][3])
    

        

