import sys


def uniq(input):
    unique = []
    remove = []
    for ch in input:
        if ch not in unique:
            unique.append(ch)
        else:
            remove.append(ch)
    return sorted(set(unique) - set(remove))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            print(uniq(sys.argv[1]))
        except Exception:
            print("Something went wrong")
    else:
        print("Parameter missing\n Usage: unique.py <string>")
        exit(-1)
