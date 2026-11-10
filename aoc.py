import click
import os
import time

import day01.python.solution as day01
import day02.python.solution as day02
import day03.python.solution as day03
import day04.python.solution as day04
import day05.python.solution as day05
import day06.python.solution as day06
import day07.python.solution as day07
import day08.python.solution as day08
import day09.python.solution as day09
import day10.python.solution as day10
import day11.python.solution as day11
import day12.python.solution as day12
import day13.python.solution as day13
import day14.python.solution as day14
import day15.python.solution as day15
import day16.python.solution as day16
import day17.python.solution as day17
import day18.python.solution as day18
import day18.python.solution as day19
import day20.python.solution as day20
import day21.python.solution as day21
import day22.python.solution as day22
import day23.python.solution as day23
import day24.python.solution as day24
import day25.python.solution as day25


@click.command()
@click.argument("day")
@click.argument("part")
@click.option("-t", "--test", is_flag=True, help="Run the test.txt file")
@click.option("-d", "--debug", is_flag=True, help="Print debugging logs to console")
def runner(day, part, test, debug):
    if debug:
        os.environ["MODE"] = "DEBUG"

    day = int(day)
    part = int(part)
    if day < 1 and day > 25:
        print(f"'{day}' is not a valid number between 1-25.")

    day_string = str(day)
    if day < 10:
        day_string = "0" + day_string
    filename = "test" if test else "input"

    input_filepath = f"day{day_string}/input/{filename}.txt"
    try:
        text_file = open(input_filepath, "r")
        input = text_file.read()
        text_file.close()
    except FileNotFoundError:
        print(f"Failed: Could not find file at path: {input_filepath}")
        return

    try:
        day_module = globals()[f"day{day_string}"]

        if part == 1:
            solution = day_module.part_one
        elif part == 2:
            solution = day_module.part_two
    except Exception:
        print(f"No python solutions for day {day_string} part {part}.")
        return


    start = time.time()
    answer = solution(input)

    print("-------")
    if answer == -1:
        print(f"Solution for day {day_string} part {part} not yet completed.")
    else:
        print(answer)
    print("-------")

    end = time.time()
    elapsed_seconds = end - start
    print(f"Completed in {elapsed_seconds} seconds.")


if __name__ == "__main__":
    runner()
