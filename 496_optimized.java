class Solution {
        public int[] nextGreaterElement(int[] findNums, int[] nums) {
        Map<Integer, Integer> map = new HashMap<>(); 
        Stack<Integer> stack = new Stack<>();
        for (int i = 0 ; i < nums.length; i++) {
            while (!stack.isEmpty() && stack.peek() < nums[i])
                map.put(stack.pop(), nums[i]);
            stack.push(nums[i]);
        }   
        for (int i = 0; i < findNums.length; i++)
            findNums[i] = map.getOrDefault(findNums[i], -1);
        return findNums;
    }
}