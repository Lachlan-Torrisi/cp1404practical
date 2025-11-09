"""
Estimate: 30 min
Actual:
"""

from datetime import datetime

class Project:
    """Represent a project with relevant details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return user-friendly string representation."""
        return (f"{self.name}, start: {self.start_date.strftime('%d%m%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Order projects by priority (ascending)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% completed."""
        return self.completion_percentage == 100