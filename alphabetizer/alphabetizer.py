# alphabetizes an input file by line

def main():
    with open('acronyms.txt', 'r+') as fp:
        lines = fp.read().split('\n')
        lines.sort()
        fp.seek(0)
        fp.write('\n'.join(lines))

if __name__ == '__main__':
    main()