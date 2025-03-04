from enum import Enum

class Chord(Enum):
    AUGMENTED_MAJOR_SEVENTH = (4, 8, 11)
    MAJOR_SEVENTH = (4, 7, 11)
    DOMINANT_SEVENTH = (4, 7, 10)
    MINOR_MAJOR_SEVENTH = (3, 7, 11)
    MINOR_SEVENTH = (3, 7, 10)
    HALF_DIMINISHED_SEVENTH = (3, 6, 10)
    DIMINISHED_SEVENTH = (3, 6, 9)