class Solution:
    def subsetSums(self, arr, N):
        # code here
        ans=[]
        i=0
        s=0
        self.fun(arr,i,s,ans)
        return ans
    def fun(self,arr,i,s,ans):
        if (i>=len(arr)):
            ans.append(s)
            return
        self.fun(arr,i+1,arr[i]+s,ans)
        self.fun(arr,i+1,s,ans)
        