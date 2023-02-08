class Solution:
    def countOdds(low: int, high: int) -> int:
        
        return ((high - low) // 2) + 1 if high % 2 != 0 or low % 2 != 0 else (high - low) // 2

    if __name__ == "__main__":
        countOdds(int(input()), int(input()))