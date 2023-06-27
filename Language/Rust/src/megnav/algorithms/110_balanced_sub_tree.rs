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
    pub fn is_balanced(root: Option<NodeRef>) -> bool {
        let mut diff= 0;
        let ret = Solution::is_balanced_recursive(
            &root, diff
        );
        if ret == -1 {
            return false;
        } else {
            true
        }
    }

    pub fn is_balanced_recursive(root: &Option<NodeRef>, diff:i32) -> i32 {
        if diff == -1 {
            return -1;
        }
        match root{
            None => return 0,
            Some(node) => {
                let node = node.borrow();
                let right = Solution::is_balanced_recursive(&node.right, diff);
                let left = Solution::is_balanced_recursive(&node.left, diff);
                
                let mut diff = (right-left).abs();
                if diff > 1 {return -1;}
                else {
                    std::cmp::max(right, left)+1;
                }
                
            }
        }
    }
}