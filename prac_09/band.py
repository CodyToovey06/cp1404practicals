class Band:
    """Represents a Band objective."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({",".join([str(musician) for musician in self.musicians])}"

    def add(self, musician):
        """Add musicians to the collection."""
        self.musicians.append(musician)

    def play(self):
        """Return musicals that are playing."""
        return "\n".join(musician.play() for musician in self.musicians)
