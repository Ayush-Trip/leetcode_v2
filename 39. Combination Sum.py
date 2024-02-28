class Solution:
    def combinationSum(self, arr: List[int], t: int) -> List[List[int]]:
        i=0
        curr=[]
        ans=[]
        self.fun(i,t,arr,curr,ans)
        return ans
    def fun(self,i,t,arr,curr,ans):
        if t==0 :
            l=curr[:]
            ans.append(l)
            return 
        if t<0:
            return
        if i>=len(arr):
            return
        self.fun(i+1,t,arr,curr,ans)
        curr.append(arr[i])
        t-=arr[i]
        self.fun(i,t,arr,curr,ans)
        curr.pop()