from dataclasses import dataclass


@dataclass
class Client():
    """
    Represents a client with various attributes such as name, phone number, and address.

    Attributes:
    -----------
    code: str
        The unique identifier for the client.
    address_line_1: str
        The first line of the client's address.
    town: str
        The town or city where the client is located.
    phone: str
        The client's phone number.
    email: str
        The client's email address.
    name: str
        The client's first name.
    last_name: str
        The client's last name.
    """
    code: str
    address_line_1: str
    town: str
    phone: str
    email: str
    name: str
    last_name: str
