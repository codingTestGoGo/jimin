import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int max = nums.length/2;
        int count = 0; // 종류 개수 세기
        HashMap<Integer, Integer> map = new HashMap<>(); // 종류, 수
        for (int kind : nums) {
            if (map.containsKey(kind)) {
                map.put(kind, map.get(kind) + 1);
            }
            else {
                map.put(kind, 1); 
            }
        }

        for (int key : map.keySet()) {
            // System.out.println(map.get(key));
            count++;
        }
        if (max >= count) {
            answer = count;
        }
        else {
            answer = max;
        }
        return answer;
    }
}