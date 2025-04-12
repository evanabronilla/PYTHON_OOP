class Author:
    """Represents an author of a book."""

    def __init__(self, name: str):
        self.name = name

    def get_details(self) -> str:
        return f"Author: {self.name}"


class Book:
    """Represents a book, composed with an Author and optional nested Chapter."""

    def __init__(self, title: str, author: Author):
        self.title = title
        self.author = author

    def display(self) -> None:
        print(f"Book: {self.title} by {self.author.get_details()}")

    class Chapter:
        """Nested class representing a chapter in the book."""

        def __init__(self, title: str, number: int):
            self.title = title
            self.number = number

        def display_chapter(self) -> None:
            print(f"Chapter {self.number}: {self.title}")
