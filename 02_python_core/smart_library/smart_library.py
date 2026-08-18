"""Command-line analyzer for the Smart Library CSV dataset."""

import csv
from collections import Counter, defaultdict
from pathlib import Path


DATA_FILE = Path(__file__).with_name("library_books.csv")
REQUIRED_COLUMNS = {
    "book_id", "title", "author", "category", "year", "pages",
    "rating", "copies", "available_copies",
}


def load_books(file_path=DATA_FILE):
    """Load and validate book records from a CSV file."""
    try:
        with Path(file_path).open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            columns = set(reader.fieldnames or [])
            missing = REQUIRED_COLUMNS - columns
            if missing:
                raise ValueError(
                    "CSV is missing required columns: " + ", ".join(sorted(missing))
                )

            books = []
            for line_number, row in enumerate(reader, start=2):
                try:
                    row["year"] = int(row["year"])
                    row["pages"] = int(row["pages"])
                    row["rating"] = float(row["rating"])
                    row["copies"] = int(row["copies"])
                    row["available_copies"] = int(row["available_copies"])
                except (TypeError, ValueError) as error:
                    raise ValueError(f"Invalid numeric value on CSV line {line_number}") from error

                if row["available_copies"] > row["copies"]:
                    raise ValueError(
                        f"Available copies exceed total copies on CSV line {line_number}"
                    )
                books.append(row)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Dataset not found: {file_path}") from error

    if not books:
        raise ValueError("The CSV file contains no book records.")
    return books


def filter_books(books, category=None, minimum_rating=None):
    """Return books matching an optional category and minimum rating."""
    category = category.casefold().strip() if category else None
    return [
        book for book in books
        if (category is None or book["category"].casefold() == category)
        and (minimum_rating is None or book["rating"] >= minimum_rating)
    ]


def search_books(books, query):
    """Search case-insensitively in book titles and author names."""
    query = query.casefold().strip()
    if not query:
        return []
    return [
        book for book in books
        if query in book["title"].casefold() or query in book["author"].casefold()
    ]


def sort_by_rating(books):
    """Return a new list ordered by rating, then title."""
    return sorted(books, key=lambda book: (-book["rating"], book["title"].casefold()))


def category_analysis(books, limit=5):
    """Return the most common categories with counts and percentages."""
    counts = Counter(book["category"] for book in books)
    return [
        {
            "category": category,
            "titles": count,
            "percentage": count / len(books) * 100,
        }
        for category, count in counts.most_common(limit)
    ]


def inventory_by_category(books):
    """Aggregate total and available copies for every category."""
    inventory = defaultdict(lambda: {"copies": 0, "available": 0})
    for book in books:
        inventory[book["category"]]["copies"] += book["copies"]
        inventory[book["category"]]["available"] += book["available_copies"]
    return dict(sorted(inventory.items()))


def library_statistics(books):
    """Calculate high-level library statistics."""
    return {
        "titles": len(books),
        "copies": sum(book["copies"] for book in books),
        "available": sum(book["available_copies"] for book in books),
        "average_rating": sum(book["rating"] for book in books) / len(books),
        "highest_rated": max(books, key=lambda book: book["rating"]),
        "lowest_rated": min(books, key=lambda book: book["rating"]),
    }


def read_rating(prompt="Minimum rating (0-5): "):
    """Read a valid rating from the user."""
    while True:
        try:
            rating = float(input(prompt))
            if 0 <= rating <= 5:
                return rating
        except ValueError:
            pass
        print("Please enter a number between 0 and 5.")


def print_books(books):
    if not books:
        print("No matching books found.")
        return
    print(f"\n{'ID':<6} {'Title':<45} {'Category':<20} {'Rating':<7} Available")
    print("-" * 94)
    for book in books:
        print(
            f"{book['book_id']:<6} {book['title'][:43]:<45} "
            f"{book['category']:<20} {book['rating']:<7.1f} "
            f"{book['available_copies']}/{book['copies']}"
        )


def print_statistics(books):
    stats = library_statistics(books)
    print("\n--- Library Statistics ---")
    print(f"Unique titles: {stats['titles']}")
    print(f"Total copies: {stats['copies']}")
    print(f"Available copies: {stats['available']}")
    print(f"Average rating: {stats['average_rating']:.2f}")
    print(
        f"Highest rated: {stats['highest_rated']['title']} "
        f"({stats['highest_rated']['rating']:.1f})"
    )
    print(
        f"Lowest rated: {stats['lowest_rated']['title']} "
        f"({stats['lowest_rated']['rating']:.1f})"
    )


def print_category_analysis(books):
    print("\n--- Top Categories ---")
    for index, item in enumerate(category_analysis(books), start=1):
        print(
            f"{index}. {item['category']}: {item['titles']} titles "
            f"({item['percentage']:.1f}%)"
        )


def print_inventory(books):
    print(f"\n{'Category':<24} {'Copies':>8} {'Available':>12}")
    print("-" * 46)
    for category, totals in inventory_by_category(books).items():
        print(f"{category:<24} {totals['copies']:>8} {totals['available']:>12}")


def main():
    try:
        books = load_books()
    except (FileNotFoundError, ValueError) as error:
        print(f"Could not start Smart Library: {error}")
        return

    actions = {
        "1": lambda: print_books(search_books(books, input("Title or author: "))),
        "2": lambda: print_books(filter_books(books, category=input("Category: "))),
        "3": lambda: print_books(sort_by_rating(filter_books(books, minimum_rating=read_rating()))),
        "4": lambda: print_books(sort_by_rating(filter_books(
            books,
            category=input("Category: "),
            minimum_rating=read_rating(),
        ))),
        "5": lambda: print_statistics(books),
        "6": lambda: print_category_analysis(books),
        "7": lambda: print_inventory(books),
    }

    while True:
        print(
            "\n=== Smart Library Analyzer ===\n"
            "1. Search by title or author\n"
            "2. Filter by category\n"
            "3. Filter by minimum rating\n"
            "4. Recommend by category and rating\n"
            "5. Show library statistics\n"
            "6. Analyze categories\n"
            "7. Show inventory by category\n"
            "0. Exit"
        )
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Choose a number from 0 to 7.")


if __name__ == "__main__":
    main()
