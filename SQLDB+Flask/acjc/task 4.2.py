def openfile(filename):
    deviceFile = open(filename,'r')
    deviceList = []
    for line in deviceFile:
        deviceList.append(line[:-1].split(','))
    print(deviceList)
    #RMB CLOSE FILE
    deviceFile.close()
    return deviceList


sales = openfile('SALES.txt')
tech_support = openfile('TECH_SUPPORT.txt')

import sqlite3
db = sqlite3.connect('records.db')
for line in sales:
   
    db.execute("INSERT INTO Employee(Employee_ID, Employee_name, Job_type, Date_of_Employment, Service_status)\
    Values(?,?,?,?,?)", (int(line[0]),line[1],'Sales',line[2],line[3]))
    db.execute("Insert into Sales(Employee_ID,Total_Sales) Values(?,?)",(int(line[0]),int(line[4])))

for line in tech_support:
    db.execute("INSERT INTO Employee(Employee_ID, Employee_name, Job_type, Date_of_Employment, Service_status) \
    Values(?,?,?,?,?)", (line[0],line[1],'Tech_support',line[2],line[3]))
    db.execute("Insert into Tech_support(Employee_ID, Bugs_resolved) Values(?,?)",(int(line[0]),int(line[4])))

#RMB TO COMMIT AND CLOSE DB
db.commit()
db.close()

