class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        output = 0
        for sentence in sentences:
            arr = sentence.split(" ")
            num = len(arr)
            if num > output:
                output = num
        return output


solution = Solution()
solution.mostWordsFound(["alice and bo7b love leetcode", "i think so too", "this is great thanks very much"])