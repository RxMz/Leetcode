/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.lang.Math;
class Solution {
    int depth = 0;
    public int maxDepth(TreeNode root) {
        if(root != null){
            return count(root, 0);
        }
        return 0;
    }
    public static int count(TreeNode node, int count){
        if(node != null){
            count = Math.max(count(node.left,count+1),count(node.right, count+1));
            return count;
        }
        else{
            return count;
        }
    }
}
