#coding=utf-8
import numpy as np
import operator
import os

def classify0(inx, dataset, labels, k):
    diff_matrix = np.tile(inx, (dataset.shape[0],1)) - dataset
    distance = ((diff_matrix ** 2).sum(axis=1))**0.5
    distindices = distance.argsort()
    km = min(k, dataset.shape[0])
    classcount = {}
    for i in range(km):
        label = labels[distindices[i]]
        classcount[label] = classcount.get(label, 0) + 1
    return sorted(classcount.iteritems(), key=operator.itemgetter(1), reverse=True)[0][0]
    
def file2matrix(filename, number_of_attributes):
    fr = open(filename)
    array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    return_mat = np.zeros((number_of_lines, number_of_attributes))
    class_label_vector = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split("\t")
        return_mat[index,:] = list_from_line[:number_of_attributes]
        class_label_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_label_vector
    
def autonorm(dataset):
    min_vals = dataset.min(0)
    max_vals = dataset.max(0)
    ranges = max_vals - min_vals
    norm_dataset = np.zeros(np.shape(dataset))
    m = dataset.shape[0]
    norm_dataset = dataset - np.tile(min_vals, (m,1))
    norm_dataset =  norm_dataset/np.tile(ranges, (m,1))
    return norm_dataset, ranges, min_vals

def classify_person():
    result_list = ['not at all', 'in small doses', 'in large doses']
    percent_tats = float(raw_input("percentage of time spent playing video games?"))
    ffmiles = float(raw_input("frequent flier miles earned per year?"))
    icecream = float(raw_input("liters of icecream cosumed per year?"))
    datingdataset, datinglabels = file2matrix('machinelearninginaction/Ch02/datingTestSet2.txt', 3)
    normMat, ranges, minvals = autonorm(datingdataset)
    inarr = np.array([ffmiles, percent_tats, icecream])
    classifier_result = classify0((inarr-minvals)/ranges, normMat, datinglabels, 3)
    print "You will probably like this person:%s"%result_list[classifier_result-1]
    
    
def img2vector(filename):
    return_vect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            return_vect[0, 32*i+j] = int(linestr[j])
    return return_vect

def handwritingclassify():
    hwLabels = []
    training_file_list = os.listdir("machinelearninginaction/Ch02/trainingDigits")
    m = len(training_file_list)
    training_mat = np.zeros((m, 1024))
    for i in range(m):
        file_name_str = training_file_list[i]
        filestr = file_name_str.split(".")[0]
        class_num_str = filestr.split("_")[0]
        hwLabels.append(class_num_str)
        training_mat[i,:] = img2vector("machinelearninginaction/Ch02/trainingDigits/%s" % file_name_str)
    test_file_list = os.listdir("machinelearninginaction/Ch02/testDigits")
    error_count = 0.0
    mtest = len(test_file_list)
    for i in range(mtest):
        file_name_str = test_file_list[i]
        filestr = file_name_str.split(".")[0]
        class_num_str = filestr.split("_")[0]
        vector_under_test = img2vector("machinelearninginaction/Ch02/testDigits/%s" % file_name_str)
        classifierResult = classify0(vector_under_test, training_mat, hwLabels, 5)
        print "the classifier came back with: %s, the real answer is: %s" %(classifierResult, class_num_str)
        if classifierResult != class_num_str:
            error_count += 1
    print "the total number of erros is: %d" % error_count
    print "the total error rate is: %f" % (error_count/float(mtest))
        