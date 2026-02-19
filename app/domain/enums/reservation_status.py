from enum import Enum

class ReservationStatus(Enum):
    CREATED = "created"
    CHECKED_IN = "checked_in"
    CHECKED_OUT = "checked_out"