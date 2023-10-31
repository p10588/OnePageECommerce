import pytest
from service.payment_service import PaymentService, PaymentFactory,PaymentType

@pytest.mark.parametrize('payment_method, total_amount',[
                          (PaymentType.TEST_PAYMENT, 1000),
                          (PaymentType.TEST_PAYMENT, None),
                        ])
def test_process_payment(payment_method, total_amount):
    try:
        payment_service = PaymentService()
        payment_service.process_payment(payment_method, total_amount,
                                        __payment_callback, __payment_fallback)
        assert True
    except Exception as e:
        print(f'Error: {e}')
        assert False

def __payment_callback():
    print('payment callback')
    pass

def __payment_fallback():
    print('payment fallback')
    pass

@pytest.mark.parametrize('class_name',['TestPayment'])
def test_payment_factory(class_name):
    try:
        payment_class = PaymentFactory.create_payment(class_name)
        payment = payment_class()
        print(payment.__class__.__name__)
        assert payment.__class__.__name__ == class_name
    except Exception as e:
        print(f'Error: {e}')
        assert False