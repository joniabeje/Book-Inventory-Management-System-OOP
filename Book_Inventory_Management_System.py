
class Book:
    inventory = []

    def __init__(self, title: str, author: str, genre: str, price: float, quantity: int):
        assert price >= 0, "Price can't be negative."
        assert quantity >= 0, "Quantity can't be negative."

        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

        Book.inventory.append(self)

    def update_quantity(self, amount: int):
        new_quantity = self.quantity + amount
        assert new_quantity >= 0, "Quantity can't be negative after update."
        self.quantity = new_quantity

    def update_price(self, new_price: float):
        assert new_price >= 0, "New price can't be negative."
        self.price = new_price

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre}, {self.price}, {self.quantity})"

    @staticmethod
    def list_inventory():
        for book in Book.inventory:
            print(book)
            print('-' * 20)


def main():
    while True:
        print("\nWelcome to the Online Bookstore Inventory System")
        print("1. Add a new book")
        print("2. Update book quantity")
        print("3. Update book price")
        print("4. View inventory")
        print("5. Exit")

        choice = input("Please choose an option: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")

            while True:
                try:
                    price = float(input("Enter the price (e.g., 9.99): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the price.")

            quantity = int(input("Enter the quantity: "))
            Book(title, author, genre, price, quantity)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            title = input("Enter the title of the book to update: ")
            for book in Book.inventory:
                if book.title == title:
                    amount = int(input(f"Enter the amount to update the quantity (can be negative): "))
                    book.update_quantity(amount)
                    print(f"Updated quantity for '{title}'.")
                    break
            else:
                print(f"Book '{title}' not found in inventory.")

        elif choice == '3':
            title = input("Enter the title of the book to update: ")
            for book in Book.inventory:
                if book.title == title:
                    while True:
                        try:
                            new_price = float(input("Enter the new price (e.g., 9.99): "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for the price.")
                    book.update_price(new_price)
                    print(f"Updated price for '{title}'.")
                    break
            else:
                print(f"Book '{title}' not found in inventory.")

        elif choice == '4':
            print("\nCurrent Inventory:")
            Book.list_inventory()

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
