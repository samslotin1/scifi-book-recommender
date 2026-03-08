import random

books = [
    {"title": "Dune", "type": "space"},
    {"title": "1984", "type": "dystopia"},
    {"title": "Lucifer's Hammer", "type": "apocalypse"},
    {"title": "The Stand", "type": "apocalypse"},
    {"title": "Brave New World", "type": "dystopia"},
    {"title": "Fahrenheit 451", "type": "dystopia"},
    {"title": "The Postman", "type": "apocalypse"}
]

print("=== Classic Sci-Fi Book Recommender ===")
print()

print("Choose a category: space | dystopia | apocalypse")
choice = input("Your choice: ").lower()

matches = []

for book in books:
    if book["type"] == choice:
        matches.append(book["title"])

print()

if matches:
    recommendation = random.choice(matches)
    print("Recommended book:", recommendation)
else:
    print("No books found for that category.")
