import time

def ft_progress(list):
    start = time.time()
    max_value = max(list)
    elapsed = 0
    for i in list:
        now = time.time() - start
        percent = 100 * (i) / max_value
        if percent > 0:
            elapsed = (100 - percent) * now / percent
        filled = int(percent / 5)
        if filled == 20:
            empty = 0
        else:
            empty = 19 - filled
        line = "ETA: %5.2fs [%3d%%]" % (now, percent)
        line += "[" + '=' * filled +'>' * (filled != 20) + ' ' * empty + ']'
        line += "%4d/%4d | elapsed time %5.2fs" % (i + 1, max_value + 1, elapsed)
        print(line, end="\r")
        yield i

"====================>"
if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

    "ETA: 8.67s [ 23%][=====> > ] 233/1000 | elapsed time 2.33s"