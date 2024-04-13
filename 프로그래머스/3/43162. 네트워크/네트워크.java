import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for(int i = 0; i < n; i++){
            //방문하지 않았다면 방문해서 dfs 돌리고 판단
            if(!visited[i]){
                dfs(i, computers, visited, n);
                answer++;
            }
        }
        return answer;
    }
    
    private void dfs(int visitedIndex, int[][] computers, boolean[] visited, int n){
        visited[visitedIndex] = true;
        for(int i = 0; i < n; i++){
           if(computers[visitedIndex][i] == 1 && visited[i] == false){
               dfs(i, computers, visited, n);
           }
        }
    }
}