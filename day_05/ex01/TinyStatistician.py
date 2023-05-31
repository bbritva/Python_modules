
def _guard_(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception:
            return None
    return wrapper


class TinyStatistician:

    @_guard_
    def mean(self, x):
        return sum(x) / len(x)

    @_guard_
    def median(self, x):
        return self.percentile(x, 50)

    @_guard_
    def quartile(self, x):
        return [self.percentile(x, 25), self.percentile(x, 75)]

    @_guard_
    def percentile(self, x, p):
        """computes the expected percentile of a given non-empty list or
        array x. The method returns the percentile as a float, otherwise None if x is an
        empty list or array or a non expected type object. The second parameter is the
        wished percentile."""
        x.sort()
        i = (len(x) - 1) * p / 100
        if i.is_integer():
            return x[int(i)]
        floor = int(i)
        res = x[floor] * (floor + 1 - i) + x[floor + 1] * (i - floor)
        return res

    @_guard_
    def var(self, x):
        mean = self.mean(x)
        return sum([(i - mean) ** 2 for i in x]) / len(x)

    @_guard_
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
