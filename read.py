#keeping values in dictionary
def reading():
    file=open("coursework.txt","r")
    d={}
    s=1
    for line in file:
        line=line.replace("\n","" )
        d[s]=line.split(",")
        s=s+1
    dictionary=d
    return(dictionary)


    



