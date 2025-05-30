// Last updated: 5/30/2025, 7:34:53 PM
class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minstack;
    public MinStack() {
      stack = new Stack();
      minstack = new Stack();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minstack.isEmpty() || val <= minstack.peek()) {
            minstack.push(val);
        }
         else {
            minstack.push(minstack.peek());
        }
    }
    
    public void pop() {
        stack.pop();
        minstack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minstack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */