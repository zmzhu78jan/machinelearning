#coding=utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']


decision_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")



def plot_node(nodetxt, center_pt, parent_pt, nodetype):
    create_plot.ax1.annotate(nodetxt, xy=parent_pt, xycoords="axes fraction", xytext=center_pt, textcoords="axes fraction", \
        va="center", ha="center", bbox=nodetype, arrowprops=arrow_args)
    

def get_num_leafs(mytree):
    num_leafs = 0
    firststr = mytree.keys()[0]
    second_dict = mytree[firststr]
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == "dict":
            num_leafs += get_num_leafs(second_dict[key])
        else:
            num_leafs += 1
    return num_leafs
    
def get_tree_depth(mytree):
    maxdepth = 0
    firststr = mytree.keys()[0]
    second_dict = mytree[firststr]
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == "dict":
            this_depth = 1 + get_tree_depth(second_dict[key])
        else:
            this_depth = 1
        if this_depth > maxdepth:
            maxdepth = this_depth
    return maxdepth
    
    
def plot_mid_text(cntr_pt, parent_pt, txt_string):
    x_mid = (parent_pt[0] - cntr_pt[0])/2.0 + cntr_pt[0]
    y_mid = (parent_pt[1] - cntr_pt[1])/2.0 + cntr_pt[1]
    create_plot.ax1.text(x_mid, y_mid, str(txt_string))
    
    
def plot_tree(mytree, parent_pt, nodetxt):
    num_leafs = get_num_leafs(mytree)
    depth = get_tree_depth(mytree)
    firststr = mytree.keys()[0]
    cntr_pt = (plot_tree.xoff + (1.0 + float(num_leafs))/2.0/plot_tree.total_w, plot_tree.yoff)
    plot_mid_text(cntr_pt, parent_pt,nodetxt)
    plot_node(firststr, cntr_pt, parent_pt, decision_node)
    second_dict = mytree[firststr]
    plot_tree.yoff = plot_tree.yoff - 1.0/plot_tree.total_d
    for key in second_dict.keys():
        if type(second_dict[key]).__name__ == "dict":
            plot_tree(second_dict[key], cntr_pt, str(key))
        else:
            plot_tree.xoff = plot_tree.xoff + 1.0/plot_tree.total_w
            plot_node(second_dict[key], (plot_tree.xoff, plot_tree.yoff), cntr_pt, leaf_node)
            plot_mid_text((plot_tree.xoff, plot_tree.yoff), cntr_pt, str(key))
    plot_tree.yoff = plot_tree.yoff + 1.0/plot_tree.total_d


def create_plot(intree):
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    create_plot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plot_tree.total_w = float(get_num_leafs(intree))
    plot_tree.total_d = float(get_tree_depth(intree))
    plot_tree.xoff = -0.5/plot_tree.total_w
    plot_tree.yoff = 1.0
    plot_tree(intree, (0.5,1.0), '')
    plt.show()
    
    