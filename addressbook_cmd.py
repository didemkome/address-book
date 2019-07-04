import sys
import sqlite3

VALİD_COMMANDS = ['add', 'remove', 'list']
DATABASE_FİLE = 'addressbook_cmd.db'

def add_person():
    db = sqlite3.connect(DATABASE_FİLE)
    connect = db.cursor()
    full_name = input('Enter Full Name: ')
    phone_number = input('Enter Phone Number: ')
    email_address = input('Enter E-mail Address: ')
    connect.execute('INSERT INTO people(full_name, phone_number, email_address) VALUES(?,?,?)', (full_name, phone_number, email_address))
    db.commit()
    connect.close()

def remove_person():
    db = sqlite3.connect(DATABASE_FİLE)
    connect = db.cursor()
    ID = input('Enter people id to delete: ')
    connect.execute('DELETE FROM people where id=?', (ID,))
    db.commit() # Commit the changes to the database
    connect.close()

def list_person():
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

def main(argv=None):
    db = sqlite3.connect(DATABASE_FİLE)
    connect = db.cursor()
    connect.execute("CREATE TABLE IF NOT EXISTS people( id INTEGER PRIMARY KEY, full_name, phone_number, email_address)")
    db.commit()

    while True:
        task = input('Select task: ')
        if task in ['exit' , 'quit' , 'q']:
            print("Exiting.")
            return 0
        
        if task in VALİD_COMMANDS:
            if task == 'add':
                add_person()
            elif task == 'remove':
                remove_person()
            elif task == 'list':
                list_person()
            else:
                pass

    connect.close()
if __name__ == '__main__':
    sys.exit(main() )