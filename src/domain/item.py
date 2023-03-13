from dataclasses import dataclass


@dataclass
class Item():
    """
    Represents an item with various attributes such as SKU, title, quantity, and price.

    Attributes:
    -----------
    sku: str
        The unique identifier for the item.
    title: str
        The title of the item.
    quantity: float
        The quantity of the item.
    price: float
        The price of the item.
    net: float
        The net amount of the item (i.e. the total amount before taxes and fees).
    iva: float
        The amount of IVA tax applied to the item.
    ila: float
        The amount of ILA tax applied to the item.
    discount: float
        The amount of discount applied to the item.
    """
    SKU: str
    title: str
    quantity: float
    price: float
    net: float
    iva: float
    ila: float
    discount: float
