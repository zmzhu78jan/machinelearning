#coding=utf-8
from math import log
from collections import Counter
import operator

def calc_shannon_ent(dataset):
    num_entries = len(dataset)
    label_counts = Counter([feat_vec[-1] for feat_vec in dataset])
    shannon_ent = 0.0
    for key in label_counts.iterkeys():
        prob = float(label_counts[key])/num_entries
        shannon_ent += -prob * log(prob, 2)
    return shannon_ent

    
def split_dataset(dataset, axis, value):
    ret_dataset = []
    for feat_vec in dataset:
        if feat_vec[axis] == value:
            reduced_feat_vec = feat_vec[:axis]
            reduced_feat_vec.extend(feat_vec[axis+1:])
            ret_dataset.append(reduced_feat_vec)
    return ret_dataset
   

def choose_best_feature_to_split(dataset):
    num_features = len(dataset[0]) - 1
    base_entropy = calc_shannon_ent(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in dataset]
        unique_vals = set(feat_list)
        new_entropy = 0.0
        for value in unique_vals:
            sub_dataset = split_dataset(dataset, i, value)
            prob = len(sub_dataset)/float(len(dataset))
            new_entropy = prob * calc_shannon_ent(sub_dataset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature
    
    
def majority_cnt(class_list):
    class_count = Counter(class_List)
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]
    
    
def create_tree(dataset, labels):
    class_list = [example[-1] for example in dataset]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(dataset[0]) == 1:
        return majority_cnt(class_list)
    best_feat = choose_best_feature_to_split(dataset)
    best_feat_label = labels[best_feat]
    mytree = {}
    mytree[best_feat_label] = {}
    del labels[best_feat]
    feat_values = [example[best_feat] for example in dataset]
    unique_vals = set(feat_values)
    for value in unique_vals:
        sublabels = labels[:]
        mytree[best_feat_label][value] = create_tree(split_dataset(dataset, best_feat, value), sublabels)
    return mytree
        
        
def classify(input_tree, feat_labels, test_vec):
    firststr = input_tree.keys()[0]
    second_dict = input_tree[firststr]
    feat_index = feat_labels.index(firststr)
    class_label = None
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == "dict":
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
    return class_label

    
def store_tree(input_tree, filename):
    import pickle
    fw = open(filename, "w")
    pickle.dump(input_tree, fw)
    fw.close()

    
def grab_tree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
    
    
    
    