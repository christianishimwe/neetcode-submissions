class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        ["ab", "cd"]

        "2#ab3#cd
        what about this input: ["2#ab", "#cd"] -> 4#2#ab

        """
        for i, word in enumerate(strs):
            strs[i] = str(len(word)) + "#" + word
        
        return "".join(strs)

            
    def decode(self, s: str) -> List[str]:
        l = len(s)
        i = 0
        output = []

        while i < l:
            str_here = []
            num = []
            # first read of the number
            while i < l and s[i] != "#":
                num.append(s[i])
                i += 1
            # we go to the sharp edge
            num = int("".join(num))
            # now read the string
            count = 0
            # skip the #
            i += 1
            while count < num:
                str_here.append(s[i])
                i += 1
                count += 1
            # build str_here
            str_here = "".join(str_here)
            output.append(str_here)
        return output



