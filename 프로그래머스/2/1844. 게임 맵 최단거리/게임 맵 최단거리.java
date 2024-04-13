import java.util.*;

class Solution {
    final int[] dx = {-1, 1, 0, 0};
    final int[] dy = {0, 0, -1, 1};
    
    public int solution(int[][] maps) {
        int[][] visited = new int[maps.length][maps[0].length];
        
        bfs(maps, visited);
        
        int answer = visited[maps.length - 1][maps[0].length - 1];
        return answer == 0 ? -1 : answer;
    }
    
    private void bfs(int[][] maps, int[][] visited){
    
        visited[0][0] = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        
        while(!queue.isEmpty()){
            int[] node = queue.remove();
            
            for(int i = 0; i < 4; i ++){
                int nx = node[0] + dx[i];
                int ny = node[1] + dy[i];
                
                if((0 <= nx && nx < maps.length) 
                   && (0 <= ny && ny < maps[0].length) 
                   && visited[nx][ny] == 0 
                   && maps[nx][ny] == 1){
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = visited[node[0]][node[1]] + 1;
                }
            }
        }
    }
}