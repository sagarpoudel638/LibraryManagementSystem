def display():
    print("Book ID          Bookname          Author          Quantity          Price in $")
    print("--------------------------------------------------------------------------")
    file=open("coursework.txt","r")
    sn=1# for serial number in bill
#for reading and displaying books of text file
    for line in file:
        print(" ",sn,"\t\t"+line.replace(",","\t")+"\t")
        sn=sn+1
    print("--------------------------------------------------------------------------")    
    return display
