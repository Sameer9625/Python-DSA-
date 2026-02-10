class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        firstIndex = scIndex = None

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1
                if count == 1:
                    firstIndex = i
                elif count == 2:
                    scIndex = i
                else:
                    return False   # more than 2 mismatches

        # no mismatches → already equal
        if count == 0:
            return True

        # exactly two mismatches → check swap condition
        if count == 2:
            return (
                s1[firstIndex] == s2[scIndex] and
                s1[scIndex] == s2[firstIndex]
            )

        return False