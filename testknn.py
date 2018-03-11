#coding=utf-8
import knn
import unittest
import numpy as np

class Tester(unittest.TestCase):
    def testknn(self):
        dataset = np.array(([0,0],[0.1,0.1],[0,0.1],[0.1,0],[1,1],[1.1,1],[0.9,1],[1,0.9]))
        labels = ['A','A','A','A','B','B','B','B']
        inx = [0.12,0.03]
        self.assertEqual(knn.classify0(inx,dataset,labels,4),'A')
        
    def testclassifyperson(self):
        knn.classify_person()
        
    def testclassifyhandwriting(self):
        knn.handwritingclassify()

if __name__ == "__main__":
    unittest.main()