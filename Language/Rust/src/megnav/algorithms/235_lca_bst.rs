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
    pub fn lowest_common_ancestor(root: Option<NodeRef>, p: Option<NodeRef>, q: Option<NodeRef>) -> Option<NodeRef> {
        Solution::lca(&root, &p, &q)
    }

    pub fn lca(root: &Option<NodeRef>, p:&Option<NodeRef>, q:&Option<NodeRef>) -> Option<NodeRef>  {
        match root {
            None => return None,
            Some(node) => {
                let node_ref = node.borrow();
                let p_ref = p.as_ref().unwrap().borrow();
                let q_ref = q.as_ref().unwrap().borrow();
                
                if node_ref.val > p_ref.val && node_ref.val > q_ref.val {
                    return Solution::lca(&node_ref.left, &p, &q);
                } else if node_ref.val < p_ref.val && node_ref.val < q_ref.val {
                    return Solution::lca(&node_ref.right, &p, &q);
                } else {
                    return Some(node.clone());
                }
            }
        }
    }
}