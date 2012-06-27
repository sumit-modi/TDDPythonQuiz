import unittest
import pymock
import FizzBuzz
"""
Q3. What will be printed when we execute 'python FizzBuzzStubbed.py' ? [3 pts]



Ans:_
setUpClass FizzBuzzStubbed
setup
test_report
teardown
.setup
test_report
teardown
.tearDownClass





Q4. Implement MyStub class so that you can send it as a fake object to the
report method of FizzBuzz object from a test case. [3 pts]

"""
class MyStub(object):
    def __init__(self):
        self.openflag=False
        self.values=[] # create empty list

    def open(self):
        self.openflag = True #"open fake file"

    def write(self,msg):
        self.values.append(msg) # append values to list

    def close():
        self.openflag = False # close fake "file"










    
class TestFizzBuzzStubbed(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        print "setUpClass FizzBuzzStubbed"
        
    def setUp(self):
        super(TestFizzBuzzStubbed, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setup"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        
    def tearDown(self):
        super(TestFizzBuzzStubbed, self).tearDown()
        self.fb = None
        print "teardown"

    def test_report(self):
        print "test_report"
        pass

    def test_report_for_empty_list(self):
        print "test_report"
        pass

if __name__ == "__main__":
    unittest.main()