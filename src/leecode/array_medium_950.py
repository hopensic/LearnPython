from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        deq = deque()
        deck.sort(reverse=True)
        deq.appendleft(deck[0])
        for i in deck[1:]:
            deq.appendleft(deq.pop())
            deq.appendleft(i)
        return deq


lst = [17, 13, 11, 2, 3, 5, 7]
s = Solution()
print(s.deckRevealedIncreasing(lst))
