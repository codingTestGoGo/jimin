import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, -1}); // (sum, idx)
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int sum = cur[0];
            int idx = cur[1];
            if (idx == numbers.length - 1) {
                if (sum == target) {
                    answer += 1;
                    continue;
                }
                else {
                    answer += 0;
                    continue;
                }
            }
            queue.offer(new int[]{cur[0] + numbers[idx + 1], idx + 1});
            queue.offer(new int[]{cur[0] - numbers[idx + 1], idx + 1});
        }
        
        return answer;
    }

}