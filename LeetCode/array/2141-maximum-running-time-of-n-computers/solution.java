class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long sum=0;
        long result=0;
        for(int i=0;i<batteries.length;i++){
            sum=sum+batteries[i];
        }
        long max= sum/n;
        long min=0;
        long mid=(max+min+1)/2;
        while(min<max){
        sum=0;
        for(int i=0;i<batteries.length;i++){
            sum=sum+Math.min(batteries[i],mid);
        }

        if(sum>=mid*n){
            result=mid;
            min=mid;
            mid=(max+min+1)/2;
            continue;
        }
        else{
            max=mid-1;
            mid=(max+min+1)/2;
            continue;
        }
        }

        return result;
    }
}
