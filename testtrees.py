#coding=utf-8
import trees
import unittest

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
        
        
if __name__ == "__main__":
    unittest.main()
