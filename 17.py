class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
            #1) This was a little tricky in the beginning as this was the first question I started off with. 
            1) Go through every letter in the given digits, get the letters associated to it, add it to a temporary word and continue.
            2) Once the limit of the temporary word reaches the length of the given digits. Add to the final list 
        """
        
        numpad ={2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}
        diglen = len(digits)
        if diglen == 0:
            return []
        to_ret = []
        temp_word = ""
        digits_int = digits
        def recurse(index, digits_int, to_ret, temp_word):
            if len(temp_word) == diglen:
                to_ret.append(temp_word)
                return 
            for i in numpad[int(digits_int[index])]:
                recurse(index + 1, digits_int, to_ret, temp_word+i)
                
        recurse(0, digits_int, to_ret, temp_word)
        return to_ret
            