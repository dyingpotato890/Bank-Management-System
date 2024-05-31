import csv
import os
import random
import pymsgbox
import datetime
import mysql.connector as mysql

from customer import _customer_

conn = mysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='bank_management_system',
                     charset='utf8')
cur = conn.cursor()

today = datetime.date.today()

class _admin_:
    # ADMIN MODULE
    @staticmethod
    def admin():
        while True:
            print('\n')
            print('\t\t\t\t         ================================================')
            print('\t\t\t\t         ~~~~~~~~~~~~~~~~~~~ SERVICES ~~~~~~~~~~~~~~~~~~~')
            print('\t\t\t\t         ================================================')
            print()
            print('\t\t\t\t\t\t    1.Customer Account Creation')
            print('\t\t\t\t\t\t    2.Customer Account Removal')
            print('\t\t\t\t\t\t    3.Add New Admin')
            print('\t\t\t\t\t\t    4.Remove Existing Admin')
            print('\t\t\t\t\t\t    5.Show Admin(s)')
            print('\t\t\t\t\t\t    6.Show Customers(s)')
            print('\t\t\t\t\t\t    7.Show Transaction(s)')
            print('\t\t\t\t\t\t    8.Go Back')
            print()
            print('\t\t\t\t         ================================================')
            print()
            o1 = int(input('Enter Your Option: '))
            print()

            if o1 == 1:
                _admin_.add_customer()
            elif o1 == 2:
                _admin_.remove_customer()
            elif o1 == 3:
                _admin_.add_admin()
            elif o1 == 4:
                _admin_.remove_admin()
            elif o1 == 5:
                _admin_.show_admin()
            elif o1 == 6:
                _admin_.show_customer()
            elif o1 == 7:
                _admin_.view_transactions()
            elif o1 == 8:
                choice = pymsgbox.confirm('Are you Sure You Want To Go back', 'Confirm', ["Yes", 'No'])
                if choice == 'Yes':
                    break
            else:
                pymsgbox.alert('Please Choose A Valid Service!', 'ALERT')
    
    # ADMIN LOGIN
    @staticmethod
    def admin_login():
        username = input('Username: ')
        password = input('Password: ')
        print()
        login = 0

        f = open('Python/Bank Management System/adminlogin.csv', 'r')
        r = csv.reader(f)

        for i in r:
            if username == i[2] and password == i[3]:
                login = 1
                comment = 'Welcome ' + i[1] + '!'
                pymsgbox.confirm(comment, 'Etihad National Bank', ["Enter"])
                f.close()
                return login

    # TO ADD A NEW CUSTOMER
    @staticmethod
    def add_customer():
        f = open('Python/Bank Management System/customerlogin.csv', 'a', newline = '')
        w = csv.writer(f)

        cust_id = input('\t\t\t\t\t          Enter The Customer ID(CXXX): ')
        cust_name = input('\t\t\t\t\t          Enter The Name: ')
        cust_age = int(input('\t\t\t\t\t          Enter The Age: '))
        cust_gender = input('\t\t\t\t\t          Enter The Gender(M/F/O): ')
        cust_phn = int(input('\t\t\t\t\t          Enter The Phone Number: '))
        cust_email = input('\t\t\t\t\t          Enter The Email-ID: ')
        cust_balance = 0
        print()

        process = 'y'
        while process == 'y':
            cust_account_number = random.randint(900000000, 999999999)
            sql = "select * from customer_details where account_number=%s"
            cur.execute(sql, (cust_account_number,))
            A = cur.fetchall()
            if not A:
                print("\t\t\t\t\t          Your account number is: ", cust_account_number)
                print()

                cust_pin = int(input('\t\t\t\t\t          Enter A Four Digit PIN: '))
                cus_balance = 0
                print()

                cur.execute("insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (cust_id, cust_account_number, cust_name, cust_gender, cust_age, cust_phn, cust_email , cust_balance))

                process = 'n'

        print('\t\tPlease Create A Username And Password For Online Banking. Enter The Below Details Carefully.\n')

        print('\t\t\t\t\t  ********************************************\n')
        cust_username = input('\t\t\t\t\t\t  Create A Username: ')
        cust_password = input('\t\t\t\t\t\t  Create A Password: ')
        print('\n\t\t\t\t\t  ********************************************')
        w.writerow([cust_id, cust_account_number, cust_name, cust_username, cust_password, cust_pin])

        conn.commit()
        f.close()

        print()
        pymsgbox.alert('Account Created Successfully!', 'Etihad National Bank')

    # TO REMOVE AN EXISTING CUSTOMER
    @staticmethod
    def remove_customer():
        delete_id = input('Enter The Customer ID: ')
        print()

        temp = []
        with open('Python/Bank Management System/customerlogin.csv', 'r', newline = '') as f1:
            r = csv.reader(f1)
            for i in r:
                temp.append(i[0])

        if delete_id in temp:
            f1 = open('Python/Bank Management System/customerlogin.csv', 'r', newline = '')
            r = csv.reader(f1)
            f2 = open('duplicate.csv', 'a', newline = '')
            w = csv.writer(f2)

            query1 = 'delete from customer_details where CUSTOMER_ID=%s'
            cur.execute(query1, (delete_id,))
            conn.commit()

            for i in r:
                if i[0] != delete_id:
                    w.writerow(i)

            f1.close()
            f2.close()
            os.remove('Python/Bank Management System/customerlogin.csv')
            os.rename('duplicate.csv', 'Python/Bank Management System/customerlogin.csv')

            pymsgbox.alert('The Customer Has Been Removed.', 'Etihad National Bank')
            print()
        else:
            pymsgbox.alert('The Customer Does Not Exist In The System.', 'Etihad National Bank')

    # TO ADD AN ADMIN
    @staticmethod
    def add_admin():
        with open('Python/Bank Management System/adminlogin.csv', 'a', newline = '') as f:
            w = csv.writer(f)
            print()

            admin_id = input('\t\t\t\t\t          Enter The Admin ID (AXXX): ')
            admin_name = input('\t\t\t\t\t          Enter Admin Name: ')
            admin_designation = input('\t\t\t\t\t          Enter The Designation: ')
            admin_joindate = today.strftime("%y/%m/%d")
            print()

            print('\t\t     Please Create A Username And Password For The Admin. Enter The Below Details Carefully.')
            print()

            print('\t\t\t\t\t  ********************************************')
            print()
            admin_username = input('\t\t\t\t\t\t  Create A Username: ')
            admin_password = input('\t\t\t\t\t\t  Create A Password: ')
            print()
            print('\t\t\t\t\t  ********************************************')

            l = [admin_id, admin_name, admin_username, admin_password]
            print()

            cur.execute("insert into admin_details values(%s,%s,%s,%s)",(admin_id, admin_name, admin_designation, admin_joindate))
            conn.commit()
            w.writerow(l)

        pymsgbox.alert('A New Admin Has Been Added Successfully!', 'Etihad National Bank')
        print()

    # TO REMOVE AN ADMIN
    @staticmethod
    def remove_admin():
        delete_id = input('Enter The Admin ID: ')
        print()

        temp = []
        with open('Python/Bank Management System/customerlogin.csv', 'r', newline = '') as f1:
            r = csv.reader(f1)
            for i in r:
                temp.append(i[0])

        if delete_id in temp:
            f1 = open('Python/Bank Management System/adminlogin.csv', 'r', newline='')
            f2 = open('duplicate.csv', 'a', newline='')
            r = csv.reader(f1)
            w = csv.writer(f2)

            query1 = 'delete from admin_details where ADMIN_ID=%s'
            cur.execute(query1, (delete_id,))
            conn.commit()

            for i in r:
                if i[0] != delete_id:
                    w.writerow(i)

            f1.close()
            f2.close()
            os.remove('Python/Bank Management System/adminlogin.csv')
            os.rename('duplicate.csv', 'Python/Bank Management System/adminlogin.csv')
            pymsgbox.alert('The Admin Has Been Removed Successfully.', 'Etihad National Bank')
            print()
        else:
            pymsgbox.alert('The Customer Does Not Exist In The System.', 'Etihad National Bank')
    
    # TO SHOW ALL CUSTOMERS
    @staticmethod
    def show_customer():
        cur.execute('select * from customer_details order by customer_id')
        s = cur.fetchall()
        
        print("Present Content Of The Table:\n")
        print('\t\t' + '================================================================ CUSTOMERS =================================================================\n')
        print('\t\t' + '-' * 140)
        print('\t\t' + '{:<15}'.format("CUSTOMER_ID"),
              '{:<15}'.format("ACCOUNT NUMBER"),
              '{:<22}'.format("NAME"),
              '{:<10}'.format("GENDER"),
              '{:<10}'.format("AGE"),
              '{:<15}'.format("PHONE NUMBER"),
              '{:<35}'.format("EMAIL"),
              '{:<15}'.format("BALANCE"))
        print('\t\t' + '-' * 140)

        for k in s:
            print('\t\t' + '{:<15}'.format(k[0]),
                  '{:<15}'.format(k[1]),
                  '{:<22}'.format(k[2]),
                  '{:<10}'.format(k[3]),
                  '{:<10}'.format(k[4]),
                  '{:<15}'.format(k[5]),
                  '{:<35}'.format(k[6]),
                  '{:<15}'.format(k[7]))
            print()
            print('\t\t' + '-' * 140)

        print('\n\t\t' + '============================================================================================================================================\n')

    # TO SHOW ALL ADMINS
    @staticmethod
    def show_admin():
        cur.execute('select * from admin_details')
        s = cur.fetchall()
        
        print("Present Content Of The Table:")
        print('\n\t\t\t\t' + '=========================== ADMINS ===========================\n')
        print('\t\t\t\t' + '-' * 62)
        print('\t\t\t\t' + '{:<10}'.format("ADMIN_ID"),
              '{:<22}'.format("NAME"),
              '{:<15}'.format("DESIGNATION"),
              '{:<15}'.format("DATE_OF_JOIN"))
        print('\t\t\t\t' + '-' * 62)

        for k in s:
            print('\t\t\t\t' + '{:<10}'.format(k[0]), '{:<22}'.format(k[1]), '{:<15}'.format(k[2]),'{:<15}'.format(str(k[3])))
            print()
            print('\t\t\t\t' + '-' * 62)

        print('\n\t\t\t\t' + '==============================================================\n')

    # BANK STATEMENT FOR ADMINS
    @staticmethod
    def view_transactions():
        while True:
            print('\n\t\t\t\t\t    =========================================')
            print('\t\t\t\t\t    ~~~~~~~~~~~~~~~~ OPTIONS ~~~~~~~~~~~~~~~~')
            print('\t\t\t\t\t    =========================================\n')
            print('\t\t\t\t\t\t      1.Show All Transactions')
            print('\t\t\t\t\t\t      2.Sort By Date')
            print('\t\t\t\t\t\t      3.Sort By Account Number')
            print('\t\t\t\t\t\t      4.Go Back\n')
            print('\t\t\t\t\t    =========================================\n')
            
            o = int(input('Enter Your Option: '))
            print()

            if o == 1:
                cur.execute('select * from customer_transactions')
                all_trans = cur.fetchall()

                if all_trans == []:
                    pymsgbox.alert('No Tranasctions Have Been Recorded In The System.', 'ALERT')
                else:
                    _customer_.bank_statement(all_trans)
            elif o == 2:
                date = input('Enter The Date(yyyy-mm-dd): ')
                print()

                cur.execute('select * from customer_transactions where date=%s', (date,))
                date = cur.fetchall()

                if date == []:
                    pymsgbox.alert('No Transactions Were Made On This Day.', 'ALERT')
                else:
                    _customer_.bank_statement(date)
            elif o == 3:
                acc_no = int(input('Enter The Account Number: '))
                print()

                cur.execute('select * from customer_transactions where account_number=%s', (acc_no,))
                trans = cur.fetchall()

                if trans == []:
                    pymsgbox.alert('The Account Number Does Not Exist!', 'ALERT')
                else:
                    _customer_.bank_statement(trans)
            elif o == 4:
                choice = pymsgbox.confirm('Are you Sure You Want To Go Back', 'Confirm', ["Yes", 'No'])
                if choice == 'Yes':
                    break
            else:
                pymsgbox.alert('Please Enter A Valid Option!', 'ALERT')