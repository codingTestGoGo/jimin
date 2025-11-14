import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>(); // 종류, 개수
        for (String[] cloth : clothes) {
            if (map.containsKey(cloth[1])) {
                map.put(cloth[1], map.get(cloth[1]) + 1);
            }
            else {
                map.put(cloth[1], 1);    
            }
            
        }
        int[] comb = new int[map.size()];
        int i = 0;
        for (String key : map.keySet()) {
            System.out.println(key + " " + map.get(key));
            comb[i] = map.get(key) + 1;
            i++;
        }
        for (i = 0; i < map.size(); i++) {
            answer *= comb[i];
        }
        return answer - 1;
    }
}