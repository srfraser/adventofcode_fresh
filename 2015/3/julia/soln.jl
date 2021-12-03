using Printf

puzzle_input = open(joinpath(dirname(Base.PROGRAM_FILE), "../input")) do file
    read(file, String)
end


directions = Dict(
    ">" => (1, 0),
    "v" => (0, 1),
    "<" => (-1, 0),
    "^" => (0, -1),
)



function visited_houses(puzzle)
    current_coords = (0, 0)
    visited = Set()

    push!(visited, current_coords)

    for direction in puzzle
        current_coords = (
            current_coords[1] + directions[direction][1],
            current_coords[2] + directions[direction][2],
        )
        push!(visited, current_coords)
    end

    return visited
end


function part1(data)
    return length(visited_houses(data))
end


function part2(puzzle)
    santa = puzzle[1:2:end]
    robo = puzzle[2:2:end]
    return length(union(visited_houses(santa), visited_houses(robo)))
end

puzzle_input = split(chomp(puzzle_input), "")
@printf "Part 1: %s\n" part1(puzzle_input)
@printf "Part 2: %s\n" part2(puzzle_input)
