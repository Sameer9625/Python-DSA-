# for ch in string:
#     if ch is opening bracket:
#         stack.push(ch)

#     elif ch is closing bracket:
#         if stack is empty:
#             return False
        
#         if stack.top() matches ch:
#             stack.pop()
#         else:
#             return False

# return stack is empty

# def isBalanced(s):
#     stack = []

#     # Dictionary for matching brackets
#     bracket_map = {')': '(', '}': '{', ']': '['}

#     for ch in s:
#         # If opening bracket → push
#         if ch in "({[":
#             stack.append(ch)

#         # If closing bracket → check matching
#         elif ch in ")}]":
#             if not stack:
#                 return False

#             if stack[-1] == bracket_map[ch]:
#                 stack.pop()
#             else:
#                 return False

#     return len(stack) == 0


# # Driver code
# s = input().strip()
# print(isBalanced(s))

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in "({[":
                stack.append(ch)

            elif ch in ")}]":
                if not stack:
                    return False

                if stack[-1] == bracket_map[ch]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0