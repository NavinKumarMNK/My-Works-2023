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
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut vec2d = Vec::new();
        let mut depth = 0 as usize;
        Solution::level_order_rec(&root, &mut depth, &mut vec2d);
        vec2d
    }

    pub fn level_order_rec(root: &Option<Rc<RefCell<TreeNode>>>, depth:&mut usize, vec2d:&mut Vec<Vec<i32>>) {
        match root{
            None => (),
            Some(node) => {
                let node = node.borrow();
                if vec2d.len() <= *depth {
                    vec2d.resize(*depth +1 ,vec![]);
                }
                vec2d[*depth].push(node.val);
                *depth+=1;
                Solution::level_order_rec(&node.left, depth, vec2d);
                Solution::level_order_rec(&node.right, depth, vec2d);
                *depth-=1;
            }
        }
    }
}