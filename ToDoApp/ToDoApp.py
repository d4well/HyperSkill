from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()

engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    user_input1 = input("Enter task\n")
    user_input2 = input("Enter deadline\n")
    new_row = Task(task=user_input1, deadline=datetime.strptime(user_input2, "%Y-%m-%d"))

    session.add(new_row)
    session.commit()
    print("The task has been added!")
    print()


def read_today():
    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline == today.date()).all()
    if rows:
        print(f"Today {rows[0].deadline.strftime('%#d %b')}")
        for num, row in enumerate(rows, start=1):
            print(f"{num}. {row.task}")
        print()
    else:
        print("Nothing to do!")
        print()


def read_day(date):
    rows = session.query(Task).filter(Task.deadline == date).all()
    if rows:
        print(f"{rows[0].deadline.strftime('%A %#d %b')}")
        for num, row in enumerate(rows, start=1):
            print(f"{num}. {row.task}")
        print()
    else:
        print(f"{date.strftime('%A %#d %b')}:")
        print("Nothing to do!")
        print()


def read_week():
    today = datetime.today()
    week = [today+timedelta(day) for day in range(0, 7)]
    for date in week:
        read_day(date.date())


def read_missed_tasks():
    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline < today.date()).order_by(Task.deadline).all()
    if rows:
        print("Missed tasks:")
        for num, row in enumerate(rows, start=1):
            print(f"{num}. {row.task}. {row.deadline:%#d} {row.deadline:%b}")
        print()
    else:
        print("Nothing is missed!")
        print()


def read_tasks(delete=None):
    rows = session.query(Task).order_by(Task.deadline).all()
    if rows:
        if delete is None:
            print("All tasks:")
        for num, row in enumerate(rows, start=1):
            print(f"{num}. {row.task}. {row.deadline:%#d} {row.deadline:%b}")
        print()
    else:
        print("Nothing to do!")
    return rows


def delete_task():
    print("Choose the number of the task you want to delete:")
    rows = read_tasks(True)
    user_input = input("")
    if rows:
        row_to_delete = rows[int(user_input) - 1]
        session.delete(row_to_delete)
        session.commit()
        print("The task has been deleted!")
    else:
        print("Nothing to delete")


while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    user_input = input()
    if user_input == "1":
        read_today()
    elif user_input == "2":
        read_week()
    elif user_input == "3":
        read_tasks()
    elif user_input == "4":
        read_missed_tasks()
    elif user_input == "5":
        add_task()
    elif user_input == "6":
        delete_task()
    elif user_input == "0":
        print("Bye!")
        break
    else:
        continue

