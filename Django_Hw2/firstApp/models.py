from datetime import datetime

from django.db import models

# Create your models here.

class Task:
    title: str
    description: str
    beginning : datetime
    end : datetime

    def __init__(self, title, description, beginning, end):
        self.title = title
        self.description = description
        self.beginning = beginning
        self.end = end

    def __str__(self):
        return self.title