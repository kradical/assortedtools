import urllib.request

def get_page_content():
    pass

def main():
    with open('Structure and Interpretation of Computer Programs.html', 'a') as fp:
        for x in range(5, 36):
            with urllib.request.urlopen('https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-' + str(x) + '.html') as response:
                page_html = response.read()
            fp.write(str(page_html).split(']')[1].split('[')[0])

if __name__ == '__main__':
    main()