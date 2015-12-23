def main():
    with open('input.txt', 'r+') as inputfile:
        outputstring = []
        outputstring.append(4*" " + "/**\n" + 6*" " + "* <pre>\n")
        for line in inputfile:
            elems = line.split(',')
            try:
                req = elems[3].strip('"')
                desc = elems[4].strip('"')
                if len(req) > 3 and req[:3] == 'SSP':
                    if 6*" " + "* " + req + " " + desc + "\n" not in outputstring:
                        outputstring.append(6*" " + "* " + req + " " + desc + "\n")
            except IndexError:
                continue
        with open('output.txt', 'w') as outputfile:
            outputfile.write("".join(outputstring))

if __name__ == '__main__':
    main()