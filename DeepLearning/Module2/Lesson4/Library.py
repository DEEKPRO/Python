class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"We have the follwing books in out library: {self.name}")
        for book in self.booklist:
            print(book)

    def landBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    
    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list.")
    
    def ret(self, book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Wings of Fire', "Dog man"], "Let's Upskill")

    while True:
        print(f"Welcome to the {books.name} library. Enter your choice to continue.")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()
        if user_choice not in ["1", '2', '3', '4']:
            print("Please enter a valid option.")
            continue

        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            books.displayBooks()
        
        elif user_choice == 2:
            books.displayBooks()
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            books.landBook(user, book)
        
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            books.ret(book)
        
        else:
            print("Not a valid option.")
        
        print("Press q to quit and c to continue")
        users = ""
        while (users !="c" and users != "q"):
            users = input()
            if users == "q":
                exit()

            elif users == "c":
                continue