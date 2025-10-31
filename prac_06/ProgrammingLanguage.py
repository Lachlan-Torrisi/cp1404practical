class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Returns a formatted string for this language."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}")