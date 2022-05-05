import os
import psycopg2
from settings import url

class JournalEntry():
    def __init__(self,title,text, entry_num):
        self._title = title
        self._text = text
        self._entry_num = entry_num
    def __str__(self):
        return self._title
    def print_record(self):
        return self._entry_num, self._title, self._text

#url = "postgres://onwjxrpt:bjnHXy30sMOxDhnVVb4t4lEnDZ5buNq8@jelani.db.elephantsql.com/onwjxrpt"


exit = False
entries = []
while not exit:
    connection = psycopg2.connect(url)
    cursor = connection.cursor()
    os.system('clear' if os.name == "posix" else 'cls')
    number_of_posts = len(entries)+1
    start_screen = tkinter.Label(text = "Welcome to the Journal\n Please select one of the following options: 1)Add a New Entry \n2)View an Entry\n3)Exit" )
    print("Welcome to the Journal\n")
    print("Please select one of the following options: ")
    print("1)Add a New Entry \n2)View an Entry\n3)Exit")
    entry = input()
    if entry == "1":
        os.system('cls' if os.name == "nt" else 'clear')
        print("Please Input a Title:")
        title = input()
        print("\nText:")
        text = input()
        newEntry = JournalEntry(title,text,number_of_posts)
        entries.append(newEntry)
        try:
            query = "INSERT INTO entries (entry_num, title, text) values ('{entry_num}', '{title}', '{text}');".format(entry_num = number_of_posts, title = title, text = text)
            cursor.execute(query)
            connection.commit()
        finally:
            connection.close()
            cursor.close()
    elif entry == "2":
        os.system("cls" if os.name == "nt" else 'clear')
        try:
            query = "SELECT * FROM entries"
            cursor.execute(query)
            entry_list = cursor.fetchall()    
            print(entry_list)
        finally:
            cursor.close()
            connection.close()
        _wait = input("Press enter to continue")
    elif entry == "3":
        exit = 3