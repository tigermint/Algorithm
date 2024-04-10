import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        for(int num : arr){
            if(!stack.isEmpty() && stack.peek() == num){
                continue;
            }
            stack.push(num);
        }
        List<Integer> list = new ArrayList<>(stack);
        return list.stream().mapToInt(i -> i).toArray();
        
    }
}