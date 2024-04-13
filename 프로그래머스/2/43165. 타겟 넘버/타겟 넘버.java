class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, target, 0);
        return answer;
    }
    
    public void dfs(int[] numbers, int index, int target, int sum){
        //종료 조건
        if(index == numbers.length){
            if(sum == target){
                answer++;
            }
            return;
        }
        
        dfs(numbers, index + 1, target, sum + numbers[index]);
        dfs(numbers, index + 1, target, sum - numbers[index]);
    }
    
    
}