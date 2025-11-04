"""
Estimated time: 30 minutes
Actual time:
"""
CURRENT_YEAR = 2025
MINIMUM_AGE = 50


class Guitar:
    """Class for storing guitar details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        """Get age of guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """"""
        return self.get_age() >= MINIMUM_AGE
