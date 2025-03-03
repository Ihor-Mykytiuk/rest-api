from typing import List
from dataclasses import dataclass, field
import uuid


@dataclass
class Book:
    title: str
    author: str
    published_year: int
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


books: List[Book] = []
