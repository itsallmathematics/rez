import sys
from profile import Profile

def main(argv):
    prof = Profile()
    prof.load()
    print(prof)


if __name__ == '__main__':
    main(sys.argv)
