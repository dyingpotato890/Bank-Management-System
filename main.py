import mysql.connector as mysql
import time
import pymsgbox
from datetime import date

from customer import _customer_
from admin import _admin_

today = date.today()

conn = mysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='bank_management_system',
                     charset='utf8')
cur = conn.cursor()

if __name__ == "__main__":
    print("\t\t\t\t\t   Welcome To Etihad Banking Server!\n\n")
    print()

    print('\t\t\t\t\t   Please Wait While We Load Our Services', end='')
    for i in range(0, 6):
        time.sleep(0.5)
        print('.', end='')

    while True:
        print('\n\n\t\t\t\t\t    =========================================')
        print('\t\t\t\t\t    ~~~~~~~~~~~~~~~~~ LOGIN ~~~~~~~~~~~~~~~~~')
        print('\t\t\t\t\t    =========================================\n')
        print('\t\t\t\t\t\t        1.Admin Login')
        print('\t\t\t\t\t\t        2.Customer Login')
        print('\t\t\t\t\t\t        3.Exit Application\n')
        print('\t\t\t\t\t    =========================================\n')

        o = int(input('Enter Your Option: '))
        print()

        if o==1:
            login_value = _admin_.admin_login()
            if login_value==1:
                _admin_.admin()
            else:
                pymsgbox.alert('The Username Or Password You Have Entered Is Incorrect. Please Try Again.', 'ALERT')
        elif o==2:
            login_value = _customer_.customer_login()
            if login_value[0]==1:
                _customer_.customer(login_value[1])
            else:
                pymsgbox.alert('The Username Or Password You Have Entered Is Incorrect. Please Try Again.', 'ALERT')            
        elif o==3:
            choice = pymsgbox.confirm('Are you Sure You Want To Exit', 'Confirm', ["Yes", 'No'])
            if choice=='Yes':
                pymsgbox.alert('Thank You For Using Our Application!', 'Etihad National Bank')
                print('-'*129)
                break
        else:
            pymsgbox.alert('Please Enter A Valid Option!', 'ALERT')