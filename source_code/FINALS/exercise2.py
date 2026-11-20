class Queue:

    def __init__(self):
        self.requests = []  # each item: dict with id, name, service

    def is_empty(self):
        return len(self.requests) == 0

    def enqueue(self, student_id, name, service):
        request = {"id": student_id, "name": name, "service": service}
        self.requests.append(request)  # rear = end of list
        print("Student request successfully added!")

    def dequeue(self):
        if self.is_empty():
            print("No pending student requests. Queue is empty.")
            return None
        served = self.requests.pop(0)  # front = index 0 (allowed by rubric)
        print("\nSTUDENT SUCCESSFULLY SERVED!")
        print(f"Student ID: {served['id']}")
        print(f"Student Name: {served['name']}")
        print(f"Service: {served['service']}")
        return served

    def peek(self):
        if self.is_empty():
            print("No pending student requests. Queue is empty.")
            return None
        front = self.requests[0]
        print("\nNEXT STUDENT TO BE SERVED:")
        print(f"Student ID: {front['id']}")
        print(f"Student Name: {front['name']}")
        print(f"Service: {front['service']}")
        return front

    def display_queue(self):
        if self.is_empty():
            print("No pending student requests. Queue is empty.")
            return
        print("\nPENDING STUDENT REQUESTS:")
        print("FRONT")
        for req in self.requests:
            print(f"{req['id']} | {req['name']} | {req['service']}")
        print("REAR")

    def count(self):
        return len(self.requests)


def display_menu():
    print("\nSTUDENT SERVICE REQUEST SYSTEM")
    print("1. Add Student Request")
    print("2. Serve Next Student")
    print("3. View Next Student")
    print("4. Display All Pending Requests")
    print("5. Count Pending Requests")
    print("6. Exit")


def main():
    queue = Queue()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Student Name: ").strip()
            service = input("Service: ").strip()
            queue.enqueue(student_id, name, service)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.peek()
        elif choice == "4":
            queue.display_queue()
        elif choice == "5":
            print(f"Total pending requests: {queue.count()}")
        elif choice == "6":
            print("Exiting Student Service Request System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    main()



