#用不同字母代表不同的道路，两个字母的组合表示路线规划，将所有可能的路线写在一张纸上，之间有冲突的两条路线用直线连接起来。
# 得到路线冲突图。
#行驶方向分组原则
# 1、同属一组的各个方向行驶的车辆，均可以同时行驶，不出现相互交错的行驶路线，保证安全性。
# 2、所做的分组尽可能大，减少分组数，降低红绿灯之间的转换次数，以提高路口的效率。

def coloring(G):
    color = 0
    groups = set()
    verts = vertices(G)      #图的表示
    while verts:
        new_group = set()
        for v in list(verts):
            if not_adjacent_with_set(v, new_group, G):       #图的操作
                new_group.add(v)
                verts.remove(v)
        groups.add((color, new_group))
        color += 1
    return groups

