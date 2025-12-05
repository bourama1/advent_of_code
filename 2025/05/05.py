from bisect import bisect_right


def parse_ranges_and_check_ids(path="input.txt"):
    ranges = []
    fresh_ids = []

    with open(path, "r", encoding="utf-8") as f:
        # read range lines until blank line
        for line in f:
            s = line.strip()
            if s == "":
                break
            a, b = s.split("-")
            ranges.append((int(a), int(b)))

        # merge overlapping/adjacent ranges
        ranges.sort()
        merged = []
        for a, b in ranges:
            if not merged or a > merged[-1][1] + 1:
                merged.append([a, b])
            else:
                if b > merged[-1][1]:
                    merged[-1][1] = b

        # prepare for fast containment checks
        starts = [r[0] for r in merged]

        # process remaining lines as ids (streaming, no large memory use)
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                x = int(s)
            except ValueError:
                continue
            idx = bisect_right(starts, x) - 1
            if idx >= 0 and merged[idx][0] <= x <= merged[idx][1]:
                fresh_ids.append(x)

    return merged, fresh_ids


def calc_fresh_ids(merged_ranges):
    sum_counts = 0
    for range_start, range_end in merged_ranges:
        count = range_end - range_start + 1
        sum_counts += count
    return sum_counts


if __name__ == "__main__":
    merged_ranges, fresh_ids = parse_ranges_and_check_ids()
    print("Merged ranges:", merged_ranges)
    print("Matching ids (count):", len(fresh_ids))
    print("Matching ids sample (first 100):", fresh_ids[:100])
    print("Total count of fresh ids in merged ranges:", calc_fresh_ids(merged_ranges))
