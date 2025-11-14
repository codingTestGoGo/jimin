import java.util.*;
class Solution {
    static boolean[] visited; // 자동으로 0 초기화
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(n, computers, i);
                answer += 1;
            }
        }
        return answer;
    }
    public void dfs(int n, int[][] computers, int now) {
        visited[now] = true;
        for(int i = 0; i < n; i++) {
            if (!visited[i] && computers[now][i] == 1) {
                dfs(n, computers, i);
                // visited[i] = true;
            }
        }
        
    }
}