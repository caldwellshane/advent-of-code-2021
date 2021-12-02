use super::input::INPUT_PATH;
use anyhow::{anyhow, Error, Result};
use itertools::Itertools;
use std::fs;
use std::path::Path;
use std::str::FromStr;

static DAY: i16 = 2;

#[derive(Default)]
struct Position {
    horiz: i64,
    depth: i64,
}

#[derive(Default)]
struct PartOneSubmarine {
    position: Position,
}

#[derive(Default)]
struct PartTwoSubmarine {
    position: Position,
    aim: i64,
}

enum Direction {
    Forward,
    Down,
    Up,
}

impl FromStr for Direction {
    type Err = Error;
    fn from_str(s: &str) -> Result<Direction, Self::Err> {
        match s {
            "forward" => Ok(Direction::Forward),
            "down" => Ok(Direction::Down),
            "up" => Ok(Direction::Up),
            _ => Err(anyhow!("Bad direction string `{}`", s)),
        }
    }
}

struct Movement {
    direction: Direction,
    displacement: i64,
}

trait Moveable {
    fn update_position(&mut self, movement: &Movement);
}

impl Moveable for PartOneSubmarine {
    fn update_position(&mut self, movement: &Movement) {
        match movement.direction {
            Direction::Forward => self.position.horiz += movement.displacement,
            Direction::Down => self.position.depth += movement.displacement,
            Direction::Up => self.position.depth -= movement.displacement,
        }
    }
}

impl Moveable for PartTwoSubmarine {
    fn update_position(&mut self, movement: &Movement) {
        match movement.direction {
            Direction::Forward => {
                self.position.horiz += movement.displacement;
                self.position.depth += movement.displacement * self.aim;
            }
            Direction::Down => self.aim += movement.displacement,
            Direction::Up => self.aim -= movement.displacement,
        }
    }
}

fn parse_movement(instruction: &str) -> Result<Movement> {
    let (f0, f1) = instruction
        .split_whitespace()
        .collect_tuple()
        .ok_or_else(|| anyhow!("Unable to split `{}` on whitespace", instruction))?;
    let direction = Direction::from_str(f0)?;
    let displacement = i64::from_str(f1)?;
    Ok(Movement {
        direction,
        displacement,
    })
}

pub fn run() {
    let data_str = fs::read_to_string(&Path::new(INPUT_PATH).join(format!("day_{:02}.txt", DAY)))
        .expect("Something went wrong reading data file.");
    let mut sub_1 = PartOneSubmarine::default();
    let mut sub_2 = PartTwoSubmarine::default();
    for instr in data_str
        .split_terminator('\n')
        .map(|line| parse_movement(line).expect("Unable to parse a line!"))
    {
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
