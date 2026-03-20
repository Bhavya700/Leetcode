class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count_map = Counter(words)
        len_word = len(words[0])
        res = []

        for low in range(len_word):
            start = low
            window = defaultdict(int)
            words_used = 0

            for high in range(low, len(s) - len_word + 1, len_word):
                curr_word = s[high : high + len_word]

                if curr_word not in word_count_map:
                    start = high + len_word

                    window = defaultdict(int)
                    words_used = 0
                    continue
                
                words_used += 1
                window[curr_word] += 1
            
                while window[curr_word] > word_count_map[curr_word]:
                    window[s[start : start + len_word]] -= 1
                    words_used -= 1
                    start += len_word

                if words_used == len(words):
                    res.append(start)
            
        return res