import users as us
import admin as ad
import borrower as br

class SignIn:
    def admin(self):
        print("Welcome Admin....")
        print("\n*---------------------------------------------------------------*\n\n")
        while True:
            print("\nChoose the operation to do\n")
            print("1.VIEW ALL VEHICLES\n2.VIEW ALL CARS\n3.VIEW ALL BIKES\n4.SEARCH VEHICLES\n5.MODIFY THE SERVICE DEPOSIT\n6.MODIFY THE VEHICLE DATA\n7.DELETE A VEHICLE\n8.ADD A VEHICLE\n9.MODIFY THE ORDERED VEHICLE DETAILS\n10.ENTER FINAL RANTED VEHICLE\n11.VIEW CUSTOMER DETAILS\n12.ENTER SERVICE DETAILS\n0.TO END THE OPERATION ")
            print()
            option = int(input("PRESS A NUMBER: "))
            print()

            if option == 0:
                print("\nTHANK YOU\n")
                break  # Exit the loop when the user enters 0
            elif option <= 3:
                opts = ad.view_vehicle(option)
                print(opts)
            elif option == 4:
                opts = ad.ser_vehicle(option)
            elif option <= 6:
                opts = ad.mod_vehicle(option)
            elif option == 7:
                opts = ad.del_vehicle(option)
            elif option == 8:
                opts = ad.add_vehicle(option)
            elif option == 9:
                ad.ord_mod(option)
            elif option == 10:
                ad.fnl_rent(option)
            elif option == 11:
                ad.view_customers(option)
            elif option == 12:
                ad.add_service_details(option)
            else:
                print("OPTION IS NOT VALID...")


    def borrower(self):
        br.cust_view()
        


    def add_details(self):
        print("\n*---------------------------------------------------------------*\n\n")
        print("ADDING YOUR DATA ")
        print("\n*---------------------------------------------------------------*\n\n")
        name = input("ENTER YOUR NAME: ")
        age = int(input("ENTER YOUR AGE: "))
        licence = int(input("ENTER YOUR LICENCE NUMBER: "))
        print("INITIALLY YOU HAVE TO PAY SOME AMOUNT AS SECURITY DEPOSIT AMOUNT")
        sd = int(input("ENTER THE AMOUNT: "))
        mail = input("ENTER YOUR EMAIL: ")
        password = input("ENTER YOUR PASSWORD: ")
        gender = input("YOUR GENDER: ")

        add = us.user_add(name, age, licence, sd, mail, password, gender)

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")
print()

result = us.user_check(user_name, pass_word)

sign = SignIn()

if result == 'yes':
    sign.admin()
elif result == 'yesb':
    sign.borrower()
else:
    sign.add_details()
