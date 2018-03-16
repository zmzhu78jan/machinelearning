#coding=utf-8
import trees
import unittest
import treeplotter

class TreesTest(unittest.TestCase):
    def create_my_dataset(self):
        my_dataset = [[1,1,'yes'],[1,1,'yes'],[0,1,'no'],[0,1,'no'],[1,0,'no']]
        labels = ["no surfacing", "flippers"]
        return my_dataset, labels
        
    def test_choose_best_feature_to_split(self):
        my_dataset, labels = self.create_my_dataset()
        self.assertEqual(trees.choose_best_feature_to_split(my_dataset), 0)
        self.assertEqual(trees.split_dataset(my_dataset, 0, 1), [[1,'yes'],[1,'yes'],[0,'no']])
        self.assertEqual(trees.create_tree(my_dataset, labels), {"no surfacing":{1:{"flippers":{1:"yes",0:"no"}},0:"no"}})
        
    def test_classify(self):
        mytree = {u"属性1":{1:{u"属性2":{0:1,1:3}},2:3}}
        labels = [u"属性1", u"属性2"]
        test_vec = [2,0]
        self.assertEqual(trees.classify(mytree, labels, test_vec), 3)
        test_vec = [1,1]
        self.assertEqual(trees.classify(mytree, labels, test_vec), 3)
        test_vec = [3,1]        
        self.assertIsNone(trees.classify(mytree, labels, test_vec))
        
    def test_store_tree(self):
        mytree = {u"属性1":{1:{u"属性2":{0:1,1:3}},2:3}}
        filename = "mytree.dat"
        trees.store_tree(mytree, filename)
        mytree2 = trees.grab_tree(filename)
        self.assertEqual(mytree, mytree2)
        
    def test_examples(self):
        fr = open("machinelearninginaction/Ch03/lenses.txt")
        lenses = [inst.strip().split("\t") for inst in fr.readlines()]
        lenses_labels = ["age", "prescript", "astigmatic", "tearrate"]
        lenses_tree = trees.create_tree(lenses, lenses_labels)
        treeplotter.create_plot(lenses_tree)
        
        
if __name__ == "__main__":
    unittest.main()
