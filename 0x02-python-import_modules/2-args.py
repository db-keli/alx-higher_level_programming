#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    print("{:d} arguments".format(len(args) - 1))
    count = 1
    for arg in args:
        print("{:d}: {:s}".format(count, arg))
        count += 1
