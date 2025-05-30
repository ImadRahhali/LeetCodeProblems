// Last updated: 5/30/2025, 7:35:15 PM
import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> listOfLists = new ArrayList<>();

        for (String s : strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            
            map.computeIfAbsent(sortedString, k -> new ArrayList<>()).add(s);
        }

        listOfLists.addAll(map.values());
        
        return listOfLists;
    }

}
