use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

type NodeRef = Rc<RefCell<TreeNode>>;

struct Solution;

impl Solution {
    pub fn is_subtree(root: Option<NodeRef>, sub_root: Option<NodeRef>) -> bool {
        Solution::is_subtree_recursive(&root, &sub_root)
    }

    pub fn is_subtree_recursive(root: &Option<NodeRef>, sub_root: &Option<NodeRef>) -> bool {
        match (root, sub_root) {
            (None, _) => false,
            (Some(node), Some(sub_node)) => {
                let node = node.borrow();
                let sub_node = sub_node.borrow();

                if node.val == sub_node.val && Solution::is_identical(&node.left, &sub_node.left)
                    && Solution::is_identical(&node.right, &sub_node.right)
                {
                    return true;
                }

                let ans1 = Solution::is_subtree_recursive(&node.left, sub_root);
                let ans2 = Solution::is_subtree_recursive(&node.right, sub_root);

                ans1 || ans2
            }
            _ => false,
        }
    }

    fn is_identical(root1: &Option<NodeRef>, root2: &Option<NodeRef>) -> bool {
        match (root1, root2) {
            (None, None) => true,
            (Some(node1), Some(node2)) => {
                let node1 = node1.borrow();
                let node2 = node2.borrow();

                node1.val == node2.val
                    && Solution::is_identical(&node1.left, &node2.left)
                    && Solution::is_identical(&node1.right, &node2.right)
            }
            _ => false,
        }
    }
}
