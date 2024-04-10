import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int maxSelect = nums.length / 2;
        Set<Integer> numsSet = new HashSet<>();
        
        for(int num : nums){
            numsSet.add(num);
        }
        
        if(maxSelect <= numsSet.size()){
            return maxSelect;
        }
        return numsSet.size();
    }
}