import mysql.connector
import borrower as br


def com_db():
    db_config = {
        "host": "__________",
        "user": "_________",
        "password": "________",
        "database": "________",
    }

    db = mysql.connector.connect(**db_config)

    key = db.cursor()

    return db, key


def user_check(user_name, pass_word):

    db, key = com_db()

    query = "SELECT * FROM admin_details WHERE a_mail = %s AND a_password = %s"

    key.execute(query, (user_name, pass_word))

    result = key.fetchone()

    if result:
        return 'yes'
    else:
        key.execute(
            ' SELECT * FROM CUSTOMER_DETAILS WHERE C_MAIL=%s AND c_password = %s', (user_name, pass_word,))
        r = key.fetchone()
        if r:
            return 'yesb'


def user_add(name, age, licence_no, sd_amt, email, password, gender):

    db, key = com_db()

    com_db()

    insert_query = "INSERT INTO CUSTOMER_DETAILS (C_NAME, C_AGE, L_NO, SD_AMT, C_MAIL, C_PASSWORD, C_GENDER) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    data = (name, age, licence_no, sd_amt, email, password, gender)

    try:
        key.execute(insert_query, data)
        db.commit()
        print("DATA ADDED SUCCESSFULLY....")
        br.cust_view()
    except mysql.connector.Error as err:
        print("Please try later.......... Error occuried")
        print(f"Error: {err}")
        db.rollback()
