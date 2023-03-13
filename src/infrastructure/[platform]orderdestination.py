
from src.application.ordercreator import OrderDestination
from src.domain.order import Order


class PlatformOrderDestination(OrderDestination):
    def __init__(self):
        pass

    def create_order(self, order: Order):
        # TODO: implement logic for creating order in destination platform.
        pass
