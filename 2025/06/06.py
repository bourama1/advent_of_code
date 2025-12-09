def main():
    # Read lines without stripping so alignment stays intact
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Last line = operators aligned with columns
    operator_line = lines[-1]
    digit_lines = lines[:-1]

    width = max(len(line) for line in lines)
    # Pad lines so all have equal width
    digit_lines = [line.ljust(width) for line in digit_lines]
    operator_line = operator_line.ljust(width)

    problems = []
    current_cols = []

    # Scan columns right→left
    for col in range(width - 1, -1, -1):
        col_chars = [row[col] for row in digit_lines]
        op_char = operator_line[col]

        if all(c == " " for c in col_chars) and op_char == " ":
            # This is a separator column
            if current_cols:
                problems.append(current_cols)
                current_cols = []
        else:
            current_cols.append((col_chars, op_char))

    # Add final problem if present
    if current_cols:
        problems.append(current_cols)

    results = []
    for problem in problems:
        print("Processing problem with columns:", problem)
        numbers = []
        operator = None

        # Each item in problem = (digits_in_column, operator_at_bottom)
        for col_chars, op_char in problem:
            if op_char.strip():
                operator = op_char  # The operator for this problem

            # Build the number from this column
            digits = "".join(c for c in col_chars if c.isdigit())
            if digits:
                numbers.append(int(digits))

        if operator == "+":
            result = sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n

        results.append(result)

    # Print results in the required order
    for i, v in enumerate(results, 1):
        print(f"Problem {i}: {v}")

    print("Sum of results:", sum(results))


if __name__ == "__main__":
    main()
