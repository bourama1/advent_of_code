import re

pattern = re.compile(r'^(\d+)\1+$')

def is_repeating(num):
    return bool(pattern.match(str(num)))

def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            values = line.strip().split(",")
            wrongs_ids = []
            for value in values:
                range_start, range_end = map(int, value.split("-"))
                for num in range(range_start, range_end + 1):
                    if is_repeating(num):
                        wrongs_ids.append(num)
            print(f"Input: {line.strip()}\nRepeating IDs: {wrongs_ids}")
            print(f"Sum of Repeating IDs: {sum(wrongs_ids)}")

if __name__ == "__main__":
    main()