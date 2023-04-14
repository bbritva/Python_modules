import time


def ft_progress(list):
    start = time.time()
    start_value = list[0]
    end_value = list[len(list) - 1]
    diff = end_value - start_value
    if diff == 0:
        diff = 1
    eta = 0
    for i in list:
        now = time.time() - start
        percent = 100 * (i - start_value) / diff
        if i == end_value:
            percent = 100
        if percent > 0:
            eta = 100 * now / percent
        filled = int(percent / 5)
        if filled == 20:
            empty = 0
        else:
            empty = 19 - filled
        line = "ETA: %5.2fs [%3d%%] " % (eta, percent)
        line += "[" + '=' * filled + '>' * (filled != 20) + ' ' * empty + '] '
        line += "%4d/%4d | elapsed time %5.2fs" % (i, end_value, now)
        print(line, end="\r")
        yield i


if __name__ == "__main__":
    listy = range(100)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.001)
    print()
    print(ret)
