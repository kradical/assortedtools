def main():
    with open('input.txt', 'r') as fp:
        nonblanklines = [x for x in fp if not x.isspace()]
        print(len(nonblanklines))

if __name__ == '__main__':
    main()