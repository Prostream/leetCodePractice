''' 1.相邻房子不能同色
    2.对称位置不能同色
'''
MOD = 10**9 + 7

def count_colorings(n):
    """
    n: 偶数，街上房子的数量
    返回: 满足条件的染色方案数，对 MOD 取模
    """
    # n为偶数，故房子可以分为 n/2 对
    half = n // 2
    # 第一对有6种方式，每增加一对有3种选择
    return (6 * pow(3, half - 1, MOD)) % MOD

# 示例测试
if __name__ == "__main__":
    n = 4  # 例如 4 栋房子
    print(count_colorings(n))  # 期望输出: 18
