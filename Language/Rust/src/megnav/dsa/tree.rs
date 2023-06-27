// Binary Tree Implementation
use std::rc::{Rc, Weak};
use std::cell::RefCell;
use std::fmt::Debug;

//type MutRef = RefCell<Node>;
type NodeRef = Rc<RefCell<Node>>;
//type WeakNodeRef = Weak<MutRef>;
#[derive(Debug)]
struct Tree {
    root : Option<NodeRef>,
}

#[derive(Debug)]
struct Node {
    value : i32,
    left : Option<NodeRef>,
    right : Option<NodeRef>,
}

impl Node {
    fn new(value : i32) -> Self {
        println!("Node created");
        Node {
            value,
            left : None,
            right : None,
        }
    }
} 


impl From<Node> for Option<NodeRef> {
    fn from(node: Node) -> Self {
        Some(Rc::new(RefCell::new(node)))
    }
}

/*
impl From<Node> for Optin<WeakNodeRef> {
    fn from(node: Node) -> Self {
        Some(Rc::downgrade())
    }
}*/

impl Tree {
    fn new() -> Self {
        println!("Tree created");
        Tree {root: None}
    }

    fn insert(&mut self, value:i32) {
        if self.root.is_none() {
            self.root = Node::new(value).into();
        } else {
            //Tree::insert_recursive(&mut self.root, value);
            Tree::insert_iterative(&mut self.root, value);
        }
    }
   
    fn insert_iterative(node: &mut Option<NodeRef>, value:i32){
        if node.is_none(){
            *node = Node::new(value).into();
            return;
        }
        let mut q = Vec::new();
        let node = node.as_mut().unwrap();
        q.push(node.clone());

        while let Some(node) = q.pop() {
            let mut node = node.as_ref().borrow_mut();
            if value > node.value {
                let right = &mut node.right;
                match right {
                    None => {
                        *right = Node::new(value).into();
                        return;
                    }
                    Some(n) => {
                        q.push(n.clone());
                    }
                }
            } else if value < node.value {
                let left = &mut node.left;
                match left {
                    None => {
                        *left = Node::new(value).into();
                        return;
                    }
                    Some(ref mut n) => {
                        q.push(n.clone());
                    }
                }
            }
        } 
    }

    fn insert_recursive(node: &mut Option<NodeRef>, value:i32){
        match node {
            None => {
                *node = Node::new(value).into();
            }
            Some(node) => {
                let mut node = node.as_ref().borrow_mut();
                if value < node.value {
                    Tree::insert_recursive(&mut node.left, value);
                } else {
                    Tree::insert_recursive(&mut node.right, value);
                }
            }
        }
    }
}

#[cfg(test)]
pub mod tests {
    use super::*;
    #[test]
    pub fn works() {
        let mut tree = Tree::new();
        tree.insert(8);
        tree.insert(10);
        tree.insert(3);
        tree.insert(1);
        tree.insert(6);
        tree.insert(4);

        assert_eq!(tree.root.is_some(), true);
        println!("{:?}", tree);
    }
}

fn main() {

}
