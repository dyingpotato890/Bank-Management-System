import mysql.connector as mysql
import pymsgbox
import csv
from datetime import date

from loan import _loan_

conn = mysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='bank_management_system',
                     charset='utf8')
cur = conn.cursor()

today = date.today()

#['C001', '952090760', 'Reuben Jude Cherian', 'cust_1', '1234', '1234']

class _customer_:    
    # CUSTOMER MODULE
    @staticmethod
    def customer(s):
        while True:
            print('\n\t\t\t\t\t    ==========================================')
            print('\t\t\t\t\t    ~~~~~~~~~~~~~~~~ SERVICES ~~~~~~~~~~~~~~~~')
            print('\t\t\t\t\t    ==========================================')
            print()
            print('\t\t\t\t\t\t        1.Cash Withdrawal')
            print('\t\t\t\t\t\t        2.Cash Deposit')
            print('\t\t\t\t\t\t        3.Loan Information')
            print('\t\t\t\t\t\t        4.Calculate Your EMI')
            print('\t\t\t\t\t\t        5.Bank Statement')
            print('\t\t\t\t\t\t        6.Go Back')
            print()
            print('\t\t\t\t\t    ==========================================')
            print()

            o1 = int(input('Please Enter Your Option: '))
            print()

            if o1 == 1:
                _customer_.withdraw(s)
            elif o1 == 2:
                _customer_.deposit(s)
            elif o1 == 3:
                _customer_.loan_info(s)
            elif o1 == 4:
                _loan_.calculate_emi()
            elif o1 == 5:
                acc_no = s[1]
                cur.execute('select * from customer_transactions where account_number=%s', (acc_no,))
                trans = cur.fetchall()
                _customer_.bank_statement(trans)
                print()
                cur.execute('select balance from customer_details where account_number=%s', (acc_no,))
                balance = cur.fetchone()
                print('\t\t\t\t\t\tYour Current Balance Is: Rs.', balance[0], '/-')
            elif o1 == 6:
                choice = pymsgbox.confirm('Are you Sure You Want To Go back', 'Confirm', ["Yes", 'No'])
                if choice == 'Yes':
                    break
            else:
                pymsgbox.alert('Please Choose A Valid Service!', 'ALERT')

    # CUSTOMER LOGIN
    @staticmethod
    def customer_login():
        username = input('Username: ')
        password = input('Password: ')
        login = 0
    
        f = open('Python/Bank Management System/customerlogin.csv','r')
        r = csv.reader(f)

        for i in r:
            if username == i[3] and password == i[4]:
                login = 1
                comment = 'Welcome '+ i[2] + '!'
                pymsgbox.confirm(comment, 'Etihad National Bank', ["Enter"])
                f.close()
                return login, i

    # LOAN INFORMATION
    @staticmethod
    def loan_info(s):
        print('The Details Will Be Sent As An Email.')
        _loan_.sendmail(s)

        m = input('\n\t\t\t\t\tDo You Want To Calculate Your Monthly EMI(y/n): ')
        print()
        if m in 'yY':
            _loan_.calculate_emi()

    # WITHDRAWAL
    @staticmethod
    def withdraw(s):
        date = today.strftime("%y/%m/%d")

        acc_no = s[1]
        acc_pin = int(s[5])
        sub = int(input('Enter The Amount To Withdraw: Rs.'))

        print()
        ask_pin = int(input('Enter Your Pin: '))

        if ask_pin == acc_pin:
            cur.execute('select balance from customer_details where ACCOUNT_NUMBER=%s', (acc_no,))
            balance = cur.fetchall()

            total = int(balance[0][0]) - sub

            if total >= 0:
                cur.execute('update customer_details set balance=%s where ACCOUNT_NUMBER=%s', (total, acc_no))

                print()
                print('\t\t\t\t\t\tYour Cash Has Been Withdrawn Succesfully...')
                print()
                check = input('\t\t\t\t\tDo You Want To View Your Current Balance?(y/n): ')
                print()

                if check in 'yY':
                    print('\t\t\t\t\t\tYour Current Balance Is: Rs.', total, '/-')

                cur.execute('insert into customer_transactions values(%s,%s,%s,%s,%s)',(acc_no, s[2], '-' + str(sub), 'Withdrawal', date))

            else:
                print()
                print('\t\t\tYou Do Not Have The Required Balance To Withdraw The Entered Amount!')

        else:
            pymsgbox.alert('Incorrect PIN. Please Try Again!', 'ALERT')

        conn.commit()

    # DEPOSIT
    @staticmethod
    def deposit(s):
        date = today.strftime("%y/%m/%d")

        acc_no = s[1]
        acc_pin = int(s[5])
        add = int(input('Enter The Deposit Amount: Rs.'))

        print()
        ask_pin = int(input('Enter Your Pin: '))

        if ask_pin == acc_pin:
            cur.execute('select balance from customer_details where ACCOUNT_NUMBER=%s', (acc_no,))
            balance = cur.fetchall()

            total = int(balance[0][0]) + add
            cur.execute('update customer_details set balance=%s where ACCOUNT_NUMBER=%s', (total, acc_no))

            print()
            pymsgbox.alert('Your Cash Has Been Deposited Succesfully!', 'Etihad National Bank')
            print()
            check = input('\t\t\t\t\tDo You Want To View Your Current Balance?(y/n): ')
            print()

            if check in 'yY':
                print('\t\t\t\t\t\tYour Current Balance Is: Rs.', total, '/-')

            cur.execute('insert into customer_transactions values(%s,%s,%s,%s,%s)',(acc_no, s[2], '+' + str(add), 'Deposit', date))
            
        else:
            pymsgbox.alert('Incorrect PIN. Please Try Again!', 'ALERT')

        conn.commit()

    # BANK STATEMENT
    @staticmethod
    def bank_statement(s):
        print("Transactions:")
        print()
        print('\t\t\t' + '================================ BANK STATEMENT =================================')
        print()
        print('\t\t\t' + '-' * 81)
        print('\t\t\t' + '{:<15}'.format("ACCOUNT_NUMBER"), '{:<22}'.format("NAME"), '{:<10}'.format("AMOUNT"),
              '{:<20}'.format("TRANSACTION_TYPE"), '{:<15}'.format("DATE"))
        print('\t\t\t' + '-' * 81)

        for k in s:
            print('\t\t\t' + '{:<15}'.format(k[0]), '{:<22}'.format(k[1]), '{:<10}'.format(k[2]), '{:<20}'.format(k[3]),
                  '{:<15}'.format(str(k[4])))
            print()
            print('\t\t\t' + '-' * 81)

        print()
        print('\t\t\t' + '=================================================================================')