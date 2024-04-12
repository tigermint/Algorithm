import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int width = 0;
        int height = 0;
        
        for(int[] size : sizes){
            int a = Math.max(width, size[0]) * Math.max(height, size[1]);
            int b = Math.max(width, size[1]) * Math.max(height, size[0]);
            
            if(a > b){
                width = Math.max(width, size[1]);
                height = Math.max(height, size[0]);
            }else{
                width = Math.max(width, size[0]);
                height = Math.max(height, size[1]);
            }
        }

        return width * height;
    }
}