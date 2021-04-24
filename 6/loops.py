# pythonic loop
my_items = ["a", "b", "c"]

for item in my_items:
    print(item)

# pythonic loop with index
for i, item in enumerate(my_items):
    print(f"{i}: {item}")

# pythonic loop with key and values
emails = {
    "Bob": "bob@example.com",
    "Alice": "alice@example.com",
}

for name, email in emails.items():
    print(f"{name} -> {email}")
