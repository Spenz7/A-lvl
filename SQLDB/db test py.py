import sqlite3
#connect and store in a variable
db = sqlite3.connect('test.db')
#db.execute('Create table book' +'(ID INTEGER, Title)')
#if u db.rollback() here doesn't work cuz they try to create table then ctrl z
#but can't work cuz u can't create another same table in the first place,
#so use # instead so it won't run the code at all

#i.e 123 is integer cuz u need follow data type
db.execute("Insert into book(id,title) values(123,'Harry Potter')")
db.rollback()
#insertbookid = input('Enter book id to insert')
#db.execute("Insert into book(id) values(?)",(insertbookid,))
#deletebookid = input('Enter book id to delete')
#db.execute("Delete from book where id = ?",(deletebookid,))
#db.commit()
#imagine cursor as mouse starting at first row
cursor = db.execute('Select id,title from book')
print(cursor)
for row in cursor:
    print(row)
    print(row[1])

    



#rmb to close
db.close()
