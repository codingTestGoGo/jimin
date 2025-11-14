import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>(); // 참가자이름, 이름등장횟수
        for (String str : participant) {
            if (map.containsKey(str)) {
                map.put(str, map.get(str) + 1);
            }
            else {
                map.put(str, 1);
            }
        }
        for (String str : completion) {
            if (map.containsKey(str)) {
                map.put(str, map.get(str) - 1);
            }
        }
        // for (String key : map.keySet()) {
        //     System.out.println(key + " " + map.get(key));
        // }
        for (String str : map.keySet()) {
            if (map.get(str) != 0) {
                answer = str;
                break;
            }
        }
    return answer;
    }
}