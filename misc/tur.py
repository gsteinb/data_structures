from datetime import date
from datetime import datetime

"""
Program that takes the new Transit Usage Report from http://www.prestocard.ca
as a csv file and creates a new file that contains all the monthly totals and
a cumulative yearly total. The file used is a csv file downloaded from 
prestocard.ca

"""


FILE = "TUR_2017.csv"

months = {1:"January", 2:"Febraury", 3:"March", 4:"April", 5:"May", 6:"June",
          7:"July", 8:"August", 9:"September", 10:"October",
          11:"November", 12:"December"}


if __name__ == "__main__":
    month = 1
    file = open(FILE, "r")
    result_file = open("TUR_2017.txt", 'w')
    result_file.write("Transit Usage Report 2017 Breakdown\n\n")
    result_file.write(months[month] + "\n")
    title = file.readline()
    tsum = 0
    msum = 0
    for line in file:
        # get info from the csv
        items = line[:-1].split(',')
        date = items[0].split(' ')[0][1:]
        date = datetime.strptime(date, "%m/%d/%Y").date()
        
        # check if the date is the same else write the month and amount
        if date.month != month:
            month = date.month
            result_file.write("${}\n\n".format(round(msum, 2)))
            result_file.write(months[month] + '\n')
            tsum += msum
            msum = 0
        
        # increase the sum
        amount = items[-1]
        if amount[1] == "(":
            amount = 0 - float(amount[3:-2])
        else:
            amount = float(amount[2:-1])
        msum -= amount
    tsum += msum
    # the december amount
    result_file.write("${}\n\n".format(round(msum, 2)))
    result_file.write("Annual Total: ${}\n".format(round(tsum, 2)))
    file.close()
    result_file.close()
