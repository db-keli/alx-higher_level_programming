#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    print("{:d} arguments".format(len(argv)))
    count = 1
    for arg in argv:
        print("{:d}: {:s}".format(count, arg))
        count += 1
