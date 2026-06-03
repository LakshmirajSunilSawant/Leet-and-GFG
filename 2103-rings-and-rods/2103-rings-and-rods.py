class Solution(object):
    def countPoints(self, rings):
        rods = [set() for _ in range(10)]

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)

        count = 0
        for colors in rods:
            if len(colors) == 3:
                count += 1

        return count