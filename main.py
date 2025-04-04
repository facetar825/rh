import sqlite3
import random
library_db = sqlite3.connect("librery.db")
cursor = library_db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Books ("
               "book_id INTEGER,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER,"
               "available INTEGER )")

cursor.execute("CREATE TABLE IF NOT EXISTS Readers ("
               "reader_id INTEGER,"
               "name TEXT,"
               "phone TEXT,"
               "book_id INTEGER)")
library_db.commit()
library_db.close()


def add_book(title, author, year):
    library_db = sqlite3.connect('librery.db')
    cursor = library_db.cursor()
    book_id = random.randint(1, 1000)
    availble = 1
    cursor.execute("INSERT INTO Books (book_id, title, author, year, available) VALUES (?, ?, ?, ?, ?)",(book_id, title, author, year, availble))

    library_db.commit()
    library_db.close()
def add_readers(name, phone):
    library_db = sqlite3.connect("librery.db")
    cursor = library_db.cursor()
    reader_id = random.randint(1, 1000)
    book_id = random.randint(1,100)

    cursor.execute("INSERT INTO Readers ("
               "reader_id,"
               "name,"
               "phone,"
               "book_id ) VALUES (?, ?, ?, ?)", (reader_id, name, phone, book_id))


    library_db.commit()
    library_db.close()
add_book("gg", "ee", 23)





