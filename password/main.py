import sqlite3

MASTER_USER = "PKZD"
MASTER_PASSWORD = "666"

print("Enter your username")
usr = input("User: ")
psw = input("Password: ")
if usr != MASTER_USER or psw != MASTER_PASSWORD:
    print("Check your username and password and try again.")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL

);
''')

def menu():
    print("*" * 30)
    print("* n : enter a new password   *")
    print("* l : list of saved services *")
    print("* s : Show passwords         *")
    print("* e : exit                   *")
    print("*" * 30)

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    
    ''')

    if cursor.rowcount == 0:
        print('The service is not registered.')
    else:
        for user in cursor.fetchall():
            print('\n')
            print("#" * 30)
            print(user)
            print("#" * 30)
            print('\n')

def insert_service(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print("  -------------")
        print("|",service, "|")
        print("  ------------")

while True:
    menu()
    choice = input("What do you want to do? : ")
    if choice not in ['n', 'l', 's', 'e']:
        print ("Invalid option!")
        continue

    if choice == 'e':
        print("Goodbye XD")
        break

    if choice == 'n':
        service = input('What is the name of the service ? : ')
        username = input('What is the name of the user ? : ')
        password = input("what's the password ? : ")
        insert_service(service, username, password)

    if choice == 'l':
        show_services()

    if choice == 's':
        service = input("What service are you looking for? : ")
        get_password(service)

conn.close()

