use std::io;

fn main() {
    // Read the first integer n
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read input");
    let n: usize = n.trim().parse().expect("Invalid input");

    // Read the array of size n
    let mut array = Vec::new();
    for _ in 0..n {
        let mut element = String::new();
        io::stdin().read_line(&mut element).expect("Failed to read input");
        let element: i32 = element.trim().parse().expect("Invalid input");
        array.push(element);
    }

    let mut i=0;
    let mut j=0;
    let mut start_even = 0;
    let mut n=0;
    while n < array.len() {
        if array[i] % 2 == 1 && start_even==0 {
            if i == array.len() {
                println!("{}", 1);
            } else {
                println!("{}", array[i]);
            }       
            start_even = 1;
            i+=1;
            n+=1;
        } else {i+=1;}
        if array[j] %2 == 0 && start_even==1 {
            if j == array.len() {
                println!("{}", 0);
            } else {
                println!("{}", array[j]);
            }
            j+=1;
            start_even=0;
            n+=1;
        } else {i+=1;}
    } 
    
}
