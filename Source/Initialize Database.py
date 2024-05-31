import mysql.connector as mysql
import csv
import os

def customer_details(cur):
    cur.execute('create table IF NOT EXISTS customer_details(CUSTOMER_ID varchar(4) primary key,ACCOUNT_NUMBER int,NAME varchar(30),GENDER char(1),AGE int,PHONE_NUMBER varchar(20),EMAIL_ID varchar(50),BALANCE int default 0)')
    cur.execute("insert into customer_details values('C001',952090760,'Reuben Jude Cherian','M',20,'+971561442688','reubenjudecherian@gmail.com',9000)")
    cur.execute("insert into customer_details values('C002',970439492,'Afia Nasumudeen','F',19,'+919037458082','afianasumudeen@gmail.com',6600)")
    conn.commit()

def admin_details(cur):
    cur.execute('create table IF NOT EXISTS admin_details(ADMIN_ID char(4) primary key,NAME varchar(30),DESIGNATION varchar(30),JOIN_DATE date)')
    cur.execute("insert into admin_details values('A001','Niranjay Ajayan','Owner','2022-01-02')")
    cur.execute("insert into admin_details values('A002','Annika Das','Manager','2022-01-02')")
    conn.commit()

def customer_transactions(cur):
    cur.execute('create table IF NOT EXISTS customer_transactions(ACCOUNT_NUMBER int,NAME varchar(40),AMOUNT int,TRANSACTION_TYPE varchar(30),DATE date)')

def create_database(cursor):
    try:
        cursor.execute('CREATE DATABASE IF NOT EXISTS bank_management_system')
        print("Database 'bank_management_system' created successfully.")
    except mysql.Error as err:
        print(f"Error creating database: {err}")

def add_admin(cur):
    cur.execute("select * from admin_details;")
    items = cur.fetchall()

    file_path = os.path.join("C:\\Users\\niran\\Documents\\VS Code\\Python\\Bank Management System", 'adminlogin.csv')

    with open(file_path, 'a', newline = '') as f:
        w = csv.writer(f)
        
        for i in range (0 , len(items)):
            admin_id = items[i][0]
            admin_name = items[i][1]
            admin_username = "admin_{}".format(i+1)
            admin_password = "1234"
        
            l=[admin_id, admin_name, admin_username, admin_password]
            w.writerow(l)

    print('\nThe Default Username for Admins are admin_1/admin_2 and Password is 1234\n')

def add_customer(cur):
    cur.execute("select * from customer_details;")
    items = cur.fetchall()

    file_path = os.path.join("C:\\Users\\niran\\Documents\\VS Code\\Python\\Bank Management System", 'customerlogin.csv')

    with open(file_path, 'a', newline = '') as f:
        w = csv.writer(f)
        
        for i in range (0 , len(items)):
            cust_id = items[i][0]
            cust_acc_no = items[i][1]
            cust_name = items[i][2]
            cust_username = "cust_{}".format(i+1)
            cust_password = cust_pin = "1234"
        
            l = [cust_id, cust_acc_no, cust_name, cust_username, cust_password, cust_pin]
            w.writerow(l)

    print('The Default Username for Customer are cust_1/cust_2 and Password & PIN is 1234\n')

if __name__ == "__main__":
    host = input('Host: ')
    user = input('User: ')
    password = input('Password: ')

    try:
        mysqlconn = mysql.connect(host=host,
                                  user=user,
                                  passwd=password,
                                  charset='utf8')
        mysqlcursor = mysqlconn.cursor()

        create_database(mysqlcursor)
        mysqlconn.close()

        conn = mysql.connect(host=host,
                             user=user,
                             passwd=password,
                             database='bank_management_system',
                             charset='utf8')
        cur = conn.cursor()

        customer_details(cur)
        admin_details(cur)
        customer_transactions(cur)
        conn.commit()

        add_admin(cur)
        add_customer(cur)
        conn.close()

        print('Done')
    except mysql.Error as err:
        print(f"MySQL error: {err}")