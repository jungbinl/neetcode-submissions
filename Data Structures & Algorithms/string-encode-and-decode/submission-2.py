class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in strs:
            a = a + str(len(i)) + "#" + i
        return a

    def decode(self, s: str) -> List[str]:
        result = list()
        if s == "":
            return result
        else:
            while s.find("#") != -1:
                index = s.find("#")
                nums = index -1
                while s[nums].isdecimal() | nums > -1:
                    nums -= 1
                word_nums = int(s[nums+1:index])
                word = s[index+1:word_nums+index+1]
                # print(word)
                result.append(word)
                s = s[word_nums+index +1:]
                # print(s)
            return result
