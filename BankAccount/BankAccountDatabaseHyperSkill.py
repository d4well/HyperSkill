import random
import sqlite3
import os

if not os.path.isfile('./card.s3db'):
    db_bank = sqlite3.connect('./card.s3db')
    db_cursor = db_bank.cursor()
    db_cursor.execute('''CREATE TABLE card (
                        id INTEGER,
                        number TEXT,
                        pin TEXT,
                        balance INTEGER DEFAULT 0
                        )''')
    db_bank.commit()

elif os.path.isfile('./card.s3db'):
    db_bank = sqlite3.connect('./card.s3db')
    db_cursor = db_bank.cursor()


class BankAccount:
    accounts = {}
    acc_objs = []
    db_cursor.execute("SELECT MAX(id) FROM card")
    id_num = db_cursor.fetchone()[0]

    def __init__(self):
        self.card_number = self.account_number_generator()
        self.pin = self.pin_generator()
        self.balance = 0
        if BankAccount.id_num is None:
            BankAccount.id_num = 0
        else:
            BankAccount.id_num += 1
        self.id = BankAccount.id_num

    @staticmethod
    def account_number_generator():
        def generator():
            first_six = '400000'
            last_ten = (random.choice(list(range(0, 9))) for i in range(9))
            acc_num = [int(i) for i in first_six] + list(last_ten)
            return acc_num

        def luhns(acc_number):
            odds_mul2 = [j * 2 if i % 2 != 0 else j for i, j in enumerate(acc_number, 1)]
            sub9 = [i - 9 if i > 9 else i for i in odds_mul2]
            last_digit = 10 - (sum(sub9) % 10)
            if last_digit == 10:
                acc_number.append(0)
            else:
                acc_number.append(last_digit)
            acc_str = (str(i) for i in acc_number)
            luhns_acc_str = ''.join(acc_str)
            return luhns_acc_str

        while True:
            acc_number = generator()
            luhns_acc = luhns(acc_number)
            if luhns_acc not in BankAccount.accounts:
                BankAccount.accounts[luhns_acc] = None
                break
            else:
                continue
        return luhns_acc

    def pin_generator(self):
        pin_number = (str(random.choice(list(range(0, 9)))) for i in range(4))
        pin_num = "".join(pin_number)
        BankAccount.accounts[self.card_number] = pin_num
        return pin_num

    def add_to_db(self):
        db_cursor.execute(
            f"""INSERT INTO card (id, number, pin, balance) VALUES ({self.id}, {self.card_number},\
            "{self.pin}", {self.balance})""")
        db_bank.commit()


def luhns_check(acc_number):
    acc_number = [int(i) for i in str(acc_number)]
    last = acc_number.pop()
    odds_mul2 = [j * 2 if i % 2 != 0 else j for i, j in enumerate(acc_number, 1)]
    sub9 = [i - 9 if i > 9 else i for i in odds_mul2]
    last_digit = 10 - (sum(sub9) % 10)
    return last_digit == last


created_accounts = []
i = True
while i:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_input = int(input())
    if user_input == 1:
        print("Your card has been created")
        a = BankAccount()
        a.add_to_db()
        print("Your card number:")
        print(f"{a.card_number}")
        print("Your card PIN:")
        print(f"{a.pin}")

    elif user_input == 2:
        print("Enter your card number:")
        user_input2 = input()
        print("Enter your PIN:")
        user_input3 = input()
        db_cursor.execute("SELECT number FROM card")
        card_nums = [i[0] for i in db_cursor.fetchall()]
        if user_input2 in card_nums:
            db_cursor.execute(f"""SELECT pin FROM card WHERE number={user_input2}""")
            card_pin = db_cursor.fetchone()[0]
            db_cursor.execute(f"""SELECT number FROM card WHERE number={user_input2}""")
            card_num = db_cursor.fetchone()[0]
        if user_input2 in card_nums and card_pin == user_input3:
            print("You have successfully logged in!")
            while True:
                print("1. Balance")
                print("2. Add income")
                print("3. Do transfer")
                print("4. Close account")
                print("5. Log out")
                print("0. Exit")
                user_input4 = int(input())
                if user_input4 == 1:
                    db_cursor.execute(f"""SELECT balance FROM card WHERE number={user_input2}""")
                    balance = db_cursor.fetchone()[0]
                    print(f"Balance is: {balance} $")
                    continue
                elif user_input4 == 2:
                    user_input5 = int(input("Please enter value to add: "))
                    db_cursor.execute(
                        f"""UPDATE card SET balance = balance + {user_input5} WHERE number={card_num}""")
                    db_bank.commit()
                    print("Income was added!")
                    continue
                elif user_input4 == 3:
                    user_input7 = input("Please enter account number to transfer ")
                    if user_input7 == user_input2:
                        print("You can't transfer money to the same account!")
                        continue
                    elif user_input7 not in card_nums and luhns_check(user_input7):
                        print("Such a card does not exist.")
                        continue
                    elif not luhns_check(user_input7):
                        print("Probably you made a mistake in the card number. Please try again!")
                        continue
                    else:
                        print("Everything fine")

                    db_cursor.execute(f"""SELECT balance FROM card WHERE number={user_input2}""")
                    balance = db_cursor.fetchone()[0]
                    user_input6 = int(input("How much money would you like to transfer? "))

                    if user_input6 > balance:
                        print("Not enough money!")
                        continue

                    else:
                        db_cursor.execute(
                            f"""UPDATE card SET balance = balance - {user_input6} WHERE number={user_input2}""")
                        db_bank.commit()
                        db_cursor.execute(
                            f"""UPDATE card SET balance = balance + {user_input6} WHERE number={user_input7}""")
                        db_bank.commit()
                        print("Transaction finished")

                elif user_input4 == 4:
                    db_cursor.execute(f"""DELETE FROM card WHERE number={user_input2}""")
                    db_bank.commit()
                    print("Your account has been deleted")
                    break
                elif user_input4 == 5:
                    print("You have successfully logged out!")
                    break
                elif user_input4 == 0:
                    i = False
                    print("Bye!")
                    break
        else:
            print("Wrong card number or PIN!")
            continue
    elif user_input == 0:
        print("Bye!")
        break
    else:
        continue


