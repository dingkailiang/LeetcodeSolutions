import importlib
import sys

if len(sys.argv) < 2:
    print("usage: {} question#".format(sys.argv[0]))
    exit(1)

question = sys.argv[1] 
m = importlib.import_module('.' + question,"solutions")
solution = m.Solution()
for case in m.TESTCASES:
    print("--- Input ---")
    print(case)
    print("--- Output ---")
    func = getattr(solution,m.METHOD)
    if isinstance(case,tuple):
        output = func(*case)
    else:
        output = func(case)
    print(output)
    print()