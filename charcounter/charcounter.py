def main():
    total_length = 0
    with open('input.txt', 'r') as fp:
        data = fp.read()
        print(len(data))

if __name__ == '__main__':
    main()