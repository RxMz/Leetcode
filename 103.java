/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> to_ret = new ArrayList<List<Integer>>();
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        if(root == null){
            return to_ret;
        }
        q1.add(root);
        System.out.println("Adding");
        while(!q1.isEmpty() || !q2.isEmpty()){
            
            List<Integer> temp = new ArrayList<>();
            while(!q1.isEmpty()){
                TreeNode curr = q1.remove();
                if(curr.left != null)
                    q2.add(curr.left);
                if(curr.right != null)
                    q2.add(curr.right);
                temp.add(curr.val);
            }
            if(temp.isEmpty())
                break;
            to_ret.add(temp);
            List<Integer> temp2 = new ArrayList<>();
            while(!q2.isEmpty()){
                TreeNode curr = q2.remove();
                if(curr.left != null)
                    q1.add(curr.left);
                if(curr.right != null)
                    q1.add(curr.right);
                temp2.add(curr.val);
            }
            if(temp2.isEmpty())
                break;
            to_ret.add(temp2);
        }
        int i = 0;
        List<List<Integer>> to_ret_final = new ArrayList<List<Integer>>();
        for (List<Integer> a: to_ret){
            i+=1;
            if(i%2 == 0){
                Collections.reverse(a);
            }
            
                to_ret_final.add(a);
        }
        return to_ret_final;
    }
}