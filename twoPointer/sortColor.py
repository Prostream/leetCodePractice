def sort_colors(colors):
    # 荷兰国旗问题 Dijkstra
    # O（n）时间复杂度 O（1）空间复杂度
    # 声明3个pointer 2前1后
    n = len(colors)
    start = 0
    current = 0
    end = n-1
    # start current end

    # start=red cur=green end=blue
    # 循环比较 cur如果是1单纯c进位，是0和start换位，然后start和cur都进位，是2则和end换位，单纯end退位（这里的进位退位比较关键，
    # 但 mid 不动，因为交换过来的元素还没有检查过，可能仍需要进一步处理。）
    # 为什么是<=而不是<呢，因为mid和end交换后，指向同一个位置，这个时候可能还需要把这个数交给start，需要=再跑一次循环才能做完整
    while current <= end:
        if colors[current] == 0:
            colors[current],colors[start] = colors[start],colors[current]
            current=current+1
            start=start+1
        elif colors[current] == 2:
            colors[current], colors[end] = colors[end], colors[current]
            end=end-1
        else:
            current=current+1
    return colors


# Driver code
def main():
    sort_colors([2,1,1,0,0])

if __name__ == '__main__':
    main()