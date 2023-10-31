import pytest
from service.logistics_service import LogisticsFactory, LogisticsService,LogisticsType

def test_process_logistics():
    try: 
        log_service = LogisticsService()
        log_service.process_logistics(LogisticsType.TEST_LOGISTICS, 'wertyuio')
        assert True
    except Exception as e :
        print(f'Error: {e}')
        assert False

@pytest.mark.parametrize('class_name',['TestLogistics'])
def test_logistics_factory(class_name):
    try:
        logistics_class = LogisticsFactory.create_Logistics(class_name)
        logistics = logistics_class()
        print(logistics.__class__.__name__)
        assert logistics.__class__.__name__ == class_name
    except Exception as e:
        print(f'Error: {e}')
        assert False