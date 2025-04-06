from dataclasses import dataclass
from typing import List

@dataclass
class Event:
    outcome: List<str>
    
    def __init__(self, )