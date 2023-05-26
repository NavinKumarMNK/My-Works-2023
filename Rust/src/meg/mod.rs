mod meg{
    pub struct Meg {
        pub name1: String,
        pub name2: String,
        pub messages: Vec<String>,
    }
    impl Meg {
        pub fn message(message: &str) -> Meg {
            Meg {
                name1: String::from("Meg"),
                name2: String::from("Meg"),
                messages: vec![String::from(message)],
            }
        }
    }
    pub mod help_meg {
        fn seat_at_table(){
            println!("Seat at table");
        }
        pub fn add_to_waitlist(){
            seat_at_table();
            println!("Add to waitlist");
            let meg:super::Meg = super::Meg::message("Hello");
            serve_customer(meg);
        }
        fn serve_customer(cust_pizza: super::Meg){
            println!("Serve customer");
        }
    }
}

pub fn order_food(){
    crate::meg::meg::help_meg::add_to_waitlist();
    
}