from typing import List

from src.domain.order import Order
from src.application.ordercreator import OrderSource


class PlatformOrderSource(OrderSource):
    def __init__(self, order_data: dict) -> None:
        self.order_data = order_data

    def get_orders(self) -> List[Order]:
        # TODO: implement logic for extracting orders from order_data
        # to a list of Order objects
        return []
