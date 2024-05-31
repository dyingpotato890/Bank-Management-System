import smtplib
from email.message import EmailMessage
import pymsgbox
import mysql.connector as mysql

conn = mysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='bank_management_system',
                     charset='utf8')
cur = conn.cursor()

class _loan_:
    #SEND EMAIL
    @staticmethod
    def sendmail(s):
        main = EmailMessage()

        cur.execute('select email_id from customer_details where account_number=%s', (s[1],))
        user_email = cur.fetchone()[0]

        try:
            main['Subject'] = 'Loan Information'
            main['From'] = 'Etihad Bank'
            main['To'] = str(user_email)

            with open('Python/Bank Management System/Source/EmailTemplate.txt', 'r') as f:
                content = f.read()
                main.set_content(content)

            with open('Python/Bank Management System/Source/Loan Information.docx', 'rb') as loan:
                file_data = loan.read()
                file_name = loan.name
                main.add_attachment(file_data, maintype='applictaion', subtype='docx', filename=file_name)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('etihadbank.noreply@gmail.com', 'etihadbankpassword')

            server.send_message(main)
            print('\t\tThe Email Has Been Sent. Please Check Your Spam Messages If The Message Was Not Found In The Main Inbox.\n')
            server.quit()

        except smtplib.SMTPAuthenticationError:
            pymsgbox.alert('Failed to authenticate with the SMTP server. Please Try Again Later', 'SMTP Authentication Error')
        except FileNotFoundError:
            pymsgbox.alert('The file "EmailTemplate.txt" or "Loan Information.docx" was not found. Please ensure these files exist.', 'File Not Found Error')
        except Exception as e:
            pymsgbox.alert(f'An error occurred: {e}', 'Error')

    # CALCULATE EMI
    @staticmethod
    def calculate_emi():
        print()
        print("\t\t\t\t    =========================================================")
        print('\t\t\t\t    ~~~~~~~~~~~~~~~~~~~~~~~ LOAN TYPE ~~~~~~~~~~~~~~~~~~~~~~~')
        print("\t\t\t\t    =========================================================")
        print()
        print('\t\t\t\t\t              1. Personal Loans')
        print('\t\t\t\t\t              2. Car Loans')
        print('\t\t\t\t\t              3. Two-Wheeler Loans')
        print('\t\t\t\t\t              4. Commercial Vehicle Loans')
        print('\t\t\t\t\t              5. Housing Loans')
        print('\t\t\t\t\t              6. Educational Loans')
        print()
        print("\t\t\t\t    =========================================================")
        print()

        loan_type = int(input('Enter The Loan Type: '))
        print()
        p = float(input("Enter principal amount: "))
        print()

        if loan_type == 1:
            y = int(input('Enter The Time Period(1/3): '))

            if y == 1:
                n = 12
                R = 8
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            elif y == 3:
                n = 36
                R = 14.96
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            else:
                pymsgbox.alert('Please Enter A Valid Time Period!', 'ALERT')
                
        elif loan_type == 2:
            n = 48
            R = 8.76
            r = R / (12 * 100)
            emi = p*r*((1+r)**n)/((1+r)**n -1)
            print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
            print()
            
        elif loan_type == 3:
            y = int(input('Enter The Time Period(1/3): '))

            if y == 1:
                n = 12
                R = 6
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            elif y == 3:
                n = 36
                R = 8
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            else:
                pymsgbox.alert('Please Enter A Valid Time Period!', 'ALERT')
                
        elif loan_type == 4:
            n = 48
            R = 8.76
            r = R / (12 * 100)
            emi = p*r*((1+r)**n)/((1+r)**n -1)
            print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
            print()
            
        elif loan_type == 5:
            y = int(input('Enter The Time Period(7/10/15): '))

            if y == 7:
                n = 84
                R = 7
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            elif y == 10:
                n = 120
                R = 9.33
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            elif y == 15:
                n = 180
                R = 12
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            else:
                pymsgbox.alert('Please Enter A Valid Time Period!', 'ALERT')
                
        elif loan_type == 6:
            y = int(input('Enter The Time Period(6/10): '))

            if y == 6:
                n = 72
                R = 9
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            elif y == 10:
                n = 120
                R = 11
                r = R / (12 * 100)
                emi = p*r*((1+r)**n)/((1+r)**n -1)
                print('\t\t\t\t\tYour Approximate Monthly EMI Is: Rs.', round(emi, 2))
                print()
            else:
                pymsgbox.alert('Please Enter A Valid Time Period!', 'ALERT')