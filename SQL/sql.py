import os
import time
import sqlite3 as sql

path_name = "data.db"

consult = "SELECT * FROM sqlite_master WHERE nome=?"

def create_menu():
    print('1. Create a table')
    print('2. Insert data:')
    print('3. Select data:')
    print('4. Delete data:')
    return int(input('Chose an operation:'))

def create_table(name, attributes):
    string = 'CREATE TABLE '
    string = string + name + ' ('
    
    for i in attributes.keys():
        string = string + i + ' ' + attributes[i] + ','

    string  = string[:len(string)-1] + ')' #Substitui a ultima virgula pelo parenteses
    return string


def main():
    attributes = {'id': 'INTEGER PRIMARY KEY AUTOINCREMENT', 'nome': 'TEXT NOT NULL', 'idade': 'INTEGER', 'salario': 'FLOAT'}
    answer = ''
    while not answer in range(1,4):
        os.system('cls' if os.name =='nt' else clear) #Limpa o terminal
        answer = create_menu()

    
    #Open database using with command to better security
    with sql.connect(path_name) as conn:
        cursor = conn.cursor()
        try:
            # cursor.execute("CREATE TABLE testes (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER, salario FLOAT)")
            cursor.execute(create_table('clientes', attributes))
        except:
          print("Already exists a database with this name!")
          time.sleep(2)  
        # cursor.execute("INSERT INTO testes (nome,idade,salario) VALUES ('Rodrigo',26,1200.00)")

        # cursor.execute("SELECT * FROM 'testes'")

        result = cursor.fetchall()
        print(result)

main()