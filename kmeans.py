#coding=utf-8
import numpy as np

def load_dataset(filename):
    datamat = []
    fr = open(filename)
    for line in fr.readlines():
        curline = line.strip().split("\t")
        fltline = map(float,curline)
        datamat.append(fltline)
    return datamat
    
    
def dist_eclud(veca, vecb):
    return np.sqrt(sum(np.power(veca - vecb, 2)))
    

def rand_cent(dataset, k):
    n = np.shape(dataset)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minj = min(dataset[:,j])
        rangej = float(max(dataset[:,j]) - minj)
        centroids[:,j] = minj + rangej * np.random.rand(k,1)
    return centroids
    
    
def kmeans(dataset, k, distmeas=dist_eclud, create_cent = rand_cent):
    m = np.shape(dataset)[0]
    cluster_assment = np.mat(zeros((m,2)))
    centroids = create_cent(dataset, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = np.inf;
            min_index = -1
            for j in range(k):
                dist_ji = distmeas(centroids[j,:], dataset[i,:])
                if dist_ji < min_dist:
                    min_dist = dist_ji
                    min_index = j
            if cluster_assment[i,0] != min_index:
                cluster_changed = True
            cluster_assment[i,:] = min_index,min_dist**2
        print centroids
        for cent in range(k):
            pts_in_clust = dataset[np.nonzero(cluster_assment[:,0].A==cent)[0]]
            centroids[cent, :] = np.mean(pts_in_clust, axis=0)
    return centroids, cluster_assment
