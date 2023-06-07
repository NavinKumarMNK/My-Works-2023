fn num_bits(size:usize, fp_rate:f64) -> usize {
    let num = -1.0f64 * (size as f64) * fp_rate.ln();
    let den = 2.0f64.ln().powf(2.0);
    (num / den).ceil() as usize
}

fn num_hashes(m:usize, n:usize) -> usize {
    ((m as f64 / n as f64) * 2.0f64.ln()).ceil() as usize
}

pub struct BloomFilter {
    bitvec : Vec<u8>,
    hashes : usize,
}

impl BloomFilter {
    pub fn new(size:usize, fp_rate:usize) -> Self {
        let m = num_bits(size, fp_rate as f64);
        let k = num_hashes(m, size);
        BloomFilter {
            bitvec : vec![0; m],
            hashes : k,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_() {

    }
}