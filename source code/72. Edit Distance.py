import queue

class Solution:
    def replace(self, str, i, dict, j):
        res = ''
        res[i] = dict[j]
        return res

    def removeZero(self, str):
        res = ""
        for i in str:
            if i != '0':
                res.append(i)
        return res

    def similar(self, str1, str2):
        res = 0
        s1 = ""
        s2 = ""
        if len(str1) < len(str2):
            s1 = str2
            s2 = str1
        else:
            s1 = str1
            s2 = str2

        for i in range(0, len(s1)):
            sim = 0
            for j in range(0, len(s2)):
                if i + j >= len(s1):
                    break
                if s1[i + j] == s2[i + j]:
                    sim += 1
            if sim > res:
                res = sim
        return res

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        target = word2
        dict = target + "0"
        q = queue.Queue()
        q.put(word1)
        qdepth = queue.Queue()
        qdepth.put(0)
        while not q.empty():
            str = q.get()
            dep = qdepth.get()
            if str == target:
                return dep

            for i in range(0, len(str)):
                maxSim = 0
                simList = []
                strList = []

                for j in range(0, len(dict)):
                    strTemp = self.replace(str, i, dict, j)
                    strTemp = self.removeZero(strTemp)
                    sim = self.similar(target, strTemp)
                    simList.append(sim)
                    strList.append(strTemp)
                for k in range(0, simList):
                    if simList[k] == maxSim:
                        q.put(strList[k])
                        qdepth.put(dep + 1)
            q.pop()
            qdepth.pop()


if __name__ == '__main__':
    sol = Solution()
    word1 = 'horse'
    word2 = 'ros'
    print(sol.minDistance(word1, word2))