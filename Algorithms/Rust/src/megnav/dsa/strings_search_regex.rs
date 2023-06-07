use std::{
    collections::VecDeque,
    io::{stdin, BufReader, BufRead},
    fs::File
};
use glob::glob;
use regex::Regex;


fn process<T>(reader: BufReader<T>, pattern: &str, replace_with: &str) 
where T : std::io::Read {
    let reg = Regex::new(pattern).unwrap();
    for line in reader.lines() {
        if let Ok(l) = line {
            println!("{}", reg.replace_all(&l, replace_with));
        }
    }
}

fn main() -> std::io::Result<()> {
    let args = std::env::args();
    println!("{:?}", args);
    let mut args: VecDeque<String> = args.skip(1).collect();
    match args.len() {
        i if i == 2 =>  {
            let pattern = args.pop_front().unwrap();
            let replace_with = args.pop_front().unwrap();
            let reader = BufReader::new(stdin());
            process(reader, &pattern, &replace_with);
        }
        i if i > 2 => {
            let pattern = args.pop_front().unwrap();
            let replace_with = args.pop_front().unwrap();
            let path = args.pop_front().unwrap();
            for entry in glob(&path).expect("Failed to Read glob") {
                match entry {
                    Ok(path) => {
                        let file = File::open(path)?;
                        let reader = BufReader::new(file);
                        process(reader, &pattern, &replace_with);
                    }
                    Err(e) => println!("{:?}", e)
                    
                }
            }
        }
        _ => println!("Must provide a certail pattern!")
    }
    println!("Usage: {} <pattern> <replace_with> <path>", args.pop_front().unwrap());
    Ok(())
}