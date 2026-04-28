class Solution():
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        data =s.split()
        for i in range(len(data)) :
            data[i]=data[i][::-1]
        return " ".join(data)


s = "Let's take LeetCode contest" 
# s = "Mr Ding"
#"s'teL ekat edoCteeL tsetnoc"
solt =Solution()
print(solt.reverseWords(s))




