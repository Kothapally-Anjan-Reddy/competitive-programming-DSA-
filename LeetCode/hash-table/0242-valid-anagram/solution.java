class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()){
            return false;
        }

        char[] s_letters=s.toCharArray();
        char[] t_letters=t.toCharArray();
        int[] arr=new int[26];

        for(char c:s_letters){
            arr[c-'a']++;
        }

        for(char c:t_letters){
            arr[c-'a']--;
        }

        for(int i:arr){
            if(i!=0){
                return false;
            }
        }

        return true;
    }
}
