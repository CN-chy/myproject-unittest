import os.path
import unittest
import yaml

class UserTest(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_user_1(self):
        assert 1 == 1

    def test_user_2(self):
        assert 1 == 1

    def test_user_3(self):
        assert 1 == 2

    def test_user_4(self):
        assert 1 == 1

    def test_user_5(self):
        assert 1 == 1

from BeautifulReport import BeautifulReport as bf
# 发现测试用例
ts = unittest.defaultTestLoader.discover('./', pattern='*.py')
run = bf(ts)
report_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
run.report('', report_dir=report_dir + '/docs', filename='user_report.html')
