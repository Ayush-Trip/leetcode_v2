//User function Template for Java//User function Template for Java
class Solution{
    ArrayList<Integer> subsetSums(ArrayList<Integer> arr, int N){
        // code here
        ArrayList <Integer> ans = new ArrayList <Integer>();
        int i=0;
        int s=0;
        fun(arr,i,ans,s);
        return ans;
    
    }
    void fun(ArrayList<Integer> arr , int i , ArrayList<Integer> ans , int s){
        if(i>=arr.size()){
            ans.add(s);
            return;
        }
        fun(arr , i+1 , ans , s+arr.get(i));
        fun(arr , i+1, ans, s);
    }
        
    
}