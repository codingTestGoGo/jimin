class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    
    // idx: 몇 번째 숫자까지 썼는지
    // sum : 숫자합
    private int dfs(int[] numbers, int target, int idx, int sum) {
        if (idx == numbers.length) {
            if (sum == target)
                return 1;
            else
                return 0;
        }
        // 현재 숫자 더하는 경우
        int cnt1 = dfs(numbers, target, idx + 1, sum + numbers[idx]);
        int cnt2 = dfs(numbers, target, idx + 1, sum - numbers[idx]);
        return cnt1 + cnt2;
        
    }
}