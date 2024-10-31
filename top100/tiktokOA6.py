#
class Solution:
    def countMinimumCharactersForVideoIDs(self, idStream, videoIds):
        # 记录每个数字最后一次出现的位置
        last_occurrences = {}
        for index, char in enumerate(idStream):
            last_occurrences[char] = index
        results = []
        # 检查每个 videoId
        for videoId in videoIds:
            max_last_occurrence = -1
            # 对于 videoId 中的每个数字，找出需要的最远位置
            for char in videoId:
                if char in last_occurrences:
                    max_last_occurrence = max(max_last_occurrence, last_occurrences[char])
                else:
                    # 如果 idStream 中没有这个数字，直接标记为无法完成
                    max_last_occurrence = -1
                    break
            # 如果找到了所有字符的有效位置，则计算长度
            if max_last_occurrence != -1:
                results.append(max_last_occurrence + 1)  # 加1因为索引从0开始
            else:
                results.append(-1)
        return results

if __name__ == '__main__':
    s = Solution()
    videoIds = ["088","364","07"]
    print(s.countMinimumCharactersForVideoIDs("064819848398",videoIds))


