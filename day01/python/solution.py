import math


def _fuel_requirement(module):
    return math.floor(module / 3) - 2


def part_one(input):
    modules = input.splitlines()

    fuel_requirements = sum(_fuel_requirement(int(module)) for module in modules)
    return fuel_requirements


def part_two(input):
    modules = input.splitlines()

    fuel_requirements = 0

    for module in modules:
        fuel_requirement = _fuel_requirement(int(module))
        total_fuel_requirement = 0

        while fuel_requirement > 0:
            total_fuel_requirement += fuel_requirement
            fuel_requirement = _fuel_requirement(fuel_requirement)

        fuel_requirements += total_fuel_requirement

    return fuel_requirements
