# Write your code here

import sys

if len(sys.argv) != 3:
    print("Usage: python3 main.py <initials> <nickname>")
    sys.exit(1)

initials = sys.argv[1]
nickname = sys.argv[2]

print("-" * 20)
print(f"Initials: {initials}")
print(f"Nickname: {nickname}")
print("-" * 20)
