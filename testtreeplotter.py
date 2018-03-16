#coding=utf-8
import unittest
import treeplotter

class TestTreeplotter(unittest.TestCase):

    def test_get_num_leafs(self):
        mytree = {u"属性1":{1:{u"属性2":{0:1,1:3}},2:3}}
        self.assertEqual(treeplotter.get_num_leafs(mytree), 3)
        
    def test_get_tree_depth(self):
        mytree = {u"属性1":{1:{u"属性2":{0:1,1:3}},2:3}}
        self.assertEqual(treeplotter.get_tree_depth(mytree), 2)
                
    def test_create_plot(self):
        mytree = {u"属性1":{1:{u"属性2":{0:1,1:3}},2:3}}
        treeplotter.create_plot(mytree)

if __name__ == "__main__":
    unittest.main()
    