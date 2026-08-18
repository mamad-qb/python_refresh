# Python Refresh

A project-based Python learning repository built to turn core concepts into small, practical command-line applications. Each folder documents a step in my progression from Python fundamentals toward data analysis and business intelligence.

## Current projects

| Project | What it does | Concepts practiced |
|---|---|---|
| [Number Guessing Game](01_basics/number_game.py) | Multi-level guessing game with replay support | Functions, loops, conditionals, random numbers, input validation |
| [Password Generator](01_basics/password_generator.py) | Generates passwords based on user-selected requirements | Strings, lists, loops, validation, `random` |
| [Expense Tracker](02_python_core/expense_tracker) | Stores, displays, edits, deletes, and summarizes expenses | CRUD operations, JSON, functions, error handling |
| [Password Manager](02_python_core/password_manager) | Saves and searches account credentials in a local JSON file | File handling, JSON, dictionaries, menu-driven programs |
| [Smart Library Analyzer](02_python_core/smart_library) | Searches and analyzes a 110-book CSV dataset | CSV, data validation, filtering, sorting, aggregation, `Counter`, `defaultdict` |

## Smart Library Analyzer

The most complete project in the repository is a menu-driven library analysis tool. It loads and validates a CSV dataset before allowing the user to:

- search by title or author;
- filter by category or minimum rating;
- generate category-and-rating recommendations;
- calculate library-wide statistics;
- identify the most common categories;
- aggregate total and available inventory by category.

Run it from the repository root:

```bash
python 02_python_core/smart_library/smart_library.py
```

The script resolves the dataset relative to its own location, so it can also be launched from a different working directory.

## Repository structure

```text
python_refresh/
├── 01_basics/
│   ├── basics.py
│   ├── hello_world.py
│   ├── number_game.py
│   └── password_generator.py
├── 02_python_core/
│   ├── expense_tracker/
│   ├── password_manager/
│   └── smart_library/
│       ├── library_books.csv
│       ├── SMART_LIBRARY_EXCEL.xlsx
│       └── smart_library.py
├── LICENSE
└── README.md
```

## Skills demonstrated

- Python fundamentals and modular functions
- Input validation and exception handling
- Reading and validating CSV and JSON data
- Searching, filtering, sorting, and aggregating records
- Building understandable command-line interfaces
- Organizing small projects with Git and GitHub

## Roadmap

This repository is actively growing. The next stages will move from core Python into:

- object-oriented programming and testing;
- data analysis with NumPy and pandas;
- data visualization;
- end-to-end analytics projects using Python, SQL, Excel, and Power BI.

## License

This project is available under the [MIT License](LICENSE).
