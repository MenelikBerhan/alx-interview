#!/usr/bin/python3
"""Make Change puzzle solution
"""


def makeChange(coins, total):
    """Finds no. coins that add up to `total`."""

    def helper(coins, total, taken=[], memo={}):
        """helper for main function"""
        if len(coins) == 1 and total % coins[0] == 0:
            return taken + ([coins] * total // coins[0])
        # key = str(total) + ':' + ','.join(coins)
        # if key in memo:
        #     return taken + memo[key]
        solutions = []
        for i, coin in enumerate(coins):
            if total == coin:
                solutions.append(taken + [coin])
                break
            if coin < total:
                i_tmp = i
                while (i_tmp < len(coins) and coins[i_tmp] > (total - coin)):
                    i_tmp += 1
                if i_tmp < len(coins):
                    c_tmp = coins[i_tmp:]
                    t_tmp = taken + [coin]
                    tot_t = total - coin
                    # key_t = str(tot_t) + ':' + ','.join(c_tmp)
                    # if key_t in memo:
                    #     solution = memo[key_t]
                    solution = helper(c_tmp, tot_t, t_tmp, memo)
                    if solution is not None:
                        solutions.append(solution)
        best_sol = None
        # best_len = -1
        for sol in solutions:
            if best_sol is None:
                best_sol = sol
            elif len(best_sol) > len(sol):
                best_sol = sol
        return best_sol

    if total <= 0:
        return 0
    ans = helper(coins, total)
    if ans is None:
        return -1
    return len(ans)
