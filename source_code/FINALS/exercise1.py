class BrowserHistory:

    def __init__(self):
        self.history = []

    def visit_website(self, url):
        self.history.append(url)
        print(f"Website added: {url}")

    def go_back(self):
        if self.is_empty():
            print("Browser history is empty. No website to go back to.")
            return None
        removed = self.history.pop()
        print(f"Website removed: {removed}")
        return removed

    def current_website(self):
        if self.is_empty():
            print("Browser history is empty. No current website.")
            return None
        current = self.history[-1]
        print(f"Current Website: {current}")
        return current

    def display_history(self):
        if self.is_empty():
            print("Browser history is empty.")
            return
        print("\nBrowser History (TOP to BOTTOM):")
        for site in reversed(self.history):
            print(site)

    def count_history(self):
        return len(self.history)

    def is_empty(self):
        return len(self.history) == 0


def display_menu():
    print("\nBROWSER HISTORY MANAGER")
    print("1. Visit a website")
    print("2. Go Back")
    print("3. View Current Website")
    print("4. Display Browser History")
    print("5. Count Visited Websites")
    print("6. Exit")

def main():
    browser = BrowserHistory()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            url = input("Enter website address: ").strip()
            browser.visit_website(url)
        elif choice == "2":
            browser.go_back()
        elif choice == "3":
            browser.current_website()
        elif choice == "4":
            browser.display_history()
        elif choice == "5":
            print(f"Total Visited Websites: {browser.count_history()}")
        elif choice == "6":
            print("Exiting Browser History Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")


if __name__ == "__main__":
    main()




