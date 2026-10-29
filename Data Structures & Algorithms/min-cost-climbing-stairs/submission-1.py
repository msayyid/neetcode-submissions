class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def cost_from(i):
            if i >= len(cost):
                return 0


            one_step = cost[i] + cost_from(i + 1)

            two_steps = cost[i] + cost_from(i + 2)
            # print(one_step)


            return min(one_step, two_steps)

        return min(cost_from(0), cost_from(1))