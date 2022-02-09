import pytest


@pytest.fixture(scope='function')
def all_fixture(request):
    print('\n全局前置')
    yield
    print('\n全局后置')