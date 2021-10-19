class RPGInfo:
    author = None
    title = None
    subtitle = None
    welcome_message = None

    @classmethod
    def welcome(cls):
        print(f"Welcome to {cls.title}: {cls.subtitle}")
        print(cls.welcome_message)

    @classmethod
    def credits(cls):
        print(f"This was {cls.title}.")
        print("Thank you for playing!")
        print(f"\nMade by {cls.author}.")
