#-*- coding: utf-8 -*-
import unittest  

class ParametrizedTestCase(unittest.TestCase):  

    #继承之后，重写一下，把参数传递到unittest里面

    def __init__(self, methodName='runTest', parame1=None, parame2=None,parame3=None):  

        super(ParametrizedTestCase, self).__init__(methodName)  

        self.parame1 = parame1
        self.parame2 = parame2
        self.parame3 = parame3


    @staticmethod  

    def parametrize(testcase_klass, parame1=None, parame2=None,parame3=None):  

        testloader = unittest.TestLoader()  

        testnames = testloader.getTestCaseNames(testcase_klass)  

        suite = unittest.TestSuite()  

        for name in testnames:  

            suite.addTest(testcase_klass(name, parame1=parame1, parame2=parame2,parame3=None))  

        return suite  

  
'''
以下为ParametrizedTestCase方法在测试类中的使用
'''
 
class TestOne(ParametrizedTestCase):  

    def test_first(self):  

        print ('parame =', self.parame1) 

        #self.assertEqual(1, 1)  

   

    def test_two(self):

        print ('parame =', self.parame2)   

        #self.assertEqual(2, 2)  

class TestTwo(ParametrizedTestCase):  

    def test_first(self):  

        print ('parame =', self.parame1) 

        #self.assertEqual(1, 1)  

   

    def test_two(self):

        print ('parame =', self.parame3) 


if __name__ == '__main__':

    suite = unittest.TestSuite()  

    suite.addTest(ParametrizedTestCase.parametrize(TestOne, parame1=2, parame2=2,parame3=None))  

    suite.addTest(ParametrizedTestCase.parametrize(TestTwo, parame1=2, parame2=2,parame3=None))
    unittest.TextTestRunner(verbosity=2).run(suite)
