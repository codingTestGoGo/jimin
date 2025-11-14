import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        StringBuilder edit_id = new StringBuilder();
        
        // 1: 대->소문자
        answer = new_id.toLowerCase();
        edit_id.append(answer);
        System.out.println("1: " + edit_id);
        
        // 2: 문자 제거
        // String[] list = "!@#$%^&*()=+[{]}:?,<>/".split("");
        // for (String c : list) {
        for (int i = edit_id.length() - 1; i >= 0; i-- ) {
            char ch = edit_id.charAt(i);
            // if (c.isEmpty()) continue; 
            // int idx = edit_id.indexOf(c);
            
            if (ch == '~' || ch == '!' || ch == '@' || ch == '#' ||
               ch == '$' || ch == '%' || ch == '^' ||
               ch == '&' || ch == '*' || ch == '(' || 
               ch == ')' || ch == '=' || ch == '+' ||
               ch == '[' || ch == '{' || ch == ']' ||
               ch == '}' || ch == ':' || ch == '?' ||
               ch == ',' || ch == '<' || ch == '>' ||
               ch == '/') {
                // int idx = edit_id.indexOf(ch);
                edit_id.deleteCharAt(i);   
            }
                
            // while (idx != -1) {
            //     edit_id.deleteCharAt(idx); // idx에 있는 문자 삭제
            //     idx = edit_id.indexOf(c);
            // }
        }
        System.out.println("2: " + edit_id);
        
        // 3: 마침표 2번 연속 -> 하나로 치환
        for (int i = 0; i < edit_id.length() - 1; i++) {
            if (edit_id.charAt(i) == '.' && edit_id.charAt(i + 1) == '.') {
                edit_id.deleteCharAt(i);
                i--;
            } 
        }
        System.out.println("3: " + edit_id);
        
        // 4. 마침표 처음&끝 -> 삭제
        if (edit_id.length() > 0 && edit_id.charAt(0) == ('.'))
                edit_id.deleteCharAt(0);
        if (edit_id.length() > 0 && edit_id.charAt(edit_id.length() - 1) == ('.')) 
                edit_id.deleteCharAt(edit_id.length() - 1);    
        System.out.println("4: " + edit_id);

        
        // 5. 빈문자열 -> a 대입
        if (edit_id.length() == 0)
            edit_id.append('a');
        
        // 6. edit_id.length() >= 16
        if (edit_id.length() >= 16) 
            edit_id.setLength(15);
        // System.out.println("글자수 줄인 후: " + edit_id);
        while (edit_id.charAt(edit_id.length() - 1) == '.') 
            edit_id.deleteCharAt(edit_id.length() - 1);
        // System.out.println("6: " + edit_id);
        
        // 7. 2자 이하 -> 3될때까지 a append
        while (edit_id.length() < 3)
            edit_id.append(edit_id.charAt(edit_id.length() - 1));
        // System.out.println("7: " + edit_id);
        
        answer = edit_id.toString();
        return answer;
    }
}