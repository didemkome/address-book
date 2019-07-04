import sqlite3

class AddressBookDatabase():

    def __init__(self, filename="addressbook.db"):
        self.db_filename = filename
        db = sqlite3.connect(self.db_filename)
        connect = db.cursor()
        connect.execute("CREATE TABLE IF NOT EXISTS people( id INTEGER PRIMARY KEY, full_name, phone_number, email_address)")
        db.commit()
        connect.close()

    def add_person(self, full_name = '', phone_number='', email_address=''):
        db = sqlite3.connect(self.db_filename)
        connect = db.cursor()
        full_name = input('Enter Full Name: ')
        phone_number = input('Enter Phone Number: ')
        email_address = input('Enter E-mail Address: ')
        connect.execute('INSERT INTO people(full_name, phone_number, email_address) VALUES(?,?,?)', (full_name, phone_number, email_address))
        db.commit()
        connect.close()
        
    def remove_person(self, id = ''):
        db = sqlite3.connect(self.db_filename)
        connect = db.cursor()
        id = input('Enter people id to delete: ')
        connect.execute('DELETE FROM people where id=?', (id,))
        db.commit() # Commit the changes to the database
        connect.close()

    def list_person(self):
        db = sqlite3.connect(self.db_filename)
        connect = db.cursor() # create a new cursor
        connect.execute('SELECT * FROM people')
        records = connect.fetchall() #to fetch all tasks from the tasks table , return a list
        if records:
            print("{:<15} {:<15} {:<15} {:<15}".format('ID' , 'Full Name', 'Phone Number', 'E-mail Address'))
            for row in records:
                print ('{:<15} {:<15} {:<15} {:<15}'.format(row[0], row[1], row[2], row[3]))
                # print (row)    
        connect.close()
        return records

if __name__ == '__main__':

    app = AddressBookDatabase()
    choice = ''
    while choice != '4':
        print(app)
        choice = input('Choose: ')
        if choice == '1':
            app.add_person()
        elif choice == '2':
            app.remove_person()
        elif choice == '3':
            app.list_person()
        elif choice == '4':
            print("Exiting.")
        else:
            print("Invalid choice.")