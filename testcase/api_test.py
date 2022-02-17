# 数据驱动
import pytest
'''
方法一 基础用法：@pytest.mark.parametrize()

@pytest.mark.parametrize(args_name, args_value)
args_name:参数名
args_value:参数值（list、tuple、dict+list、dict+tuple）数据中有多少值，接口用例执行多少次
'''


class TestApi(object):
    '''
    # 法一：@pytest.mark.parametrize(args_name, args_value)
    @pytest.mark.parametrize('args', ['y', 'z', 'q'])
    def test_api(self, args):
        print(args)
    '''

    # 法二：解包，基于法一
    @pytest.mark.parametrize('name, age', [['y', 24], ['z', 24], ['q', 24]])
    def test_api(self, name, age):
        print(name, age)


if __name__ == '__main__':
    pytest.main(['api_test.py'])






