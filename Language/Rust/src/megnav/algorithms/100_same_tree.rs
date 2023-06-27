// Definition for a binary tree node.
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
        right: None
        }
    }
}

type NodeRef = Rc<RefCell<TreeNode>>;
use std::rc::Rc;
use std::cell::RefCell;
struct Solution;

impl Solution {
    pub fn is_same_tree(p: Option<NodeRef>, q: Option<NodeRef>) -> bool {
        Solution::traversal(&p, &q)
    }

    pub fn traversal(p: &Option<NodeRef>, q:&Option<NodeRef>) -> bool {
        if p.is_none() && q.is_none(){
            return true;
        } else if (p.is_none() || q.is_none()) {
            return false;
        } else {
            let p = p.as_ref().unwrap().borrow();
            let q = q.as_ref().unwrap().borrow();
            let a = Solution::traversal(&p.left, &q.left);
            let b = Solution::traversal(&p.right, &q.right);
            
            if !(a == true && b == true) {
                return false;
            } else if q.val == p.val {
                return true;
            } else {
                return false;

            }
        }
    }
}