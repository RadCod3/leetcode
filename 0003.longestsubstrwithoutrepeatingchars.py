def lengthOfLongestSubstring(s: str) -> int:
    char_locs = {}
    max_val = 0
    curr_subs_start = 0

    for idx, char in enumerate(s):
        if char in char_locs:
            char_loc = char_locs[char]
            if char_loc >= curr_subs_start:
                curr_subs_start = char_loc + 1

        char_locs[char] = idx
        max_val = max(idx - curr_subs_start + 1, max_val)

    return max_val


print(lengthOfLongestSubstring("abba"))
