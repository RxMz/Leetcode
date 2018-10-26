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
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root != null){
            inorderTraversal(root.left);
            to_ret.add(root.val);
            inorderTraversal(root.right);
        }
        return to_ret;
    }
}