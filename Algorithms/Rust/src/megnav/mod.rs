mod megnav{
    pub struct megnav {
        pub name1: String,
        pub name2: String,
        pub messages: Vec<String>,
    }
    impl megnav {
        pub fn message(message: &str) -> megnav {
            megnav {
                name1: String::from("megnav"),
                name2: String::from("megnav"),
                messages: vec![String::from(message)],
            }
        }
    }
    pub mod help_megnav {
        fn seat_at_table(){
            println!("Seat at table");
        }
        pub fn add_to_waitlist(){
            seat_at_table();
            println!("Add to waitlist");
            let megnav:super::megnav = super::megnav::message("Hello");
            serve_customer(megnav);
        }
        fn serve_customer(cust_pizza: super::megnav){
            println!("Serve customer");
        }
    }
}

pub fn order_food(){
    crate::megnav::megnav::help_megnav::add_to_waitlist();
    
}