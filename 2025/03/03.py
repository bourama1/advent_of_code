def main():
    TOP_K = 12

    def max_subsequence(s: str, k: int) -> str:
        n = len(s)
        if k > n:
            raise ValueError(f"k ({k}) is larger than line length ({n})")
        res = []
        start = 0
        for remaining in range(k, 0, -1):
            end = n - remaining + 1  # exclusive end for search window
            # find max character in s[start:end]
            max_ch = max(s[start:end])
            idx = s.find(max_ch, start, end)
            res.append(max_ch)
            start = idx + 1
        return "".join(res)

    with open("input.txt", "r", encoding="utf-8") as f:
        total = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            print(line)
            picked = max_subsequence(line, TOP_K)
            print(picked)
            total += int(picked)
        print(f"Sum: {total}")


if __name__ == "__main__":
    main()
