from typing import List

from src.domain.order import Order


class OrderSource():
    def get_orders(self) -> List[Order]:
        raise NotImplementedError()


class OrderDestination():
    def save_order(self, orders: Order):
        raise NotImplementedError()


class OrderCreator():
    def __init__(
        self,
        order_source: OrderSource,
        order_destination: OrderDestination
    ) -> None:
        self.order_source = order_source
        self.order_destination = order_destination

    def execute(self):
        orders = self.order_source.get_orders()
        for order in orders:
            self.order_destination.save_order(order)
