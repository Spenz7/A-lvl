def openfile(filename):
    deviceFile = open(filename,'r')
    deviceList = []
    for line in deviceFile:
        deviceList.append(line[:-1].split(','))
    print(deviceList)
    deviceFile.close()
    return deviceList


Monitors = openfile('Monitors.txt')
Laptops = openfile('Laptops.txt')
Printers = openfile('Printers.txt')

import sqlite3
db = sqlite3.connect('equipment.db')
for line in Monitors:
    db.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateofPurchase, WrittenOff) \
Values(?,'Monitor',?,?,?,?)", (line[0],line[1],line[2],line[3],line[4]))
    db.execute("Insert into Monitor(SerialNumber, DateCleaned) Values(?,?)",(line[0],line[5]))

for line in Laptops:
    db.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateofPurchase, WrittenOff) \
Values(?,'Laptop',?,?,?,?)", (line[0],line[1],line[2],line[3],line[4]))
    db.execute("Insert into Laptop(SerialNumber, WeightKg) Values(?,?)",(line[0],line[5]))

for line in Printers:
    db.execute("INSERT INTO Device(SerialNumber, Type, Model, Location, DateofPurchase, WrittenOff) \
Values(?,'Printer',?,?,?,?)", (line[0],line[1],line[2],line[3],line[4]))
    db.execute("Insert into Printer(SerialNumber, Toner, DateChanged) Values(?,?,?)",(line[0],line[5],line[6]))

db.commit()
db.close()

               
