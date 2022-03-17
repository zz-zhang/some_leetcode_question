from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = []
        deck = sorted(deck, reverse=True)
        # print(deck)

        while len(deck) > 0:
            # print(deck)
            # step 3
            if len(res) == 0:
                res.append(deck[0])
                deck = deck[1:]
                continue
            # step 2
            res = [res[-1]] + res[:-1]
            # step 1
            res = [deck[0]] + res

            deck = deck[1:]
            print(res)

        print(self.verify(res))
        return res

    def verify(self, deck):
        popped = []
        while len(deck) > 0:
            # step 1
            popped.append(deck[0])
            deck = deck[1:]
            
            # step 2
            if len(deck) > 0:
                deck = deck[1:] + [deck[0]]
        print(popped)
        for num1, num2 in zip(popped[:-1], popped[1:]):
            if num1 > num2:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    deck = [1,2,3,4,5]
    print(sol.deckRevealedIncreasing(deck))