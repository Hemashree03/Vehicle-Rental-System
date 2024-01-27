import users as us
import prettytable as pr
from datetime import datetime as dt

def cust_view():

    db, key = us.com_db()
    key1=key2=key
    dat=key6=key4=key
    
    print("Welcome to 'ABC' rental company")
    print("\n*---------------------------------------------------------------*\n\n")
    print("Choose what you want to view\n")
    
    print(" 1.VIEW ALL VEHICLES\n 2.VIEW ALL CARS\n 3.VIEW ALL BIKES\n")
    
    option = int(input("PRESS A NUMBER: "))
    

    dat.execute("SELECT CURDATE()")
    datecheck=dat.fetchone()[0]
    

    if option == 1:
        key.execute("SELECT V_ID, V_MODEL, RENT_AMT, V_TYPE, MIN_SD_AMT FROM VEHICLES WHERE RENTED='NO' AND service_date <= %s",(datecheck,))

    elif option == 2:
        key.execute("SELECT V_ID, V_MODEL, RENT_AMT, V_TYPE, MIN_SD_AMT FROM VEHICLES WHERE V_TYPE='CAR' AND RENTED='NO' AND service_date <= %s",(datecheck,))

    else:
        key.execute("SELECT V_ID, V_MODEL, RENT_AMT, V_TYPE, MIN_SD_AMT FROM VEHICLES WHERE V_TYPE='BIKE'AND RENTED='NO' AND service_date <= %s",(datecheck,))

    opts = key.fetchall()

    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Rented Amount", "Vehicle Type", "Minimum Security Deposit"]
    x = key.rowcount


    print("\nNUMBER OF VEHICLES: ", x)
    print()
    for row in opts:
        if len(row) == 5:
            table.add_row(row)

    print(table)
    print()
    print('''RULE - 1   YOU CAN ONLY ADD A CAR AND A BIKE AT A TIME.\nRULE - 2   YOU MUST RETURN THE VEHICLE ON SAME DAY.\nRULE - 3   YOU MUST HAVE MINIMUM SECURITY DEPOSIT AMOUNT FOR CAR - 10000 AND FOR BIKE - 3000\nRULE - 4   IF THE VEHICLE RUN MORE THAN 500KM THEN YOU MUST PAY ADDITIONAL 15%\nRULE - 5   IF YOU WANT TO EXTEND THE RENT DAY, THEN YOU CAN EXTEND CONSECUTIVELY MAXIMUM OF THREE DAYS''')
    print()

    premit=0
    vid=1
    cid = int(input("ENTER YOUR CUSTOMER ID: "))
    key6.execute("SELECT sd_amt FROM customer_details WHERE c_id=%s",(cid,))
    csd=key6.fetchone()[0]
    cart=[]
    while vid!=0 and len(cart)<2:
        vid=int(input("ENTER THE VEHICLE ID HERE TO ADD THAT VEHICLE TO YOUR CART OR ENTER 0 TO END SHOPPING: "))
        if vid!=0:
            key6.execute("SELECT min_sd_amt FROM vehicles WHERE v_id=%s",(vid,))
            vsd=key6.fetchone()[0]
        
        if vsd >csd:
            print("YOUR MINIMUM DEPOSIT AMOUNT IS LESS.....\nSO YOU HAVE TO PAY SOME AMOUNT TO RENT A VEHICLE")
            sdmt=int(input("ENTER THE SECURITY DEPOSIT AMOUNT: "))
            m=csd+sdmt
            key4.execute("UPDATE customer_details SET sd_amt = %s WHERE c_id=%s",(m,cid,))
            permit=key4.fetchone()
            db.commit()

        if vid!=0:
            cart.append(vid)
    print(cart)
    
    query="INSERT INTO ordered_details(c_id, c_name, v_id, v_model, rent_date, return_expected_date, rent_amt)\
VALUES(%s, %s, %s, %s, %s, %s, %s);"




    print("DO YOU WANT TO REMOVE A VEHICLE FROM YOUR CART ?")
    rc=int(input("IF YES PRESS - 1 ELSE PRESS - 2 TO CONTINUE: "))
    if rc==1:
        print(table)
        rem=int(input("ENTER THE VEHICLE ID TO REMOVE: "))
        if rem in cart:
            cart.remove(rem)
        else:
            pass
    print(cart)
    c=0
    table1 = pr.PrettyTable()
    table1.field_names = ["Customer ID", "Customer Name", "Vehicle ID", "Vehicle Model", "Vehicle Required Date", "Vehicle ReturnExpected Date", "Rent Amount"]

    key6.execute("SELECT c_name FROM customer_details WHERE c_id=%s",(cid,))
    cname=key6.fetchone()[0]


    for i in cart:
        
        print()
        print("VEHICLE ID:",i)
        key2.execute("SELECT v_model FROM vehicles WHERE v_id=%s", (i,))
        vm = key2.fetchone()[0]
        rd = input("ENTER RENT DATE (YYYY-MM-DD): ")
        re = input("WHEN DID YOU RETURN THE VEHICLE (DATE - YYYY-MM-DD): ")
        std=dt.strptime(rd, '%Y-%m-%d')
        ed=dt.strptime(re, '%Y-%m-%d')
        dfn=(ed-std).days
        print()
        print("NUMBER OF DAYS:",dfn)
        print()
        key1.execute("SELECT rent_amt FROM vehicles WHERE v_id=%s", (i,))
        x=key1.fetchone()[0]
        print("VEHICLE RENT FOR PER DAY:",x)
        ramt = ( 1 + dfn ) * x
        
        print("RENT AMOUNT:", ramt)
        print()
        key.execute("UPDATE vehicles SET rented='YES' WHERE v_id=%s",(vid,))
        x=key.fetchone()
        val = (cid, cname, i, vm, rd, re, ramt)
        key.execute(query, val)
        opts = key.fetchall()
        
        db.commit()
        
        key1.execute("SELECT c_id, c_name, v_id, v_model, rent_date, return_expected_date, rent_amt FROM ordered_details WHERE rent_date = %s AND  c_id = %s AND v_id=%s", (rd, cid, i, ))
        opts = key.fetchall()
        for row in opts:
            if len(row) > 1:
                table1.add_row(row)
    print(table1)
    print("YOUR FINAL RENT AMOUNT IS",ramt)
    print("\n*---------------------------------------------------------------*\n")
    print("THANK YOU.......\nCOME AGAIN")

    
        
'''    else:
        print("YOUR SECURITY AMOUNT IS VERY LOW.....")
        print("TRY AGAIN....")
'''
