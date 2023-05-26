#![allow(unused)]

use std::io;
use rand::Rng;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::ops::Add;
use std::collections::HashMap;
use std::thread;
use std::time::Duration;
use std::rc::Rc;
use std::cell::RefCell;
use std::sync::{Arc, Mutex};



// Modules
mod megnav;
use crate::megnav::order_food;

//functions
fn get_sum(num1: i32, num2: i32) -> i32 {
    num1 + num2
}

// Generics
fn get_sum_generics<T:Add<Output = T>>(x: T, y: T) -> T {
    return x + y;
}

// Struct
struct Customer {
    name: String,
    balance: f32,   
}

impl Customer {
    fn withdraw(&mut self, amount: f32){
        if self.balance >= amount {
            self.balance -= amount;
        } else {
            println!("Not enough funds");
        }
    }
    fn deposit(&mut self, amount: f32){
        self.balance += amount;
    }
    fn get_balance(&self) -> f32 {
        self.balance
    }
}



// Traits
trait Shape {
    fn new (width:u32, height:u32) -> Self;
    fn area (&self) -> f32;
}
struct Rectangle <T, U> {
    width: T,
    height: U,
}

fn main() {
    let mut name: String = String::new();
    let mut age: String = String::new();
    let greeting: &str= "Nice to meet you";
    io::stdin().read_line(&mut name)
        .expect("Failed to read line");
    println!("Hello, world! {} {} ", name.trim_end(), greeting);
    age = String::from("20");
    let mut age: u32 = age.trim().parse()
        .expect("Age wasn;t assigned");
    age = age + 1;
    println!("You will be {} next year", age);
    
    // Data Types
    println!("Max u128 : {}", u128::MAX);
    let random = rand::thread_rng().gen_range(1..101);
    println!("Random number: {}", random);

    // Conditional Statements
    if (age >= 1) && (age >= 18){
        println!("Important Birthday");
    } else if (age == 21) || (age == 50){
        println!("Important Birthday");
    } else {
        println!("Not an important birthday");
    }

    // Ternary Operator
    let can_vote = if age >=18 {true} else {false};
    println!("Can vote: {}", can_vote);

    // match like switch Case
    match age {
        1..=18 => println!("Can vote"),
        21 | 50 => println!("Important Birthday"),
        _ => println!("Not an important birthday")
    }

    // Match with Comparator
    match age.cmp(&18){
        Ordering::Less => println!("Can't Vote"),
        Ordering::Greater => println!("Can Vote"),
        Ordering::Equal => println!("Can Vote")
    }

    // Array
    let arr1 = [1,2,3];
    println!("1st: {}", arr1[0]);
    println!("Length : {}", arr1.len());
    
    // Looping
    let mut loop_idx = 0;
    loop {
        if loop_idx >= arr1.len(){
            break;
        }
        println!("Val: {}", arr1[loop_idx]);
        loop_idx += 1;
    }

    for x in 0..arr1.len(){
        println!("Val: {}", arr1[x]);
    }

    while loop_idx < arr1.len(){
        println!("Val: {}", arr1[loop_idx]);
        loop_idx += 1;
    }

    for val in arr1.iter(){
        println!("Val: {}", val);
    }

    // Tuples
    let tuple: (u16, String, f64) = (1, "Hello".to_string(), 3.4);
    println!("Tuple: {:?}", tuple);
    let (v1, v2, v3) = tuple;
    println!("v1: {}, v2: {}, v3: {}", v1, v2, v3);

    // String
    let mut st1 = String::new();
    st1.push('A');
    st1.push_str(" Word");
    println!("st1: {}", st1);

    for word in st1.split_whitespace(){
        println!("{}", word);
    }
    let st2 = st1.replace("Word", "World");
    println!("st2: {}", st2);

    // Vectors & Strings
    let mut v1: Vec<char> = Vec::new();
    v1 = vec!['A','B','C'];
    v1.sort(); // Sort Acesending
    v1.dedup(); // Remove Duplicates
    v1.push('D');
    v1.push('E');
    for char in v1 {
        println!("{}", char);
    } 
    let st4: &str = "Random String";
    let mut st5: String = st4.to_string();
    println!("st4: {}", st4);
    let byte_arr1 = st5.as_bytes();
    let st6 = &st5[0..6];
    for byte in byte_arr1 {
        println!("{}", byte);
    }
    for char in st5.chars(){
        println!("{}", char);
    }
    match st5.find("String"){
        Some(i) => println!("Index: {}", i),
        None => println!("No match")
    }

    // Casting
    let int_u8 = 1.23 as i16;
    println!("int_u8: {}", int_u8);

    //enum
    enum Day {
        Mon, Tue, Wed, Thu, Fri, Sat, Sun
    }
    impl Day {
        fn is_weekend(&self)-> bool {
            match self{
                Day::Sat | Day::Sun => return true,
                _ => return false
            }
        }
    }
    let today:Day = Day::Mon;
    match today {
        Day::Mon => println!("It's Monday"),
        _ => println!("It's not Monday")
    }
    println!("Is weekend: {}", today.is_weekend());

    // Vectors
    let vec1: Vec<i32> = Vec::new();
    let mut vec2 = vec![1, 2, 3, 4];
    vec2.push(5);
    println!("vec2: {:?}", vec2);
    let second: &i32 = &vec2[1];
    
    match vec2.get(1) {
        Some(x) => println!("Item 2: {}", x),
        None => println!("None")
    }

    for i in &mut vec2 {
        *i += 10;
    }
    for i in &vec2 {
        println!("vec2: {}", i);
    }
    println!("vec2: {:?}", vec2);
    println!("Pop: {}", vec2.len());

    // Functions & Closures
    // let closures = |parameters| -> return_type {BODY} 
    println!("Sum: {}", get_sum(1, 2)); 
    let sum_nums = |x: i32, y: i32| x + y;
    let num = sum_nums(1, 2);
    println!("Sum: {}", num);
    let list = vec![1, 2, 3, 4];
    println!("Sum: {}", list.iter().fold(0, |a, b| a + b));

    // Generics
    println!("Sum: {}", get_sum_generics(1, 2));
    println!("Sum: {}", get_sum_generics(1.2, 2.1));
    //println!("Sum: {}", get_sum_generics('A', 'B'));

    // Ownership
    let str1 = "Hello"; // String::from("Hello") is error
    let str2 = str1;
    println!("str2: {}", str1);

    // Borrowing
    let vec1 = vec![1, 2, 3];
    let vec2 = &vec1;
    println!("vec1: {:?}", vec1);
    println!("vec2: {:?}", vec2);

    let vect1 = vec![1, 2, 3];
    let vect2 = vect1;
    //println!("vect2: {:?}", vect1); // Error

    // HashMap
    let mut hm = HashMap::new();
    hm.insert("AAA", "BBB");
    hm.insert("CCC", "DDD");
    
    for (k, v) in &hm {
        println!("{}: {}", k, v);
    }

    for k in hm.iter() {
        println!("{}: {}", k.0, k.1);
    }

    if hm.contains_key(&"AAA"){
        let val = hm.get(&"AAA");
        match val {
            Some(x) => println!("AAA: {}", x),
            None => println!("None")
        }
    }

    // Structs
    let mut megnav = Customer{name: "megnav".to_string(), balance: 100.50};
    megnav.withdraw(10.0);
    println!("Balance: {}", megnav.balance);
    println!("Customer: {}", megnav.name);
    
    // Traits
    impl Shape for Rectangle<u32, u32> {
        fn new(width: u32, height: u32) -> Rectangle<u32, u32>{
            Rectangle{width, height}
        }
        fn area(&self) -> f32 {
            return (self.width * self.height) as f32;
        }
    }
    let mut rec: Rectangle<u32, u32> = Shape::new(10, 20);
    println!("Area: {}", rec.area());
    
    // Error
    panic!("Crash and burn");

    // File Handling
    let path = "linux.txt";
    let output = File::create(path);
    let mut output = match output {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        } 
    };
    write!(output, "Rust is awesome").expect("Failed to write");
    
    let input = File::open(path).unwrap();
    let buffered = BufReader::new(input);
    for line in buffered.lines(){ 
        println!("{}", line.unwrap());
    }
    let output2 = File::create("rand.txt");
    let output2 = match output2 {
        Ok(file) => file,
        Err(error) => match error.kind(){
            ErrorKind::NotFound => match File::create("rand.txt"){
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e)
            },
            _other_error => panic!("Problem opening the file: {:?}", error),
        },
    };

    // Box stores data in heap and the pointer in stack Tree
    let b_int32 = Box::new(10);
    println!("b_int32={}", b_int32);

    struct TreeNode<T> {
        pub data: T,
        pub left: Option<Box<TreeNode<T>>>,
        pub right: Option<Box<TreeNode<T>>>,
    }
    impl<T> TreeNode<T> {
        pub fn new(data:T)-> Self{
            TreeNode {
                left:None, right:None, data:data
            }
        }
        pub fn left(mut self, node:TreeNode<T>) -> Self{
            self.left = Some(Box::new(node));
            self
        }
        pub fn right (mut self, node:TreeNode<T>) -> Self {
            self.right = Some(Box::new(node));
            self
        }
    }

    let node = TreeNode::new(1)
        .left(TreeNode::new(2))
        .right(TreeNode::new(3));


    // Concurrency
    let thread1 = thread::spawn(|| {
        for i in 1..25{
            println!("Sawned thread: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..10{
        println!("Main thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    }
    thread1.join().unwrap(); // wait for thread to finish

    /* 
    // Thread
    pub struct Bank{
        balance: f32,
    }
    fn withdraw(the_bank: &mut Bank, amt:f32){
        the_bank.balance -= amt;
    }
    let mut bank = Bank{balance:10.0};
    withdraw(&mut bank, 5.0);
    println!("Balance = {}", bank.balance);
    fn customer(the_bank: &mut Bank){
        withdraw(the_bank, 5.0);
    }

    // Closure cannot outlive the current function especially 
    // because its borrowing which is owned by the current function 
    thread::spaws(|| {
        customer(&mut bank)
    }).join.unwrap();
    // fix is the smart poninter, which going to allow multiple owners
    // and also blocks access whenever thes different parts are needed
    // Specifically, Reference Smart Pointers
    */

    // Rc<T> is a reference counting smart pointer
    pub struct Bank{
        balance: f32
    }
    fn withdraw(the_bank: &Arc<Mutex<Bank>>, amt:f32 ){
        let mut bank_ref = the_bank.lock().unwrap();
        bank_ref.balance -= amt;
        if bank_ref.balance < 0.0 {
            println!("Balance is negative: {}", bank_ref.balance);
        }
        else {
            bank_ref.balance -= amt;
            println!("Balance is {}", bank_ref.balance);
        }
    }
    fn customer(the_bank: Arc<Mutex<Bank>>){
        withdraw(&the_bank, 5.0);
    }

    let bank: Arc<Mutex<Bank>> = Arc::new(Mutex::new(Bank { balance : 100.0}));
    let handles = (0..10).map(|_| {
        let bank_ref = bank.clone();
        thread::spawn(|| {
            customer(bank_ref)

        })
    });
    for handle in handles {
        handle.join().unwrap();
    }

    println!("Total {}", bank.lock().unwrap().balance);
}

