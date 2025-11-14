import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int n = id_list.length;
        int[] answer = new int[n];
        // 1. 유저 이름 -> index 매핑
        HashMap<String, Integer> idx = new HashMap<>();
        for (int i = 0; i < n; i++) {
            // reporter_list[i] = new ArrayList<>();
            idx.put(id_list[i], i);
        }
        
        // 2. (신고자, 피신고자) 중복 제거 !!
        HashSet<String> uniqueReport = new HashSet<>();
        for (String r : report) {
            uniqueReport.add(r);
        }
        
        // 3. 각 유저가 몇 번 신고 당햇는지 카운ㄷ트
        int[] report_cnt = new int[n];
        for (String r : uniqueReport) {
            String[] tmp = r.split(" ");
            String reporter = tmp[0];
            String reported = tmp[1];
            int reported_idx = idx.get(reported);
            report_cnt[reported_idx]++;
        }
        for (String r : uniqueReport) {
            String[] tmp = r.split(" ");
            String reporter = tmp[0];
            String reported = tmp[1];
            int reporter_idx = idx.get(reporter);
            int reported_idx = idx.get(reported);
            if (report_cnt[reported_idx] >= k) {
                answer[reporter_idx]++;
            }
        }
        
        
        return answer;
    }
}