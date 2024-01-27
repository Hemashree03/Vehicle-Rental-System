import users as us
import prettytable as pr
from datetime import datetime as dt


def view_vehicle(option):
    db, key = us.com_db()

    if option == 1:
        key.execute("SELECT * FROM vehicles ")

    else:
        query = "SELECT * FROM vehicles WHERE v_type=%s"
        if option == 2:
            key.execute(query, ('car',))
        else:
            key.execute(query, ('bike',))

    opts = key.fetchall()
    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                         "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]

    for row in opts:
        if len(row) == 10:
            table.add_row(row)

    print(table)
    print()


def ser_vehicle(option):
    db, key = us.com_db()

    print("Search vehicle by\n 1. VEHICLE ID\n 2. VEHICLE MODEL")
    print(" 3. VEHICLE COLOR\n 4.VEHICLE NUMBER PLATE\n 5. VEHICLE TYPE\n 6. RENT AMOUNT")
    print(" 7. SERVICE DATE\n 8. MINIMUM SECURITY DEPOSIT AMOUNT\n 9. RENTED VEHICLE\n 10. NON-RENTED VEHICLE")
    print()
    x = int(input("PRESS A NUMBER: "))
    print()

    if x == 1:

        query = "SELECT * FROM vehicles WHERE v_id=%s"
        y = input("ENTER THE VEHICLE ID: ")
        key.execute(query, (y,))

    elif x == 2:

        query = "SELECT * FROM vehicles WHERE v_model = %s"
        y = input("ENTER THE MODEL TYPE: ")
        key.execute(query, (y,))

    elif x == 3:

        query = "SELECT * FROM vehicles WHERE v_color = %s"
        y = input("ENTER THE COLOR: ")
        key.execute(query, (y,))

    elif x == 4:

        query = "SELECT * FROM vehicles WHERE no_plate = %s"
        y = input("ENTER THE NUMBER PLATE: ")
        key.execute(query, (y,))

    elif x == 5:

        query = "SELECT * FROM vehicles WHERE v_type = %s"
        y = input("ENTER THE VEHICLE TYPE: ")
        key.execute(query, (y,))

    elif x == 6:

        query = "SELECT * FROM vehicles WHERE rent_amt = %s"
        y = input("ENTER THE RENT AMOUNT: ")
        key.execute(query, (y,))

    elif x == 7:

        query = "SELECT * FROM vehicles WHERE service_date = %s"
        y = input("ENTER THE SERVICE DATE: ")
        key.execute(query, (y,))

    elif x == 8:

        query = "SELECT * FROM vehicles WHERE min_sd_amt = %s"
        y = input("ENTER THE MINIMUM SECUTRITY DEPOSIT AMOUNT: ")
        key.execute(query, (y,))

    elif x == 9:

        query = "SELECT * FROM vehicles WHERE rented  = 'NO'"
        key.execute(query)

    elif x == 10:

        query = "SELECT * FROM vehicles WHERE rented = 'YES'"
        key.execute(query)

    opts = key.fetchall()
    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                         "Service Date", "Kilometer Ran", "Vehicle Type", "Rented or Not", "Minimum Security Deposit"]

    for row in opts:
        if len(row) == 10:
            table.add_row(row)

    print(table)
    print()


def mod_vehicle(option):
    db, key = us.com_db()
    key1 = key2 = key

    key.execute("SELECT * FROM vehicles ")
    opts = key.fetchall()
    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                         "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]

    for row in opts:
        if len(row) == 10:
            table.add_row(row)

    print(table)

    if option == 5:  # MINIMUM SECURITY AMOUNT
        query = "UPDATE vehicles SET min_sd_amt = %s WHERE v_id = %s"
        y = input(
            "ENTER THE VEHICLE ID TO CHANGE THE MINIMUM SECURITY DEPOSIT AMOUNT: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]

        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("ENTER THE MINIMUM SECURITY DEPOSIT AMOUNT TO CHANGE: ")
        key.execute(query, (z, y,))

    else:
        print()
        print("Modify vehicle by\n 1. VEHICLE ID\n 2. VEHICLE MODEL")
        print(
            " 3. VEHICLE COLOR\n 4.VEHICLE NUMBER PLATE\n 5. VEHICLE TYPE\n 6. RENT AMOUNT")
        print(" 7. SERVICE DATE\n 8. MINIMUM SECURITY DEPOSIT AMOUNT\n 9. RENTED VEHICLE\n 10. NON-RENTED VEHICLE")
        print()

        x = int(input("PRESS A NUMBER: "))

        print()

        if x == 1:  # VEHICLE MODEL
            query = "UPDATE vehicles SET v_model = %s WHERE v_id = %s"
            y = (input("ENTER THE VEHICLE ID: "))
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE MODEL NAME TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 2:    # VEHICLE COLOR
            query = "UPDATE vehicles SET v_color = %s WHERE v_id = %s"
            y = input("ENTER THE VEHICLE ID: ")
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE COLOR TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 3:  # NUMBER PLATE
            query = "UPDATE vehicles SET no_plate = %s WHERE v_id = %s"
            y = input("ENTER THE VEHICLE ID: ")
            key1.execute("SELECT * FROM vehicles WHERE no_plate = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE NUMBER PLATE TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 4:  # VEHICLE TYPE
            query = "UPDATE vehicles SET v_type = %s WHERE v_id = %s"
            y = input("ENTER THE VEHICLE ID: ")
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE VEHICLE TYPE TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 5:  # RENT AMOUNT
            query = "UPDATE vehicles SET RENT_AMT = %s WHERE v_id = %s"
            y = input("ENTER THE RENT AMOUNT: ")
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE RENT AMOUNT TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 6:  # SERVICE DATE
            query = "UPDATE vehicles SET service_date = %s WHERE v_id = %s"
            y = (input("ENTER THE VEHICLE ID TO CHANGE THE SERVICE DATE: "))
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE SERVICE DATE TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 7:  # RENTED VEHICLE
            query = "UPDATE vehicles SET rented = %s WHERE v_id = %s"
            y = input("ENTER THE VEHICLE ID: ")
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE RENT TYPE TO CHANGE: ")
            key.execute(query, (z, y,))

        elif x == 8:  # NON-RENTED VEHICLE
            query = "UPDATE vehicles SET rented = %s WHERE v_id = %s"
            y = input("ENTER THE VEHICLE ID: ")
            key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
            a = key1.fetchone()

            tbl = pr.PrettyTable()
            tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                               "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
            if a is not None:
                tbl.add_row(a)
                print(tbl)

            z = input("ENTER THE RENT TYPE TO CHANGE: ")
            key.execute(query, (z, y,))

    print("DATA MODIFIED.....\n")
    opts = key.fetchall()

    db.commit()

    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                         "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
    key2.execute("SELECT * FROM vehicles")
    opts = key2.fetchall()
    for row in opts:
        if len(row) > 0:
            table.add_row(row)

    print(table)
    print()


def del_vehicle(option):
    db, key = us.com_db()
    key1 = key2 = key

    print("Delete vehicle by\n 1.VEHICLE ID\n 2. VEHICLE MODEL\n 3. VEHICLE COLOR\n 4. VEHICLE NUMBER PLATE\n \
5. VEHICLE TYPE\n 6. RENT AMOUNT\n 7. SERVICE DATE\n 8. RENTED VEHICLE\n 9. NON-RENTED VEHICLE\n")
    x = int(input("PRESS A NUMBER: "))
    print()

    if x == 1:  # VEHICLE ID
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchall()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        '''if a is not None:
            print(a)
            tbl.add_row(a)'''
        for row in a:
            tbl.add_row(row)

        print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 2:  # VEHICLE MODEL
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchall()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 3:    # VEHICLE COLOR
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 4:  # NUMBER PLATE
        query = "DELETE FROM vehicles WHERE WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 5:  # VEHICLE TYPE
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 6:  # RENT AMOUNT
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 7:  # SERVICE DATE
        query = "DELETE FROM vehicles WHERE v_id = %s"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y))

    elif x == 8:  # RENTED VEHICLE
        query = "DELETE FROM vehicles WHERE v_id = %s AND rented = 'YES'"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    elif x == 9:  # NON-RENTED VEHICLE
        query = "DELETE FROM vehicles WHERE v_id = %s AND rented = 'NO'"
        y = input("ENTER THE VEHICLE ID: ")
        key1.execute("SELECT * FROM vehicles WHERE v_id = %s", (y,))
        a = key1.fetchone()

        tbl = pr.PrettyTable()
        tbl.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                           "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
        if a is not None:
            tbl.add_row(a)
            print(tbl)

        z = input("CONFRIMATION ENTER YES OR NO: ")
        if z == 'YES' or z == 'yes':
            key.execute(query, (y,))

    db.commit()

    opts = key.fetchall()
    print("DATA DELETED.......\n")
    table = pr.PrettyTable()
    table.field_names = ["Vehicle ID", "Vehicle Model", "Vehicle Color", "Number Plate", "Rented Amount",
                         "Service Date", "Kilometer Ran", "Vehicle Type", "Rented", "Minimum Security Deposit"]
    key2.execute("SELECT * FROM vehicles")
    opts = key2.fetchall()
    for row in opts:
        if len(row) > 0:
            table.add_row(row)

    print(table)
    print()


def add_vehicle(option):
    db, key = us.com_db()

    print("ENTER DATA TO ADD A VEHICLE")
    print("\n*---------------------------------------------------------------*\n\n")
    model = input("ENTER THE VEHICLE MODEL: ")
    clr = input("ENTER THE COLOR: ")
    no_p = input("ENTER THE NUMBER PLATE OF THE VEHICLE: ")
    r_amt = int(input("ENTER THE RENT AMOUNT OF THE VEHICLE: "))
    sd = input("ENTER THE LAST SERVICE DATE (YYYY-MM-DD): ")
    km = int(input("ENTER THE NUMBER OF KILOMETER VEHICLE RAN: "))
    vt = input("ENTER THE TYPE OF VEHICLE 'BIKE' OR 'CAR': ")
    msd = int(input("ENTER THE MINIMUM SECURITY DEPOSIT AMOUNT: "))
    rented = 'NO'
    query = "INSERT INTO vehicles (v_model, v_color, no_plate, rent_amt, service_date, km, v_type, rented, min_sd_amt) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (model, clr, no_p, r_amt, sd, km, vt, rented, msd)

    try:
        key.execute(query, data)
        db.commit()
        print("DATA ADDED SUCCESSFULLY....")
    except mysql.connector.Error as err:
        print("Please try later.......... Error occurred")
        print(f"Error: {err}")
        db.rollback()


def ord_mod(option):
    db, key = us.com_db()
    key1 = key2 = key

    print("DISPLAYING THE ORDERED VEHICLE DETAILS")
    key.execute("SELECT * FROM ordered_details")
    opts = key.fetchall()

    table = pr.PrettyTable()
    table.field_names = ["Order ID", "Customer ID", "Customer Name", "Vehicle ID",
                         "Vehicle Model", "Vehicle Required Date", "Vehicle ReturnExpected Date", "Rent Amount"]
    for row in opts:
        if len(row) > 0:
            table.add_row(row)

    print(table)
    print()
    print("Choose the operation to do\n\n 1.DELETE THE VEHICLE DETAILS")
    opt = int(input("PRESS A NUMBER: "))
    if opt == 1:
        oid = int(input("ENTER THE ORDER ID TO DELETE FROM THE TABLE: "))
        key1.execute("DELETE FROM ordered_details WHERE b_id=%s", (oid,))
        opts1 = key1.fetchall()
        print()
        key.execute("SELECT * FROM ordered_details")
        opts = key.fetchall()
        db.commit()
        table = pr.PrettyTable()
        table.field_names = ["Order ID", "Customer ID", "Customer Name", "Vehicle ID",
                             "Vehicle Model", "Vehicle Required Date", "Vehicle ReturnExpected Date", "Rent Amount"]
        for row in opts:
            if len(row) > 0:
                table.add_row(row)

        print(table)


def fnl_rent(option):

    db, key = us.com_db()
    key1 = key2 = key
    key3 = key4 = key

    key.execute("SELECT * FROM bill_details")
    opts = key.fetchall()
    tbl = pr.PrettyTable()
    tbl.field_names = ["RENT ID", "VEHICLE ID", "VEHICLE MODEL", "CUSTOMER ID", "CUSTOMER NAME",
                       "KILOMETER RAN", "DAMAGE PERCENTAGE", "VEHICLE RETURN DATE", "FINAL RENT AMOUNT", "RENT DATE"]
    for row in opts:
        if len(row) > 0:
            tbl.add_row(row)
    print(tbl)
    print()
    print()

    key4.execute("SELECT * FROM ordered_details")
    opts = key4.fetchall()
    table = pr.PrettyTable()
    table.field_names = ["Order ID", "Customer ID", "Customer Name", "Vehicle ID",
                         "Vehicle Model", "Vehicle Required Date", "Vehicle ReturnExpected Date", "Rent Amount"]
    for row in opts:
        if len(row) > 0:
            table.add_row(row)

    print(table)

    q1 = "INSERT INTO bill_details(v_id, v_model, c_id, c_name, km_ran, damage_percent, r_return_date, final_rent_Amt, r_date) \
          VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    oid = int(input("ENTER THE ORDER ID: "))

    vid = int(input("ENTER THE VEHICLE ID: "))
    key1.execute("SELECT v_model FROM vehicles WHERE v_id=%s", (vid,))
    vm = key1.fetchone()[0]

    cid = int(input("ENTER THE CUSTOMER ID: "))
    key1.execute("SELECT c_name FROM customer_details WHERE c_id=%s", (cid,))
    cname = key1.fetchone()[0]

    km = int(input("ENTER THE NUMBER OF KILOMETER RUN: "))

    dp = int(input("ENTER THE DAMAGE PERCENTAGE(0%, 20%, 50%, 75%): "))

    rr = input("ENTER THE RETURN DATE: ")
    rd = input("ENTER THE RENTED DATE: ")
    key1.execute("SELECT rent_amt FROM vehicles WHERE v_id=%s", (vid,))
    fra = key1.fetchone()[0]

    key1.execute("UPDATE vehicles SET rented='NO' WHERE v_id=%s", (vid,))
    asdf = key1.fetchone()

    std = dt.strptime(rd, '%Y-%m-%d')
    ed = dt.strptime(rr, '%Y-%m-%d')
    dfn = (ed-std).days
    dfn += 1
    print("NUMBER OF DAYS", dfn)
    fa = 0
    fa += dfn * fra

    key1.execute("SELECT km FROM vehicles WHERE v_id=%s", (vid,))
    kmo = key1.fetchone()[0]
    kms = km-kmo
    if kms > 499 and kms < 900:
        k15 = 0.15 * fra
        print("DUE TO VEHICLE RAN MORE THAN 500KM YOU HAVE TO PAY ADDITIONALLY", k15)
        fa += k15
    else:
        k40 = 0.40 * fra
        print("DUE TO VEHICLE RAN MORE THAN 900KM YOU HAVE TO PAY ADDITIONALLY", k40)
        fa += k40

    if dp:
        dpx = dp//100
        dpp = fa*dpx
        fa += dpp

    print(fa)

    key2.execute("UPDATE vehicles SET km=%s WHERE v_id=%s", (km, vid,))
    qwe = key2.fetchone()

    val = (vid, vm, cid, cname, km, dp, rr, fa, rd)
    key2.execute(q1, val)
    key2.fetchall()

    if kms % 1500 > 0:
        key3.execute("UPDATE vehicles SET km=0 WHERE v_id=%s", (vid,))
        qwe = key3.fetchone()
        key3.execute(
            "UPDATE vehicles SET service_date = CURDATE()+2 WHERE v_id=%s", (vid,))
        qwe = key3.fetchone()

    key3.execute("DELETE FROM ordered_details WHERE B_id=%s", (oid,))
    qwe = key3.fetchone()

    db.commit()

    key.execute("SELECT * FROM bill_details")
    opts = key.fetchall()
    tbl1 = pr.PrettyTable()
    tbl1.field_names = ["BILL ID", "VEHICLE ID", "VEHICLE MODEL", "CUSTOMER ID", "CUSTOMER NAME",
                        "KILOMETER RAN", "DAMAGE PERCENTAGE", "VEHICLE RETURN DATE", "FINAL RENT AMOUNT", "RENT DATE"]
    for row in opts:
        if len(row) > 0:
            tbl1.add_row(row)

    print(tbl1)


def view_customers(option):

    db, key = us.com_db()

    key.execute(
        "SELECT C_ID, C_NAME, C_AGE, C_GENDER, C_MAIL, L_NO, SD_AMT FROM customer_details")
    opts = key.fetchall()

    tbl1 = pr.PrettyTable()
    tbl1.field_names = ["CUSTOMER ID", "CUSTOMER NAME", "CUSTOMER AGE", "GENDER",
                        "CUSTOMER EMAIL ID", "LICENCE NUMBER", "SECURITY DEPOSIT AMOUNT"]
    for row in opts:
        if len(row) > 0:
            tbl1.add_row(row)

    print(tbl1)


def add_service_details(option):

    db, key = us.com_db()
    key1 = key2 = key

    key1.execute("SELECT * FROM service_details")
    opts = key1.fetchall()
    table = pr.PrettyTable()
    table.field_names = ["Service ID", "Vehicle ID", "Vehicle Model", "Service Date", "Type of Service",
                         "Parts Replaced", "Cost of Service", "Comments"]
    for row in opts:
        if len(row) > 0:
            table.add_row(row)

    print(table)

    print()

    key2.execute("SELECT * FROM bill_details")
    od = key2.fetchall()

    tbl1 = pr.PrettyTable()
    tbl1.field_names = ["BILL ID", "VEHICLE ID", "VEHICLE MODEL", "CUSTOMER ID", "CUSTOMER NAME",
                        "KILOMETER RAN", "DAMAGE PERCENTAGE", "VEHICLE RETURN DATE", "FINAL RENT AMOUNT", "RENT DATE"]
    for row in od:
        if len(row) > 0:
            tbl1.add_row(row)

    print(tbl1)

    vid = int(input("ENTER THE VEHICLE ID: "))

    sdt = input("ENTER THE SERVICE DATE: ")
    key2.execute("SELECT v_model FROM vehicles WHERE v_id=%s", (vid,))
    vn = key2.fetchone()[0]
    stp = input("ENTER THE TYPE OF SERVICE: ")
    pts = input("ENTER THE PARTS REPLACED IN THE VEHICLE: ")
    sc = int(input("ENTER THE AMOUNT COST FOR THE SERVICE: "))
    cmt = input("ENTER THE COMMENTS: ")

    query = "INSERT INTO service_details(v_id, v_model, service_date, service_type, parts_replaced, service_cost, comments)\
VALUES(%s, %s, %s, %s, %s, %s, %s)"
    val = (vid, vn, sdt, stp, pts, sc, cmt)

    key.execute(query, (val))
    adt = key.fetchall()
    key2.execute("SELECT * FROM bill_details")
    adt = key2.fetchall()

    db.commit()

    sdtbl = pr.PrettyTable()
    sdtbl.field_names = ["Service ID", "Vehicle ID", "Vehicle Model", "Service Date", "Type of Service",
                         "Parts Replaced", "Cost of Service", "Comments"]
    for row in adt:
        if len(row) > 0:
            table.add_row(row)

    print(sdtbl)
