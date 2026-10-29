class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        for a in asteroids:
            if answer:
                asteroid = answer[-1]
                if asteroid > 0 and a < 0:
                    if asteroid + a != 0:
                        answer.append(max(answer.pop(), a))
                    else:
                        answer.pop()
                elif asteroid < 0 and a > 0:
                    if asteroid + a != 0:
                        answer.append(max(answer.pop(), a))
                    else:
                        answer.pop()
                else:
                    answer.append(a)
            else: 
                answer.append(a)
        print(answer)
        return answer
            