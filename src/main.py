import sys
from profile import Profile

def main(argv):
    prof = Profile()
    prof.promptData()
    print(prof)


if __name__ == '__main__':
    main(sys.argv)
