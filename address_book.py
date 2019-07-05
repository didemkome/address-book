import sqlite3

'''
add : Add new contact
list: List contacts
remove: Delete contact
q, quit, exit: Exit

'''

VERSION = '0.1.1'
VALİD_COMMANDS = ['add', 'remove', 'list']
DATABASE_FİLE = 'addressbook.db'

class AddressBookDatabase:

    def create_table(self, DATABASE_FİLE):
        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor()
        connect.execute("CREATE TABLE IF NOT EXISTS people( id INTEGER PRIMARY KEY, full_name, phone_number, email_address)")
        db.commit()
        connect.close()
    
    def add_person(self, full_name = '', phone_number='', email_address=''):

        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor()
        full_name = input('Enter Full Name: ')
        phone_number = input('Enter Phone Number: ')
        email_address = input('Enter E-mail Address: ')
        connect.execute('INSERT INTO people(full_name, phone_number, email_address) VALUES(?,?,?)', (full_name, phone_number, email_address))
        db.commit()
        connect.close()
   
    def remove_person(self, id = ''):
        db = sqlite3.connect(DATABASE_FİLE)
        connect = db.cursor()
        id = input('Enter people id to delete: ')
        connect.execute('DELETE FROM people where id=?', (id,))
        db.commit() # Commit the changes to the database
        connect.close()

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

if __name__ == '__main__':

    import sys
    sys.argv.append('-v')

    import doctest
    doctest.testmod()

    app = AddressBookDatabase()
    choice = ''
    while choice not in ['exit' , 'quit' , 'q']:
        choice = input('Choose: ')

        if choice in ['exit' , 'quit' , 'q']:
            print("Exiting.")
            
        if choice in VALİD_COMMANDS:
            if choice == 'add':
                app.add_person()
                    
            elif choice == 'remove':
                app.remove_person()

            elif choice == 'list':
                app.list_person()

            else:
                print("Invalid choice.")