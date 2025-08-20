class BookNode:
    """
    Node representing a book in the inventory linked list.
    """
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.next = None


class Action:
    """
    Class representing an action for undo stack.
    Types: 'borrow' or 'return'
    """
    def __init__(self, action_type, book_title):
        self.action_type = action_type
        self.book_title = book_title


class ELibrary:
    def __init__(self):
        self.head = None  # Head of the inventory linked list
        self.undo_stack = []  # Stack for undoing actions

    def add_book(self, title, author):
        new_book = BookNode(title, author)
        new_book.next = self.head
        self.head = new_book
        print(f"Book added: '{title}' by {author}")

    def borrow_book(self, title):
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                if current.is_borrowed:
                    print(f"'{title}' is already borrowed.")
                    return
                current.is_borrowed = True
                self.undo_stack.append(Action('borrow', title))
                print(f"You have borrowed '{title}'")
                return
            current = current.next
        print(f"Book '{title}' not found in inventory.")

    def return_book(self, title):
        current = self.head
        while current:
            if current.title.lower() == title.lower():
                if not current.is_borrowed:
                    print(f"'{title}' was not borrowed.")
                    return
                current.is_borrowed = False
                self.undo_stack.append(Action('return', title))
                print(f"You have returned '{title}'")
                return
            current = current.next
        print(f"Book '{title}' not found in inventory.")

    def undo_last_action(self):
        if not self.undo_stack:
            print("No actions to undo.")
            return

        last_action = self.undo_stack.pop()
        current = self.head
        while current:
            if current.title.lower() == last_action.book_title.lower():
                if last_action.action_type == 'borrow':
                    current.is_borrowed = False
                    print(f"Undo: Borrow of '{current.title}' undone.")
                elif last_action.action_type == 'return':
                    current.is_borrowed = True
                    print(f"Undo: Return of '{current.title}' undone.")
                return
            current = current.next
        print(f"Undo failed: Book '{last_action.book_title}' not found.")

    def search_by_title(self, title):
        found = False
        current = self.head
        print(f"\nSearch results for title '{title}':")
        while current:
            if title.lower() in current.title.lower():
                status = "Borrowed" if current.is_borrowed else "Available"
                print(f" - {current.title} by {current.author} [{status}]")
                found = True
            current = current.next
        if not found:
            print("No books found.")

    def search_by_author(self, author):
        found = False
        current = self.head
        print(f"\nSearch results for author '{author}':")
        while current:
            if author.lower() in current.author.lower():
                status = "Borrowed" if current.is_borrowed else "Available"
                print(f" - {current.title} by {current.author} [{status}]")
                found = True
            current = current.next
        if not found:
            print("No books found.")

    def display_inventory(self):
        if not self.head:
            print("Inventory is empty.")
            return

        print("\nE-Library Inventory:")
        current = self.head
        while current:
            status = "Borrowed" if current.is_borrowed else "Available"
            print(f" - {current.title} by {current.author} [{status}]")
            current = current.next



if __name__ == "__main__":
    library = ELibrary()

    
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

  
    library.display_inventory()


    library.borrow_book("1984")
    library.return_book("1984")

    library.undo_last_action()


    library.undo_last_action()

 
    library.undo_last_action()

 
    library.search_by_title("great")
    library.search_by_author("Orwell")


    library.display_inventory()
