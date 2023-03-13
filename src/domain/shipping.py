from dataclasses import dataclass


@dataclass
class Shipping():
    """
    Represents shipping information with various attributes such as address line 1 and town.

    Attributes:
    -----------
    address_line_1: str
        The first line of the shipping address.
    town: str
        The town or city where the shipping address is located.
    """
    address_line_1: str
    town: str
