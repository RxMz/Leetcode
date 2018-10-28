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
    List<Integer> to_ret = new ArrayList<>();
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root!=null){
            to_ret.add(root.val);
            preorderTraversal(root.left);
            preorderTraversal(root.right);
        }
        return to_ret;
    }
}
