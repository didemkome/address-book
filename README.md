# Address Book

Simple Python 3 address book application using a Sqlite database.

## Overview

This project is a simple address book application written in Python.

**What can it do?**

- Add a person to the address book

```
    def add_person(self, full_name = '', phone_number='', email_address=''):

        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor()
        full_name = input('Enter Full Name: ')
        phone_number = input('Enter Phone Number: ')
        email_address = input('Enter E-mail Address: ')
        connect.execute('INSERT INTO people(full_name, phone_number, email_address) VALUES(?,?,?)', (full_name, phone_number, email_address))
        db.commit()
        connect.close()
```
- List people in the address book

```
    def list_person(self):
        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor() # create a new cursor
        connect.execute('SELECT * FROM people')
        records = connect.fetchall() #to fetch all tasks from the tasks table , return a list
        if records:
            print("{:<15} {:<15} {:<15} {:<15}".format('ID' , 'Full Name', 'Phone Number', 'E-mail Address'))
            for row in records:
                print ('{:<15} {:<15} {:<15} {:<15}'.format(row[0], row[1], row[2], row[3]))
        connect.close()
        return records
```
- Delete a person from the address book 

```
    def remove_person(self, id = ''):
        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor()
        id = input('Enter people id to delete: ')
        connect.execute('DELETE FROM people where id=?', (id,))
        db.commit() # Commit the changes to the database
        connect.close()
```
## License

This project is licensed under the MIT License (https://rem.mit-license.org/).
