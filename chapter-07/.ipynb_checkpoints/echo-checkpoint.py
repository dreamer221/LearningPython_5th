import sys

args = sys.argv
print("参数个数:", len(args))

for i, arg in enumerate(sys.argv):
    print(f"参数 {i}: {arg}")