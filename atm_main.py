import sqlite3 as sq
import datetime as dt

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
                        select = input(""
                                            + "+-----------------------+\n"
                                            + "|      command menu     |\n"
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
                        elif int(select) == 2:
                            print("Amount to be deposited:")
                            print("-----------------------")
                            amount = str(input(""))
                            conn.execute("update account set balance = balance + " + amount + " where id = \'" + ac_id +"\'")
                            conn.commit()
                            print("Your Balance:")
                            print("-------------")
                            cursor.execute("select balance from account where id = \'" + ac_id +"\'")
                            print(cursor.fetchone())
                            break

                        elif int(select) == 4:
                            print("Your Balance:")
                            print("-------------")                            
                            print(ac_balance)
                        break
                    if ac_type == "Admin":
                        select = input(""
                                            + "+-----------------------+\n"
                                            + "|   Admin command menu  |\n"
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
                        elif int(select) == 3:
                            cursor.execute("select id, name, balance, status from account")
                            ac_list = cursor.fetchall()
                            print("(ID, NAME, BALANCE, STATUS)")
                            for ac in ac_list:
                                print(ac)
                        break
                        
                else:
                    print("This account does not exist or PIN was wrong. Please check and try again.")
                    break
        conn.close()
        break





        

        (""
            + "+-----------------------+----------+---------------------+\n"
            + "|       Datetime        |   Type   |        Amount       |\n"
            + "+-----------------------+----------+---------------------+\n")