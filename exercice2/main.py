#!/usr/bin/env python3
from book import Book
def main():
    print("\nExercise 2 and 3\n")
    book = Book("TEST")
    book.insert_buy(10, 10.0)
    book.insert_sell(120, 12.0)
    book.insert_buy(5, 10.0)
    book.insert_buy(2, 11.0)
    book.insert_sell(1, 10.0)
    book.insert_sell(10, 10.0)

    print("\nExercise 5")
    book.visualisationPandas()

if __name__ == "__main__":
    main()
