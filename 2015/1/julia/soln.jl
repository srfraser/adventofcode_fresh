using Printf

puzzle_input = open(joinpath(dirname(Base.PROGRAM_FILE), "../input")) do file
    read(file, String)
end


function part1(data)
    return count("(", data) - count(")", data)
end


function part2(data)
    position = 0
    target = -1
    current = 0
    sequence = [x == "(" ? 1 : -1  for x in split(data, "")]
    for instruction in sequence
        current += instruction
        position += 1
        if current == target
            break
        end
    end
    return position
end


@printf "Part 1: %s\n" part1(puzzle_input)

@printf "Part 2: %s\n" part2(puzzle_input)