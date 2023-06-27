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

use std::borrow::BorrowMut;
use std::rc::Rc;
use std::cell::RefCell;
struct Solution;
impl Solution {
   pub fn max_depth(root: Option<NodeRef>) -> i32 {
       Solution::max_depth_recursive(&root, 0)
   }

   pub fn max_depth_recursive(root: &Option<NodeRef>, depth:i32) -> i32 {
       match root{
           None => return depth,
           Some(node) => {
               let node = node.borrow();
               let right_depth = Solution::max_depth_recursive(&node.right, depth+1);
               let left_depth = Solution::max_depth_recursive(&node.left, depth+1);
               std::cmp::max(left_depth, right_depth)
           }
       }
   }
}