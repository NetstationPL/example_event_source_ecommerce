import uuid
from unittest.mock import MagicMock

from crm.commands import RegisterCustomer
from crm.events import CustomerRegistered
from crm.services import RegisterCustomerHandler


def test_register_command_should_publish_registered_event():
    event_store = MagicMock()
    customer_id = uuid.uuid4()
    handler = RegisterCustomerHandler(event_store)

    handler.handle(RegisterCustomer(customer_id=customer_id, name="John Doe"))

    event_store.publish.assert_called_once_with(
        CustomerRegistered(customer_id=customer_id, name="John Doe"),
        "Customer#{}".format(customer_id),
    )
