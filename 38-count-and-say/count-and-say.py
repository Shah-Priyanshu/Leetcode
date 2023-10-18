def hello(n):
        if(n==1):
            return '1'
        else:
            res=hello(n-1)+'@'
            aux=""
            c=1
            for i in range(len(res)-1):
                    if(res[i]==res[i+1]):
                           c+=1
                    else:
                        aux+=str(c)+res[i]
                        c=1
                         
            return aux
class Solution(object):
    def countAndSay(self, n):
        return hello(n)