import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0, max = 0;
        int len = s.length();
        Set<Character> tracker = new HashSet();
        while(i <len && j < len){
            if(!tracker.contains(s.charAt(i))){
                tracker.add(s.charAt(i));
                i++;
                max = Math.max(max, tracker.size());
            }
            else{
                tracker.remove(s.charAt(j));
                j++;
            }
        }
        return max;
    }
}