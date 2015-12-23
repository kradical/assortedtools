# alphabetizes an input file by line

def main():
    with open('acronyms.txt', 'r+') as fp:
        lines = fp.read().split('\n')
        lines.sort(key=lambda x: x.lower())
        fp.seek(0)
        fp.write('\n'.join(lines))

if __name__ == '__main__':
    main()