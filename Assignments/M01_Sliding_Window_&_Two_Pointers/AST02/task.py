def Check_Palindrome(n: int, s: str) -> bool:
    left, right = 0, n - 1

    while left < right:
        if s[left] != s[right]:
            return (
                s[left + 1:right + 1] == s[left + 1:right + 1][::-1]
                or
                s[left:right] == s[left:right][::-1]
            )
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    print(Check_Palindrome(n, s))
