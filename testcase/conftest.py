'''
import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope='function')
def my_fixture(request):
    print('\n局部前置')
    yield
    print('\n局部后置')


@pytest.fixture(scope='session', autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
'''