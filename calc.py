import sys

x = []
for line in open(sys.argv[1]):
   num = int(line)
   x.append(num)

avg = sum(x) / float(len(x))

diffs = []
for num in x:
   diff = num - avg
   diffs.append(diff**2)

print 'average is', sum(x) / float(len(x))
print 'sumsqdiffs is', sum(diffs)
