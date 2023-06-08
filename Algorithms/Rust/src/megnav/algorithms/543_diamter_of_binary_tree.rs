// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
type NodeRef = Rc<RefCell<TreeNode>>;
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<NodeRef>) -> i32 {
        let mut max_diamter = 0;
        let mut ret_diamter = 0;
        let (ret, max) = Solution::max_diameter_recursive(
            &root, ret_diamter, max_diamter
        );
        max
    }

    pub fn max_diameter_recursive(root: &Option<NodeRef>, ret_diamter: i32, max_diameter:i32) -> (i32, i32) {
        match root {
            None => (ret_diamter, max_diameter),
            Some(node) => {
                let node = node.borrow();
                let (right, mut max_diameter) = Solution::max_diameter_recursive(&node.right, ret_diamter, max_diameter);
                let (left, mut max_diameter) = Solution::max_diameter_recursive(&node.left, ret_diamter, max_diameter);
                
                max_diameter = std::cmp::max(max_diameter, right + left);
                let ret_di = std::cmp::max(right, left)+1;
                if right + left > max_diameter{
                    max_diameter = right + left;
                }
                (ret_di, max_diameter)
            }
        }
    }
}