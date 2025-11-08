"""
Estimated time: 15 minutes
Actual time: 18
"""


class ProgrammingLanguage:
    """Display information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True or False based on language being dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of a ProgrammingLanguage"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
