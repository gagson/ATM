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
                    break
                else:
                    print("This account does not exist or PIN was wrong. Please check and try again.")
                    break





        (""
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

        (""
            + "+-----------------------+----------+---------------------+\n"
            + "|       Datetime        |   Type   |        Amount       |\n"
            + "+-----------------------+----------+---------------------+\n")