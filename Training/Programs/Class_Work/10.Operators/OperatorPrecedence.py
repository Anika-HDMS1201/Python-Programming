# Operator precedence describes the order in which operations are performed.

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)


# Operator Precedence (from highest to lowest):
# 1. () Parentheses
# 2. ** Exponentiation
# 3. +x, -x, ~x Unary plus, unary minus, bitwise NOT
# 4. *, /, //, % Multiplication, division, floor division, modulus
# 5. +, - Addition and subtraction
# 6. <<, >> Bitwise left and right shifts
# 7. & Bitwise AND
# 8. ^ Bitwise XOR
# 9. | Bitwise OR
# 10. ==, !=, >, >=, <, <=, is, is not, in, not in Comparisons, identity, and membership
# 11. not Logical NOT
# 12. and Logical AND
# 13. or Logical OR

# Examples of precedence:
print(5 + 4 * 10)      # 45 (Multiplication before addition)
print((5 + 4) * 10)    # 90 (Parentheses first)
print(10 / 2 + 3)      # 8.0 (Division before addition)
print(2 ** 3 * 2)      # 16 (Exponentiation before multiplication)
