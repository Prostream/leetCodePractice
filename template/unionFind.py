#并查集的模板，并查集就是看两个元素是不是在一个集合里，性能上采用短链的方案，union换挂也有一定的优化效果
class unionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))#[0，1,2,3,4,5,6]表示每个位置index的parent就是自己
        self.size = [0]*n #表示每个位置的size目前是0

    #目的是找到x对应的parent
    #[0,1,2,3,4,5,6] x=3
    def find(self,x):
        #利用递归进行路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    #目的是联合两个集合
    def union(self, x, y):
        find_x = self.find(x)
        find_y = self.find(y)
        find_x = self.parent[find_y]
        #如果对性能有要求，那么就把小链挂在大链上

    def isSame(self, x, y):
        return self.find(x) == self.find(y)


#kruskal算法来使用这个并查集
#kruskal算法是基于边的，用来生成MST的算法，基于贪心和最小堆
def kruskal(edges, n):
    edges = sorted(edges, key=lambda x:x[2])
    parent = list(range(n))
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    def isSame(x, y):
        return find(x) == find(y)

    count = 0
    total = 0
    for u,v,w in edges:
        if isSame(u,v):
            continue
        if count < n-1:
            count += 1
            total += w
            union(u,v)
    return total

if __name__ == "__main__":
    #       A
    # B           C
    #       D
    #
    edges, n = [[0,1,2],[0,2,4],[1,3,2],[2,3,1]], 4
    print(kruskal(edges, n))