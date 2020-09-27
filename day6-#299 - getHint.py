class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        A = 0
        B = 0
        S = []
        G = []
        for i, con in enumerate(guess):

            if con == secret[i]:
                A += 1
            else:
                S.append(secret[i])
                G.append(con)
        for i in S:
            if i in G:
                B = B + 1
                G[G.index(i)] = "x"
        return str(A) + 'A' + str(B) + 'B'