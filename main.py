# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections

# my solution using dfs to traverse graph
"""class Subject:
    def __init__(self, number=0, needs=None):
        self.number = number
        self.needs = needs if needs else []


def dfs(hashT, numCourses):
    for i in range(0, numCourses):
        q = collections.deque()
        q.append(hashT[i])
        while q:
            current = q.pop()
            for need in current.needs:
                if need == hashT[i]:
                    return False
                q.append(need)
    return True


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        hashT = {}
        for i in range(0, numCourses):
            hashT[i] = Subject(i)
        for i in range(0, len(prerequisites)):
            hashT[prerequisites[i][0]].needs.append(hashT[prerequisites[i][1]])
        return dfs(hashT, numCourses)"""


# better time complexity, no need for using graph. hashmap will do
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        preMap = {i: [] for i in range(0, numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if not preMap[crs]:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                visitSet.remove(crs)
                preMap[crs] = []
                return True
        for cors in range(0, numCourses):
            if not dfs(cors):
                return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.canFinish(5, [[1, 0], [0, 4], [4, 1], [3, 2], [3, 4]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
