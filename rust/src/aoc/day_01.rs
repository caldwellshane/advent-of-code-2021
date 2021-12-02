use super::input::INPUT_PATH;
use std::fs;
use std::path::Path;
use std::str::FromStr;

static DAY: i16 = 1;

fn count_increases(data: &Vec<i32>) -> i16 {
    let mut count = 0;
    for idx in 1..data.len() {
        if data[idx] > data[idx - 1] {
            count += 1;
        }
    }
    return count;
}

fn three_element_sums(data: &Vec<i32>) -> Vec<i32> {
    let mut sums = Vec::<i32>::new();
    for (idx, _) in data.iter().enumerate() {
        if idx >= 2 {
            sums.push(data[idx - 2] + data[idx - 1] + data[idx])
        }
    }
    return sums;
}

pub fn run() {
    let data_str = fs::read_to_string(&Path::new(INPUT_PATH).join(format!("day_{:02}.txt", DAY)))
        .expect("Something went wrong reading data file.");

    let data: Vec<i32> = data_str
        .split_whitespace()
        .filter_map(|word| i32::from_str(word).ok())
        .collect();

    println!(
        "Part 1: Found {} increases in depth.",
        count_increases(&data)
    );
    println!(
        "Part 2: Found {} increases in three-element sum.",
        count_increases(&three_element_sums(&data))
    );
}

#[test]
fn test_count_increases() {
    let data: Vec<i32> = vec![1, 2, 4, 3, 3, -12, -11, -11, 7];
    assert_eq!(count_increases(&data), 4);
}

#[test]
fn test_three_element_sums() {
    let data: Vec<i32> = vec![1, 2, 4, 3, 3, -12, -11, -11, 7];
    assert_eq!(three_element_sums(&data), vec![7, 9, 10, -6, -20, -34, -15]);
}
