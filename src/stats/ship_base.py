from enum import Enum


class ShipBase(Enum):
    # w x l in mm
    SMALL = (43, 71)
    MEDIUM = (63, 102)
    LARGE = (77.5, 129)
    HUGE = (77.5, 365)

