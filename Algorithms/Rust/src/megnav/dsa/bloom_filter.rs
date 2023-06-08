use fasthash;

//m bits = -(n * ln(p)) / ln(2)^2
fn num_bits(size:usize, fp_rate:f64) -> usize {
    let num = -1.0 * (size as f64) * fp_rate.ln();
    let den = f64::ln(2.0).powf(2.0);
    (num / den).ceil() as usize
}

// k = (m/n) ln2
fn num_hashes(m:usize, n:usize) -> usize {
    ((m as f64 / n as f64) * f64::ln(2.0)).ceil() as usize
}

pub struct BloomFilter {
    bitvec : Vec<u8>,
    hashes : usize,
}

impl BloomFilter {
    pub fn new(size:usize, fp_rate:f64) -> Self {
        let m = num_bits(size, fp_rate as f64);
        let k = num_hashes(m, size);
        BloomFilter {
            bitvec : vec![0; m],
            hashes : k,
        }
    }

    pub fn insert(&mut self, value: &str) {
        for i in 0..self.hashes {
            let index = fasthash::murmur3
            ::hash32_with_seed(value, i as u32) %
            (self.bitvec.len() as u32 * 8) ;

            let pos = index as usize;
            self.bitvec[pos / 8] |= 1 << (pos % 8);
        }
    }

    pub fn get(&self, value:&str) -> bool {
        for i in 0..self.hashes {
            let index = fasthash::murmur3
            ::hash32_with_seed(value, i as u32) %
            (self.bitvec.len() as u32 * 8) ;

            let pos = index as usize;
            match (self.bitvec[pos / 8] & (1 << (pos % 8))) == 0{
                true => return false,
                false => (),
            }
        }
        true
    }

}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_() {
        let mut filter = BloomFilter::new(2, 0.001);
        filter.insert("test");
        //filter.insert("wrong");
        println!("{:?}", filter.bitvec);
        println!("{:?}", filter.get("test"));
        //assert!(filter.get("test"));
        //assert!(!filter.get("test2"));


    }
}

fn main(){}