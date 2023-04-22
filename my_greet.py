def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather is nice today {name}?")

name = input("Enter your name: ").capitalize()
greet(name)

