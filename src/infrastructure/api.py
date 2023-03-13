import os
import logging
import hmac
import hashlib
import json
import base64
import json

from fastapi import FastAPI, HTTPException, BackgroundTasks, Request

from src.application.ordercreator import OrderCreator

# TODO: import platform specific classes
# from src.infrastructure.[platform]ordersource import [Platform]OrderSource
# from src.infrastructure.[platform]orderdestination import [Platform]OrderDestination

app = FastAPI()

def process_order(order_data: dict):
    logging.info(f"Order {order_data} will be processed")

    # Replace this with your own order process_ing logic
    # TODO: uncomment this when implement platform specific
    # Source and Destination classes
    #
    # order_source = [Platform]OrderSource(order_data)
    # orer_destination = [Platform]OrderDestination()
    # order_creator = OrderCreator(order_source, order_destination)
    # order_creator.execute()

    logging.info(f"Order {order_data} processed")


# this is the webhook endpoint. It will be called by the origin platform.
@app.post("/webhooks/order-create")
async def receive_order_create_webhook(
    request: Request, background_tasks: BackgroundTasks
):
    payload = await request.body()

    # TODO: implement security here...

    # Extract the order data
    order_data = json.loads(payload)
    if not order_data:
        raise HTTPException(
            status_code=400, detail="No order data found in webhook"
        )

    # Queue a background task to process the order
    background_tasks.add_task(process_order, order_data)

    # Respond immediately
    return {
        "message": (
            "Webhook received successfully and order processing "
            "started in background"
        )
    }
