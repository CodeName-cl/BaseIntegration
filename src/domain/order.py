from dataclasses import dataclass
from typing import List

from src.domain.client import Client
from src.domain.item import Item
from src.domain.shipping import Shipping


@dataclass
class Order():
    """
    Represents an order with various attributes such as ID, name, net amount, and shipping information.

    Attributes:
    -----------
    id: str
        The unique identifier for the order.
    name: str
        The name of the order.
    net: float
        The net amount of the order (i.e. the total amount before taxes and fees).
    iva: float
        The amount of IVA tax applied to the order.
    ila: float
        The amount of ILA tax applied to the order.
    status: str
        The current status of the order (e.g. "processing", "shipped", "delivered").
    items: List[Item]
        A list of items included in the order.
    client: Client
        The client who placed the order.
    shipping: Shipping
        The shipping information for the order.
    """
    id: str
    name: str
    net: float
    iva: float
    ila: float
    status: str
    items: List[Item]
    client: Client
    shipping: Shipping
