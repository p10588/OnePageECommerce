import pytest
from testing.conftest import *
from service.order_service import OrderService, OrderFlowFactory
from uow.uow_order import UowOrder

@pytest.mark.parametrize('class_name',['COD', 'Prepaid' ])
def test_orderflow_factory(class_name):
    try:
        orderflow_class = OrderFlowFactory.create_orderflow(class_name)
        orderflow = orderflow_class(None, None, None)
        print(orderflow.__class__.__name__)
        assert orderflow.__class__.__name__ == class_name
    except Exception as e:
        print(f'Error: {e}')
        assert False

def test_place_order():
    try:
        order_service = OrderService(None)
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        order_service.place_order(test_place_order_data, UowOrder(test_db_connection_pool))
    except Exception as e:
        print(f'Error: {e}')
        assert False

def test_get_user_orders():
    try:
        order_service = OrderService(None)
        test_db_connection_pool = pool.ThreadedConnectionPool(**DB_DATA_POOL)
        data = order_service.get_user_orders('aaa@aaa.com', UowOrder(test_db_connection_pool))   
        print(data)
    except Exception as e:
        print(f'Error: {e}')
        assert False
    