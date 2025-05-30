// Last updated: 5/30/2025, 7:35:13 PM
class Solution {
    public boolean isValid(String s) {
        HashMap<Character,Character> map = new HashMap<Character,Character>();
        map.put('[',']');
        map.put('(',')');
        map.put('{','}');
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()){
            if (map.containsKey(c)) {
                stack.push(c);
            }
            else if (stack.isEmpty() || map.get(stack.pop())!=c) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}