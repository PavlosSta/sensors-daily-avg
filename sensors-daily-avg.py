import csv
import sys

with open(sys.argv[1], mode='r') as csv_file:
    reader = csv.reader(csv_file)
    line_count = 0
    count = 0
    SumTemp = 0
    SumHumid = 0
    for row in reader:
        datetime = row[0]
        datetimeT = datetime.split()
        time = datetimeT[0]
        date = datetimeT[1]
        temp = float(row[1])
        humid = float(row[2])
        if (line_count == 0):
            oldDate = date
            count = 1
            SumTemp = temp
            SumHumid = humid
        else:
            if (date == oldDate):
                count = count + 1
                SumTemp += temp
                SumHumid += humid
            else:
                AvgTemp = SumTemp / count
                AvgHumid = SumHumid / count
                print (str(date) + " " + str(AvgTemp) + " " + str(AvgHumid))
                count = 1
                oldDate = date
                SumTemp = temp
                SumHumid = humid
        line_count += 1
    AvgTemp = SumTemp / count
    AvgHumid = SumHumid / count
    print (str(date) + " " + str(AvgTemp) + " " + str(AvgHumid))
