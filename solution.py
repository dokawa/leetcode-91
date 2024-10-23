class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 1
        # n - 1, n, one, two
        for i in range(len(s) - 1, -1, -1):
            tmp = one

            if s[i] == '0':
                one = 0

            if (i + 1 < len(s) and
                (s[i] == "1" or s[i] == "2" and
                 s[i + 1] in {"0", "1", "2", "3", "4", "5", "6"})):
                one += two

            two = tmp

        return one
