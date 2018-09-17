import importlib
import sys

if len(sys.argv) < 2:
    print("usage: {} question# [testcase]".format(sys.argv[0]))
    exit(1)

testcase = map(lambda x : int(x) if x.isnumeric() else x, sys.argv[2:])
question = sys.argv[1] 



m = importlib.import_module('.' + question,"solutions")
solution = m.Solution()
output = getattr(solution,m.METHOD)(*testcase)
print("Output: ",output)