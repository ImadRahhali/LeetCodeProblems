// Last updated: 5/30/2025, 7:34:29 PM
import java.util.ArrayList;
class Solution {
    public int calPoints(String[] operations) {
        int S = 0;
        List<Integer> record = new ArrayList<Integer>();
        for (int i=0;i<operations.length;i++) {
            int lastIndex = record.size() - 1;
            if (operations[i].equals("C")) {
                Integer poppedElement = record.remove(lastIndex);
            }
            else if (operations[i].equals("D")){
                record.add(record.get(lastIndex)*2);
            }
            else if (operations[i].equals("+")) {
                record.add(record.get(lastIndex)+record.get(lastIndex-1));
            }
            else {
                record.add(Integer.parseInt(operations[i]));
            }
        }
        
        for (int score : record) {
            S += score;
        }
        return S;
    }
}