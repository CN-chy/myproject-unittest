import os
import unittest
class OrderTest(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_order_1(self):
        assert 1 == 1

    def test_order_2(self):
        assert 1 == 1

    def test_order_3(self):
        assert 1 == 2

    def test_order_4(self):
        assert 1 == 1

    def test_order_5(self):
        assert 1 == 1

from BeautifulReport import BeautifulReport as bf
# 发现测试用例
ts = unittest.TestSuite()
ts.addTest(unittest.makeSuite(OrderTest))
run = bf(ts)
report_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
run.report('', report_dir=report_dir + '/docs', filename='order_report.html')