import os
import unittest
class SecurityTest(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_security_1(self):
        assert 1 == 1

    def test_security_2(self):
        assert 1 == 1

    def test_security_3(self):
        assert 1 == 2

    def test_security_4(self):
        assert 1 == 1

    def test_security_5(self):
        assert 1 == 1

from BeautifulReport import BeautifulReport as bf
# 发现测试用例
ts = unittest.TestSuite()
ts.addTest(unittest.makeSuite(SecurityTest))
run = bf(ts)
report_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
run.report('', report_dir=report_dir + '/docs', filename='security_report.html')
