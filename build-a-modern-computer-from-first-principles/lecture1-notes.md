# Boolean Logic

All boolean functions can be constructed using AND, OR, and NOT.
Actually, these can be reduced to NAND. ("Not and")

*With NAND gates you can construct any boolean function*

NOT(x) = (x NAND x)
(x AND y) = NOT(x NAND y)

# Gate Logic

A logic gate is a specialized chip that's designed to perform a specific boolean function (AND, OR, NAND, etc)

The *interface* of a gate answers the question "what" (is this doing?). To understand *how* it's doing it, you'd have to look at a finer level of detail.