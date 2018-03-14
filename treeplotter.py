#coding=utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']


decision_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")



def plot_node(nodetxt, center_pt, parent_pt, nodetype):
    create_plot.ax1.annotate(nodetxt, xy=parent_pt, xycoords="axes fraction", xytext=center_pt, textcoords="axes fraction", \
        va="center", ha="center", bbox=nodetype, arrowprops=arrow_args)
    

def create_plot():
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node(u"决策节点", (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node(u"叶节点", (0.8,0.1), (0.3, 0.8), leaf_node)
    plt.show()
    
    