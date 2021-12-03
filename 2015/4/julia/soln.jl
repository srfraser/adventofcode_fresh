using Printf
using Nettle


function find_leading_zeroes(secret_key; zeroes=5)
    hashinput = 1
    current = ""
    target = "0"^zeroes
    while !startswith(current, target)
        hashinput += 1
        current = hexdigest("md5", "$secret_key$hashinput")
    end
    return hashinput
end

@printf "Lowest input for part 1 %s\n" find_leading_zeroes("bgvyzdsv")
@printf "Lowest input for part 1 %s\n" find_leading_zeroes("bgvyzdsv", zeroes=6)

