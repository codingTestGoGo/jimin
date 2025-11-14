import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean visited[] = new boolean[n]; // 컴퓨터 번호 방문 여부 
        
        for (int i = 0; i < n; i++) visited[i] = false;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                queue.offer(i);
                visited[i] = true;
                answer += 1;
            }
            while(!queue.isEmpty()) {
                int next = queue.poll();
                for (int j = 0; j < n; j++) {
                    if (visited[j] == false && computers[next][j] == 1) {
                        queue.offer(j);
                        visited[j] = true;   
                    }
                }
            }
        }
        
        return answer;
    }
}