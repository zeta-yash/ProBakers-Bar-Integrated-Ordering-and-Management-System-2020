#main heading 
head='''
                             )  (  )  (
                            (^)(^)(^)(^)
                            _i__i__i__i_
                           (____________)
                           |####|>o<|###| 
                           (____________)
                           ProBakers' Bar
Welcome to the Integrated Ordering and Management System of ProBakers' Bar.'''
print(head.center(40))
#-------------------------------------------#
oldcust=[] #list of visited customer
seats=12 #total seat in restro
login=3 #pre assinged value

#food stock
food={'1.BlackForest':2,'2.Pastries':4,'3.CocoFudge':3,'4.Muffins':5,'5.Toast':10,
      '6.Sandwiches':7,'7.Pizza':4,'8.Buiscuits':14,'9.SoftDfrink':10,'10.Coffee':4,}
item=list(food.keys())

price=[200,50,40,20,10,30,90,25,20,35]

#===========MENU========================    
def menu():
    print('Item','\t\t','Price(in Rs.)')
    for i in range(0,10):
        print(list(food.keys())[i],'\t\t',price[i])
    
   
    

def chosecorrect():
    print("Oops! Option is not available. ")
##-------------------------------------------------##

    
#first choice to choose among staff or customer
    
while login!=0:
    print('''Login as:
         1.Customer
         2.Staff
         0.Exit''')
    login=int(input("Choose from the options given above:"))
    reply=10 #to make the value of reply exist

#==============CUSTOMER SECTION===========================================
    
    
    while login==1 and reply!=0:
        name=input("Please enter your name:")    
#for visited customer------------------------- 

        if name.upper() in oldcust:
            print("Welcome Back!",name,'''How can I help you?''')
            while reply!=0:
                print('''
                  1.Book Seat
                  2.Give Order
                  3.MENU
                  4.Generate Bill
                  5.Give Rating
                  0.Exit''')
                reply=int(input("Enter the choice:"))

                if reply==1 and seats>0:
                    print('Available Seats:',seats)
                    seatnum=int(input('Enter no. of Seats you want:'))
                    if seats<seatnum:
                        print("Sorry! Restro is full now.. Please try after some time..")
                    seats=seats-seatnum
                    print('Your Booking Confirmed')
                    
                if reply==1 and seats<=0:
                    print("Sorry! Restro is full now.. Please try after some time..")
                    
                if reply==2:
                    foodcodes=eval(input("Enter the food codes here (in '[]' brackets):"))
                    for m in range(0,(len(foodcodes))):
                        summ=(item[foodcodes[m]-1])
                    print('Your order has been placed!')
                    print('Order Summary',summ)    
                    
                if reply==3:
                    menu()
                    reply=int(input("Press 5 to exit"))

                
                    
                    
                if reply==5:
                    rate=int(input('Give us rating out of 10:'))
                    print('Thankyou for your valuable rating.')
                    
                

#for customer visited first time-------------------
        
        if name.upper() not in oldcust and reply!=0:
            print('Welcome!',name,'You visited first time here.'
            '''How can I help you?''')
            while reply!=0:
                print('''
                  1.Book Seat
                  2.Give Order
                  3.MENU
                  4.Generate Bill
                  5.Give Rating
                  0.Exit''')
                oldcust.append(name.upper())
                
                reply=int(input("Enter the choice:"))
                
                if reply==1 and seats>0:
                    print('Available Seats are only:',seats)
                    seatnum=int(input('Enter no. of Seats you want:'))
                    
                    if seats<seatnum or seats==0:
                        print("Sorry",seatnum,"seats are not available..")
                        
                    if seats<=0:
                        print("Sorry! Restro is full now.. Please try after some time..")
                    
                    if seats>=seatnum:
                        print('Your Booking Confirmed')
                        seats=seats-seatnum
                    
                if reply==2:
                    foodcodes=eval(input("Enter the food codes here (in '[]' brackets):"))
                    print('Your order has been placed!')
                    print('Order Summary:')
                    for m in range(0,(len(foodcodes))):
                        summ=(item[foodcodes[m]-1])
                        print('')
                        print(summ)
                    
                    

                if reply==4:
                    print('Items \t\t\t Price')
                    print('================================')
                    tot=[]
                    for m in range(0,(len(foodcodes))):
                        print(item[foodcodes[m]-1],'\t\t',price[foodcodes[m]-1])
                        tot.append(price[foodcodes[m]-1])
                        
                    print('================================')
                    print('Total','\t\t\t',sum(tot))
                     
                if reply==5:
                    rate=int(input('Give us rating out of 10:'))
                    print('Thankyou for your valuable rating.')
                    
                if reply==3:
                    menu()
                    reply=int(input("Press 5 to exit"))
                    
                      
    else:
        #for any incorrect input------------------------
        if login not in [1,2,0]: 
            chosecorrect()
        # restarts the program again....................
        else:
            print("")
#================XXXXXXXXXXXXXX CUSTOMER SECTION ENDS XXXXXXXXXXXXXX============================#
else:
    print("Thankyou!")
    
    
