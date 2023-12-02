class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        return sum(len(word) for word in words if Counter(word) <= chars_count)
        