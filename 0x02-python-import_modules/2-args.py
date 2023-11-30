#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv)
    inde = 0
    if le == 1:
        print("0 arguments.")
    elif le > 1:
        if le == 2:
            print(f"{le - 1} argument:")
        else:
            print(f"{le - 1} arguments:")
        for i in sys.argv[1:]:
            inde += 1
            print(f"{inde}: {i}")
