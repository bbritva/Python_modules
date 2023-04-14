class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if len(x) == 0:
            return None
        return sum(x) / len(x)
    
    def median(self, x):
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        return x[len(x) // 2]
    
    def quartile(self, x):
        if len(x) == 0:
            return None
        x.sort()
        if len(x) % 2 == 0:
            a1 = self.median(x[:len(x) // 2])
            a2 = self.median(x[len(x) // 2:])
            return [a1, a2]
        a1 = self.median(x[:len(x) // 2 + 1])
        a2 = self.median(x[len(x) // 2:])
        return [a1, a2]
    
    def var(self, x):
        if len(x) == 0:
            return None
        mean = self.mean(x)
        return sum([(i - mean) ** 2 for i in x]) / len(x)
     
    def std(self, x):
        if len(x) == 0:
            return None
        return self.var(x) ** 0.5
    
if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.quartile(a))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862