import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] count = {0, 0, 0};
        
        int[] s1 = {1, 2, 3, 4, 5};
        int[] s2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] s3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        for(int i = 0; i < answers.length; i++){
            if(answers[i] == s1[i % s1.length]){
                count[0] += 1;
            }
            if(answers[i] == s2[i % s2.length]){
                count[1] += 1;
            }
            if(answers[i] == s3[i % s3.length]){
                count[2] += 1;
            }
        }
        int maxValue = Arrays.stream(count).max().getAsInt();
        
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < count.length; i++){
            if(maxValue == count[i]){
                answer.add(i + 1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}