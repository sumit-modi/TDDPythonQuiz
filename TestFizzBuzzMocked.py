import unittest
import pymock
import FizzBuzz
"""
Q5. Write the psuedocode for the test_repport method, such that it uses PyMock
    mock objects to test the report method of FizzBuzz. [5 pts]
"""
class TestFizzBuzzMocked(pymock.PyMockTestCase):
        
    def setUp(self):
        super(TestFizzBuzzMocked, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setUp TestFizzBuzzMocked"

    def tearDown(self):
        super(TestFizzBuzzMocked, self).tearDown()
        self.fb = None

    def test_report(self):

        mock_opener = self.mock()
        mock_report_file = self.mock()
        self.expectAndReturn(mock_opener.open('c:\temp\Joe.txt', 'w'), mock_report_file)
        
        mock_report_file.write("33 fizz")
        mock_report_file.close()
        #replay
        self.replay()

        fb = FizzBuzz.FizzBuzz()
        fb.report([33], 'c:\temp\Joe.txt', mock_report_file)

        #verify
        self.verify()















        


if __name__ == "__main__":
    unittest.main()
