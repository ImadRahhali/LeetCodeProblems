// Last updated: 5/30/2025, 7:34:34 PM
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] list = new int[k];
        for (Integer i : nums) {
            map.put(i, map.getOrDefault(i,0)+1);
        }
        List<Integer> values = new ArrayList<>(map.values());
        Collections.sort(values, Collections.reverseOrder()); // Sort values in descending order
        List<Integer> subList = values.subList(0, k);
        List<Integer> finalList = new ArrayList<>();
        for (Integer key : map.keySet()) {
            if (subList.contains(map.get(key))) {
                finalList.add(key);
            }
        }
        for (int i =0; i<k; i++) {
            list[i] = finalList.get(i);
        }
        return list;

    }
}