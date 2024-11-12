from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        # 基本参数
        n, m, w = len(s), len(words), len(words[0])
        total_len = m * w
        word_count = Counter(words)
        result = []

        # 分段滑动窗口
        for i in range(w):
            left = i
            right = i
            current_count = Counter()

            while right + w <= n:
                # 从右端提取一个单词
                word = s[right:right + w]
                right += w

                # 如果单词在词典中，加入当前窗口的计数
                if word in word_count:
                    current_count[word] += 1

                    # 若单词出现次数超过要求，则移动左边界
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + w]] -= 1
                        left += w

                    # 检查窗口长度是否符合要求
                    if right - left == total_len:
                        result.append(left)
                else:
                    # 如果当前单词不在词典中，重置窗口
                    current_count.clear()
                    left = right

        return result
