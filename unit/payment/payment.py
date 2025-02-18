import os
import unittest
class PaymentTest(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_payment_1(self):
        assert 1 == 1

    def test_payment_2(self):
        assert 1 == 1

    def test_payment_3(self):
        assert 1 == 2

    def test_payment_4(self):
        assert 1 == 1

    def test_payment_5(self):
        assert 1 == 1

from BeautifulReport import BeautifulReport as bf
# 发现测试用例
ts = unittest.TestSuite()
ts.addTest(unittest.makeSuite(PaymentTest))
run = bf(ts)
report_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
run.report('', report_dir=report_dir + '/docs', filename='payment_report.html')
