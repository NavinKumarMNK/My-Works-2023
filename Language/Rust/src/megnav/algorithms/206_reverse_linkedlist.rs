struct Solution;

impl Solution {
    pub fn reverse_list_2(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;
        while let Some(mut boxed_node) = curr {
            let next = boxed_node.next.take();
            boxed_node.next = prev;
            prev = Some(boxed_node);
            curr = next;
        }
        prev
    }

}