# Spaced repetition for students
#### Video Demo: https://www.youtube.com/watch?v=EO2UxflEf0s
#### Description: Organizes dates for optimal active recall for students, with options to output all dates or the topics for the current date.

```
from datetime import datetime, timedelta, date
from tabulate import tabulate
import csv
import sys
```
Datetime library:
   - `datetime`  To get the current day of the week
   - `timedelta` To add days to current day without needing to think about days in a current month
   - `date` Get current date fast

Tabulate:
   - This outputs dates and tasks in tables

CSV:
   - This allows us to easily write into csv files

SYS:
   - Allows us to exit programs fast

## Main

```
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
```
While loop:
   - This asks a user of a choice from 1 to 4 with message `"Add(1), table of tasks(2), daily tasks(3), exit(4): "`
   And executes functions accordingly
   - If 4 is selected `sys.exit()` exits the program

## get_day
```
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
```
Converts the day number to words with a dictionary e.g. `get_day(0)` returns `Monday`.

# add_topic

## get_time
```
def get_time():
    day = time.weekday()
    today = [get_day(day), str(date.today())]
    return today
```
- `day = time.weekday()` returns a integer with 0 being Monday and 6 being Sunday
- Integer is converted to the word version of the weekday with `get_day(day)`
- Result of word version and the string of the current date is both added to list today and `today` is returned

## new_topic
```
def new_topic(subject_name, topic_name):
    names = []
    names.append(subject_name)
    names.append(topic_name)
    return names
```
Takes parameters and adds to list then returns

### get_subject
```
def get_subject():
    subject_name = input("Subject name: ")
    return subject_name
```
returns the input of subject name

# get_topic
```
def get_topic():
    topic_name = input("Topic name: ")
    return topic_name
```

### spc_repetition
```
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
```
 - time gets the second item in the topic info list, which is the date formatted in a string
 - Then the date is formatted as year, month, day
 - Variable created for each time a repetition is needed for 1, 7, 16, 35 days
 - `timedelta` adds the corresponding days to current times, result is saved in the `rep` variables
 - Dates are then formatted in Y-M-D again and all repetition dates are returned in a list.

 ### add_topic()
 ```
 def add_topic(names, rep_dates, date_set):
    with open("date.csv", "a") as csv:
        csv.write("\n")
        for i in names:
            csv.write(i+ ",")
        for p in date_set:
            csv.write(p+ ",")
        for d in rep_dates:
            csv.write(d+ ",")

 ```
 Takes 3 parameters:
   - `names` - This should be a list in the form of `[the subject name, the topic name]`
   - `rep_dates` - This value is also a list in which there are 4 items representing each optimal date to go over a topic added
   - `date_set` - This should also be a list in the form of `[Dayname, date as a string]`

# get_table
```
def get_table():
    with open("date.csv") as f:
        alldata = list(csv.reader(f))
        headers = ["Subject", "Topic", "Dayset", "Dateset", "Rep1", "Rep2", "Rep3", "Rep4"]
        print(tabulate(alldata, headers=headers, tablefmt="grid"))
```
- This returns a table formatted with tabulate with all data currently inside the csv file

## format daily
```
def formatdaily(data, date):
    lst=[]
    for r in range(len(data)):
        for i in data[r]:
            currentlst = data[r]
            name = currentlst[1]
            if i == date:
                lst.append(name)
    return lst
```
This takes in 2 parameters:
   - `data` This is a list of all lines in csv
   - `date` This is the current date in form 'YYYY-MM-DD'

- Loops through the data list
   - Each loop it loops through each sublist to see if the current date matches any date in the list
   - If the a date matches current date, the topic name is added to list
- List is returned

## dailytasks
```
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
```
- Getting data from the csv file and current date
- Put into the function `formatdaily()`
- Tabulate table with header `Today`, and all the tasks printed below it.

