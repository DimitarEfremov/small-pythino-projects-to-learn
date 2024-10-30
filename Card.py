from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Card:
    suit: str
    rank: str

    def __str__(self):
        return f'{self.rank} of {self.suit}'



