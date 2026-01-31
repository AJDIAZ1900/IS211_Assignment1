
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

if __name__ == "__main__":
    a = Book("Thorpe", "Beat the Dealer")
    a.display()
