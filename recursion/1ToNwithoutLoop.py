
class Solution:    
    def printNos(self, n, i=1):
        
        if i > n:
            return 
        
        print(i, end=" ")
       
        self.printNos(n, i+1)



if __name__ == "__main__":
    n = int(input("Enter n: "))
    ob = Solution()
    ob.printNos(n)
