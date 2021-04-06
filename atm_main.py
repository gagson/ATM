import sqlite3 as sq
import datetime as dt
import json

conn = sq.connect("ATM.db3")
cursor = conn.cursor()

count = 0
# while loop checks existance of the enterd username
while True:
    exit = input("+------------------------------------------------+\n"
                + "| ATM-Manager Simulator using Python and SQLite  |\n"
                + "|         By Gagson Lee (20160) Apr, 2021        |\n"
                + "|             Press ENTER to contiue             |\n"
                + "|               Type exit to quit                |\n"
                + "+------------------------------------------------+\n")

    if exit == "exit":
        break
    else:
        cursor.execute("select id, name, pin, balance, type, status from account")
        id = str(input("Type your ID:\n"))
        rows = cursor.fetchall()
        for row in rows:
            ac_id = row[0]
            ac_name = row[1]
            ac_pin = row[2]
            ac_balance = row[3]
            ac_type = row[4]
            ac_status = row[5]

            if id == ac_id:
                print(ac_pin)
                pw = str(input("Type your PIN:\n"))
                if pw == ac_pin:
                    print("Successful Login.")
                    if ac_type == "Client":
                        while True:
                            select = input(""
                                                + "+-----------------------+\n"
                                                + "|      Command Menu     |\n"
                                                + "+-----------------------+\n"
                                                + "|1 --> Withdraw         |\n"
                                                + "|2 --> Deposit          |\n"
                                                + "|3 --> Transfer         |\n"
                                                + "|4 --> Check Balance    |\n"
                                                + "|5 --> List transactions|\n"
                                                + "|6 --> Finish           |\n"
                                                + "+-----------------------+\n")
                            if int(select) == 6:
                                print("Exit")
                                break
                            elif int(select) == 1:
                                print("Amount to be withdrawed:")
                                print("-----------------------")
                                amount = str(input(""))
                                balance = cursor.execute("select balance from account where id = \'" + ac_id +"\'")
                                for b in balance:
                                    if b[0] < int(amount):
                                        print("You do not have enough amount. Please try again.")
                                        input("Press enter to continue.")
                                else:
                                    conn.execute("update account set balance = balance - " + amount + " where id = \'" + ac_id +"\'")
                                    conn.commit()
                                    print("Your Balance:")
                                    print("-------------")
                                    balance = cursor.execute("select balance from account where id = \'" + ac_id +"\'")
                                    for b in balance:
                                        print(b[0])
                                    conn.execute("insert into transactions (account_id, amount, type) values (\'" + ac_id +"\', " + amount +", \'Withdraw\')")
                                    conn.commit()                                    
                                input("Press enter to continue.")
                            elif int(select) == 2:
                                print("Amount to be deposited:")
                                print("-----------------------")
                                amount = str(input(""))
                                if int(amount) < 0:
                                    print("Please enter the right amount.")
                                else:
                                    conn.execute("update account set balance = balance + " + amount + " where id = \'" + ac_id +"\'")
                                    conn.commit()
                                    print("Your Balance:")
                                    print("-------------")
                                    balance = cursor.execute("select balance from account where id = \'" + ac_id +"\'")
                                    for b in balance:
                                        print(b[0])
                                conn.execute("insert into transactions (account_id, amount, type) values (\'" + ac_id +"\', " + amount +", \'Deposit\')")
                                conn.commit()
                                input("Press enter to continue.")
                            
                            elif int(select) == 3:
                                print("Payee ID:")
                                print("---------")
                                payee_id = str(input(""))
                                print("Amount to be transferred:")
                                print("-------------------------")  
                                amount = str(input(""))                          
                                conn.execute("update account set balance = balance + " + amount + " where id = \'" + payee_id +"\'")
                                conn.execute("update account set balance = balance - " + amount + " where id = \'" + ac_id +"\'")
                                conn.execute("insert into transactions (account_id, amount, type) values (\'" + ac_id +"\', " + amount +", \'Transfer\')")
                                conn.execute("insert into transactions (account_id, amount, type) values (\'" + payee_id +"\', " + amount +", \'Receive\')")
                                conn.commit()
                                print("Your Remaining Balance:")
                                print("-----------------------")
                                balance = cursor.execute("select balance from account where id = \'" + ac_id +"\'")
                                for b in balance:
                                    print(b[0])
                                    input("Press enter to continue.")

                            elif int(select) == 4:
                                print("Your Balance:")
                                print("-------------")                            
                                print(ac_balance)
                                input("Press enter to continue.")

                            elif int(select) == 5:
                                print("Your Transaction Records:")
                                print("-------------------------")
                                cursor.execute("select date, type, amount from transactions where account_id = \'" + ac_id +"\'")
                                print("(---------DATE--------, ---TYPE---, AMOUNT)")
                                transactions_list = cursor.fetchall()                                
                                for t in transactions_list:
                                    print(t)
                                input("Press enter to continue.")
                        break
                    if ac_type == "Admin":
                        while True:
                            select = input(""
                                                + "+-----------------------+\n"
                                                + "|   Admin Command Menu  |\n"
                                                + "+-----------------------+\n"
                                                + "|1 --> Add account      |\n"
                                                + "|2 --> Delete account   |\n"
                                                + "|3 --> Show account list|\n"
                                                + "|4 --> Dump into a flie |\n"
                                                + "|5 --> Finish           |\n"
                                                + "+-----------------------+\n")
                            if int(select) == 5:
                                print("Exit")
                                break
                            elif int(select) == 1:
                                print("Enter new account id:")
                                print("---------------------")
                                add_id = str(input(""))
                                print("Enter username for the new account:")
                                print("-----------------------------------")
                                add_name = str(input(""))
                                print("Enter PIN for the new account:")
                                print("------------------------------")
                                add_pin = str(input(""))
                                print("'Client' or 'Admin'?")
                                print("------------------------------")
                                add_type = str(input(""))
                                conn.execute("insert into account (id, name, pin, type) values (\'" + add_id + "\', \'" + add_name + "\', \'" + add_pin + "\', \'" + add_type + "\')")
                                conn.commit()
                                print("Success!")
                                input("Press enter to continue.")
                            elif int(select) == 2:
                                print("Account id to be deleted:")
                                print("---------------------")
                                del_id = str(input(""))
                                conn.execute("delete from account where id = \'" + del_id +"\'")
                                conn.commit()
                                print("Success!")
                                input("Press enter to continue.")
                            elif int(select) == 3:
                                cursor.execute("select id, name, balance, status from account")
                                ac_list = cursor.fetchall()
                                print("(ID, NAME, BALANCE, STATUS)")
                                for ac in ac_list:
                                    print(ac)
                                input("Press enter to continue.")
                            elif int(select) == 4:
                                cursor.execute("select id, name, balance, status from account")
                                ac_list = cursor.fetchall()
                                print("Enter the account list filename (.json or .txt):")
                                print("------------------------------------------------")
                                filename_ac = str(input(""))
                                with open(filename_ac, 'w') as f: 
                                    json.dump(ac_list, f)
                                    print("Success!")
                                
                                cursor.execute("select account_id, amount, type, date from transactions")
                                transactions_list = cursor.fetchall()
                                print("Enter the transactions list filename (.json or .txt):")
                                print("-----------------------------------------------------")
                                filename_transactions = str(input(""))
                                with open(filename_transactions, 'w') as f: 
                                    json.dump(transactions_list, f)
                                    print("Success!")
                                input("Press enter to continue.")
                        break
                else:
                    print("This account does not exist or PIN was wrong. Please check and try again.")
                    break
        conn.close()
    break





        

        # (""
        #     + "+-----------------------+----------+---------------------+\n"
        #     + "|       Datetime        |   Type   |        Amount       |\n"
        #     + "+-----------------------+----------+---------------------+\n")