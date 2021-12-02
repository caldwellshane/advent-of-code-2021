use super::input::INPUT_PATH;
use std::fs;
use std::path::Path;
use std::str::FromStr;

static DAY: i16 = 2;

struct Position {
    horiz: i64,
    depth: i64,
}

struct PartOneSubmarine {
    position: Position,
}

struct PartTwoSubmarine {
    position: Position,
    aim: i64,
}

struct Movement<'a> {
    direction: &'a str,
    displacement: i64,
}

trait Moveable {
    fn update_position(&mut self, movement: &Movement);
}

impl Moveable for PartOneSubmarine {
    fn update_position(&mut self, movement: &Movement) {
        match movement.direction {
            "forward" => self.position.horiz += movement.displacement,
            "down" => self.position.depth += movement.displacement,
            "up" => self.position.depth -= movement.displacement,
            &_ => panic!("Invalid movement instruction encountered."),
        }
    }
}

impl Moveable for PartTwoSubmarine {
    fn update_position(&mut self, movement: &Movement) {
        match movement.direction {
            "forward" => {
                self.position.horiz += movement.displacement;
                self.position.depth += movement.displacement * self.aim;
            }
            "down" => self.aim += movement.displacement,
            "up" => self.aim -= movement.displacement,
            &_ => panic!("Invalid movement instruction encountered."),
        }
    }
}

fn parse_movement(instruction: &str) -> Result<Movement, std::num::ParseIntError> {
    let fields: Vec<&str> = instruction.split_whitespace().collect();
    let displacement = i64::from_str(fields[1])?;
    return Ok(Movement {
        direction: fields[0],
        displacement: displacement,
    });
}

pub fn run() {
    let data_str = fs::read_to_string(&Path::new(INPUT_PATH).join(format!("day_{:02}.txt", DAY)))
        .expect("Something went wrong reading data file.");
    let instructions: Vec<Movement> = data_str
        .split_terminator("\n")
        .filter_map(|word| parse_movement(word).ok())
        .collect();
    let mut sub_1 = PartOneSubmarine {
        position: Position { horiz: 0, depth: 0 },
    };
    let mut sub_2 = PartTwoSubmarine {
        position: Position { horiz: 0, depth: 0 },
        aim: 0,
    };
    for instr in instructions {
        sub_1.update_position(&instr);
        sub_2.update_position(&instr);
    }
    println!(
        "Part 1: Final (x, y) = ({x}, {y}). Product x*y = {xy}.",
        x = sub_1.position.horiz,
        y = sub_1.position.depth,
        xy = sub_1.position.horiz * sub_1.position.depth
    );
    println!(
        "Part 2: Final (x, y) = ({x}, {y}). Product x*y = {xy}.",
        x = sub_2.position.horiz,
        y = sub_2.position.depth,
        xy = sub_2.position.horiz * sub_2.position.depth
    );
}
