import linecache
import os
import tracemalloc
import sys
import main

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

min_lookup = [i for i in range(500000)]
max_lookup = [1 for i in range(500000)]
print((sys.getsizeof(min_lookup) + sys.getsizeof(max_lookup))/1048576)


# 1000000 x 4 = 4000000 bytes = ~4 MB (1 MB = ~1000000 B)
# For CPP integer =  4 bytes, but for python 28

# Empty list = 56 bytes, + every integer equals + every pointer on integer
# which is + 8 bytes

# My case: 2 lists for about 500000 integers each is at least
# 2*(500000 * 8 + 56) = 8.000.112 bytes = 8 MB

tracemalloc.start()
main.start_point()
snapshot = tracemalloc.take_snapshot()
display_top(snapshot)

print(sys.getsizeof([i for i in range(2*500000)]))

print(sys.getsizeof([0, 0, 0, 0, 0,0 , 0,0 , 0, 3]))
print(sys.getsizeof([2222, 111, 22, 33, 44, 55,66 , 1 , 2, 3]))

