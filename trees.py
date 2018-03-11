#coding=utf-8
from math import log
from collections import Counter

def calc_shannon_ent(dataset):
    num_entries = len(dataset)
    label_counts = Counter([feat_vec[-1] for feat_vec in dataset])
    shannon_ent = 0.0
    for key in label_counts.iterkeys():
        prob = float(label_counts[key])/num_entries
        shannon_ent += prob * log(prob, 2)
    return shannon_ent

    
def split_dataset(dataset, axis, valuel):
    ret_dataset = []
    for feat_vec in dataset:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis+1:])
    return ret_dataset
   

def choose_best_feature_to_split(dataset):
    num_features = len(dataset[0]) - 1
   