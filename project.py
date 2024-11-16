from datetime import datetime, timedelta, date
from tabulate import tabulate
import csv
import sys


time = datetime.now()

def main(): 
    actions = 1
    while actions <=  4 and actions >= 1: 
        actions = int(input("Add(1), table of tasks(2), daily tasks(3), exit(4): "))
        if actions == 1:
            add_topic(new_topic(get_subject(), get_topic()), spc_repetition(), get_time())
        elif actions == 2:
            get_table()
        elif actions == 3:
            dailytasks()
        elif actions == 4:
            sys.exit()

def get_time():
    day = time.weekday()
    today = [get_day(day), str(date.today())]
    return today

def get_day(int):
    days_index = {  
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
            }
    return days_index[int]

def new_topic(subject_name, topic_name):
    names = []
    names.append(subject_name)
    names.append(topic_name)
    return names


def get_subject():
    subject_name = input("Subject name: ")
    return subject_name

def get_topic():
    topic_name = input("Topic name: ")
    return topic_name

def spc_repetition():
    topic_info = get_time()
    time = topic_info[1]
    time = datetime.strptime(time, "%Y-%m-%d")
    rep1 = time + timedelta(days=1) 
    rep2 = time + timedelta(days=7)
    rep3 = time + timedelta(days=16)
    rep4 = time + timedelta(days=35)
    formatrep1 = rep1.strftime('%Y-%m-%d')
    formatrep2 = rep2.strftime('%Y-%m-%d')
    formatrep3 = rep3.strftime('%Y-%m-%d')
    formatrep4 = rep4.strftime('%Y-%m-%d')
    repeated = [formatrep1, formatrep2, formatrep3, formatrep4]
    return repeated
    

def add_topic(names, rep_dates, date_set):
    with open("date.csv", "a") as csv:
        csv.write("\n")
        for i in names:
            csv.write(i+ ",")
        for p in date_set:
            csv.write(p+ ",")
        for d in rep_dates:
            csv.write(d+ ",")
        

def get_table():
    with open("date.csv") as f:
        alldata = list(csv.reader(f))
        headers = ["Subject", "Topic", "Dayset", "Dateset", "Rep1", "Rep2", "Rep3", "Rep4"]
        print(tabulate(alldata, headers=headers, tablefmt="grid"))
    
def formatdaily(data, date):
    lst=[]
    for r in range(len(data)):
        for i in data[r]:
            currentlst = data[r]
            name = currentlst[1]
            if i == date:
                lst.append(name)
    return lst

def dailytasks():
    today = get_time()
    date = today[1]
    with open("date.csv") as f:
        data = list(csv.reader(f))
    lst = formatdaily(data,date)
    headers = ["Today"]
    tasks = []
    for i in lst:
        newlst = [i]
        tasks.append(newlst)
    print(tabulate(tasks, headers, tablefmt="grid"))



if __name__ == "__main__":
    main()


