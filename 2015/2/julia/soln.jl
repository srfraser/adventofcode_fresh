using Printf

puzzle_input = open(joinpath(dirname(Base.PROGRAM_FILE), "../input")) do file
    read(file, String)
end


function surface_area(width, length, height)
    sides = [length * width, width * height, height * length]
    # Add margin of error: size of smallest side
    return sum(sides) * 2 + min(sides...)
end

function ribbon_length(dimensions)
    bow = prod(dimensions)
    highest = max(dimensions...)
    deleteat!(dimensions, findfirst(x->x==highest, dimensions))
    return 2 * sum(dimensions) + bow
end

function part1(data)
    total_sq_feet = 0
    for line in split(data, "\n")
        x, y, z = [parse(Int64, i) for i in split(line, "x")]
        total_sq_feet += surface_area(x, y, z)
    end
    return total_sq_feet
end


function part2(data)
    total_ribbon = 0
    for line in split(data, "\n")
        dimensions = [parse(Int64, i) for i in split(line, "x")]
        total_ribbon += ribbon_length(dimensions)
    end
    return total_ribbon
end

@printf "Part 1: %s\n" part1(puzzle_input)
@printf "Part 2: %s\n" part2(puzzle_input)
