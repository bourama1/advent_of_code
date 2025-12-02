# Script: count_zero_crossings.py
# Starting position: 50
# Dial: 0–99 circular
# Input lines: L45, R32, ...
# Counts:
# 1) times the dial *lands* on 0 -> was first version of quest
# 2) times the dial *passes through* 0 during a move


def main():
    position = 50
    passed_zero = 0

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().upper()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])

            if direction == "L":
                step = -value
            else:
                step = value

            old_pos = position
            position = (position + step) % 100
            print(
                f"Move from {old_pos} to {position} ({'L' if step < 0 else 'R'}{value})"
            )

            # Count passes through 0
            if old_pos == 0 and direction == "L":
                passed_zero -= 1  # Adjust for starting on zero #! cant skipped it because there can be more then 100 move

            if step > 0:  # Moving upward
                total = old_pos + step
                passed_zero += total // 100
            else:  # Moving downward
                total = old_pos + step
                if old_pos <= value:
                    total = -(total - 100)
                passed_zero += total // 100

            print(f"  Passed through 0 so far: {passed_zero}")

    print(f"Passed through 0: {passed_zero}")


if __name__ == "__main__":
    main()
