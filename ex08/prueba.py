import time

def ft_bar(lst, timein):
    for i, item in enumerate(lst):
        progress = (i + 1) / len(lst) * 100
        bar = "[" + "#" * int(progress // 5) + " " * (20 - int(progress //5)) + "]"
        elapsed_time = time.time() - timein
        eta = elapsed_time / progress * (100 - progress)
        print(f"ETA: {eta:.2f}s [{progress:.2f}%][{bar}] {i+1}/{len(lst)} | elapsed time {elapsed_time:.2f}s | estimated time {eta:.2f}s", end="\r")
        yield item

if __name__ == '__main__':
    my_list = range(3333)
    ret = 0
    timein = time.time()
    for item in ft_bar(my_list, timein):
        ret += item
        time.sleep(0.005)
    print()
    print(ret)