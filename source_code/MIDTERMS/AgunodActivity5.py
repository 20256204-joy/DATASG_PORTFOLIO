class Node:
    def __init__(self, record_id, resource_name):
        self.record_id = record_id
        self.resource_name = resource_name
        self.next = None

class ResourceLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def id_exists(self, record_id):
        current = self.head
        while current is not None:
            if current.record_id == record_id:
                return True
            current = current.next
        return False

    def insert_at_beginning(self, record_id, resource_name):
        new_node = Node(record_id, resource_name)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, record_id, resource_name):
        new_node = Node(record_id, resource_name)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, target_id, record_id, resource_name):
        current = self.head
        while current is not None:
            if current.record_id == target_id:
                new_node = Node(record_id, resource_name)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False

    def delete_by_id(self, record_id):
        if self.head is None:
            return False
        if self.head.record_id == record_id:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.record_id == record_id:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search_by_id(self, record_id):
        current = self.head
        while current is not None:
            if current.record_id == record_id:
                return current
            current = current.next
        return None

    def display_all(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        print("Current records:")
        while current is not None:
            print(current.record_id, "-", current.resource_name, "->", end=" ")
            current = current.next
        print("None")

    def count_records(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


def read_id(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Error: ID must be a whole number. Try again.")


def read_name(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Error: Resource name cannot be blank. Try again.")


def main():
    registry = ResourceLinkedList()

    while True:
        print("\n== CAMPUS RESOURCE REGISTRY ==")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert after a record ID")
        print("4. Delete by ID")
        print("5. Search by ID")
        print("6. Display all records")
        print("7. Count records")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            rid = read_id("Enter record ID: ")
            if registry.id_exists(rid):
                print("Error: ID", rid, "already exists. Duplicate IDs are not allowed.")
            else:
                name = read_name("Enter resource name: ")
                registry.insert_at_beginning(rid, name)
                print("Record added successfully.")

        elif choice == "2":
            rid = read_id("Enter record ID: ")
            if registry.id_exists(rid):
                print("Error: ID", rid, "already exists. Duplicate IDs are not allowed.")
            else:
                name = read_name("Enter resource name: ")
                registry.insert_at_end(rid, name)
                print("Record added successfully.")

        elif choice == "3":
            target = read_id("Enter target ID: ")
            rid = read_id("Enter new record ID: ")
            if registry.id_exists(rid):
                print("Error: ID", rid, "already exists. Duplicate IDs are not allowed.")
            else:
                name = read_name("Enter resource name: ")
                if registry.insert_after(target, rid, name):
                    print("Record added successfully.")
                else:
                    print("Error: Target ID", target, "was not found. No changes made.")

        elif choice == "4":
            rid = read_id("Enter record ID to delete: ")
            if registry.delete_by_id(rid):
                print("Record deleted successfully.")
            else:
                print("Record ID", rid, "was not found. No changes made.")

        elif choice == "5":
            rid = read_id("Enter record ID to search: ")
            found = registry.search_by_id(rid)
            if found is not None:
                print("Record found:", found.record_id, "-", found.resource_name)
            else:
                print("Record ID", rid, "was not found.")

        elif choice == "6":
            registry.display_all()

        elif choice == "7":
            print("Record count:", registry.count_records())

        elif choice == "8":
            print("Thank you. Program terminated.")
            break

        else:
            print("Invalid choice. Please enter 1 to 8.")


main()