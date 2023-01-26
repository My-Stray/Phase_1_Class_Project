
#Justin Stevens CIS261 Phase 1


end=0 
print("Welcome to Payroll\n")
Employee=str
print()
Employee = input("Enter employees name, or press 0 to end : ")
while Employee != end:
    print()
    hours = round(40,2)
    hours = (input("Enter total hours worked: ", ))
    hourlyrate = (input("Enter employees hourly rate:$ ", ))
    taxrate = input("Enter tax rate : ",)
    reghours = int(hours)
    regpay = round(reghours * hourlyrate, .2)
    overtimerate = float(hourlyrate * 1.5, .2)
    overtimepay = float(overtimehours * overtimerate)
    incometax = (float(grosspay * taxrate, .2))
    grosspay = float(regpay + overtimepay, .2)
    netpay = float(grosspay - incometax, .2)
    if Totalhours < 40:
            print("Employee Name : ",Employee)
            print("Total hours : ",Totalhours,.2)
            print("Hourly rate : $",hourlyrate,.2)
            print("Regular hours pay : $",regpay,.2)
            print("Overtime hours : 0")
            print("Overtimerate : $",overtimerate)
            print("Overtime Pay : $0.00")
            print("Gross Pay: $ ",grosspay,.2 )
            print('Income tax: $ ',incometax,.2)
            print("Net pay: $ ",netpay,.2)
    else: 
            overtimehours = round(hours - 40.00,2)
            reghours = (hours) - (overtimehours)
            print("Employee Name : ",Employeename)
            print("Total hours : ",Totalhours,.2)
            print("Regular hours : ",reghours,.2)
            print("Hourly rate : $",hourlyrate,.2)
            print("Regular hours pay : $",regpay,.2)
            print("Overtime hours: ",overtimehours)
            print("Overtimerate: $ ",overtimerate,.2)
            print("Overtime Pay: $ ",overtimepay,.2)
            print("Gross Pay: $ ",grosspay,.2)
            print('Income tax: $ ',incometax,.2)
            print("Net pay: $ ",netpay,.2)
   
    
    
   