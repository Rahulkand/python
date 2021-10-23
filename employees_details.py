import csv
def file(list):
    with open("employee__details.csv","a",newline="")as csv_file:
        write=csv.writer(csv_file)
        if csv_file.tell()==0:
            write.writerow(["name","sal","age"])
        write.writerow(list)

ch=1
num=1
while(ch==1):
    employee_details=input("enter the details of employee {0} in the form of NAME: , SAL: , AGE: ,:".format(num))
    list=employee_details.split()
    print("\nThe empolyee details are as follows\nNAME:{0}\nSAL:{1}\nAGE:{2}\n"
          .format(list[0],list[1],list[2]))
    correct=int(input("are the entered details correct 1.yes 2.no"))
    if(correct==1):
        file(list)
        ch=int(input("do u want to enter the details 1.yes 2.no"))
        num=num+1
    else:
        print("please re enter the details\n")
        ch=1

