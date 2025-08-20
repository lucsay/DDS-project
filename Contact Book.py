import os
import pickle

class ContactNode:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class ContactBook:
    def __init__(self, filename='contacts.dat'):
        self.head = None
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                try:
                    self.head = pickle.load(f)
                except EOFError:
                    self.head = None

    def save_contacts(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.head, f)

    def insert_contact(self, name, phone):
        new_node = ContactNode(name, phone)
        if self.head is None or name.lower() < self.head.name.lower():
            new_node.next = self.head
            self.head = new_node
            self.save_contacts()
            return
        current = self.head
        while current.next and current.next.name.lower() < name.lower():
            current = current.next
        if current.name.lower() == name.lower():
            current.phone = phone
            self.save_contacts()
            return
        new_node.next = current.next
        current.next = new_node
        self.save_contacts()

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                return current
            current = current.next
        return None

    def update_contact(self, name, new_phone):
        node = self.search_contact(name)
        if node:
            node.phone = new_phone
            self.save_contacts()
            return True
        return False

    def delete_contact(self, name):
        current = self.head
        prev = None
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.save_contacts()
                return True
            prev = current
            current = current.next
        return False

    def display_contacts(self):
        current = self.head
        while current:
            print(f"{current.name}: {current.phone}")
            current = current.next


if __name__ == "__main__":
    cb = ContactBook()

    cb.insert_contact("Alice", "12345")
    cb.insert_contact("Bob", "23456")
    cb.insert_contact("Charlie", "34567")
    cb.insert_contact("Alice", "54321")  # update existing Alice

    print("Contacts after insertion and update:")
    cb.display_contacts()

    print("\nSearch for Bob:")
    contact = cb.search_contact("Bob")
    if contact:
        print(f"Found: {contact.name} - {contact.phone}")
    else:
        print("Bob not found")

    cb.update_contact("Charlie", "76543")
    print("\nContacts after updating Charlie's phone:")
    cb.display_contacts()

    cb.delete_contact("Alice")
    print("\nContacts after deleting Alice:")
    cb.display_contacts()
