def main():
    with open('input.txt', 'r+') as inputfile:
        with open('output.txt', 'w') as outputfile:
            outputfile.write(4*" " + "/**\n" + 6*" " + "* <pre>\n")
            for line in inputfile:
                elems = line.split(',')
                try:
                    req = elems[3].strip('"')
                    desc = elems[4].strip('"')
                    if len(req) > 3 and req[:3] == 'SSP':
                        outputfile.write(6*" " + "* " + req + " " + desc + "\n")
                except IndexError:
                    continue

if __name__ == '__main__':
    main()