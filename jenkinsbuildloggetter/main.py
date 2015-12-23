import sys
import urllib.request
import re

def get_latest_build_num(name):
    with urllib.request.urlopen(name) as response:
        html = response.read()
        match = re.search('Last build (#', html)
        return html[match.end()]

def main():
    if len(sys.argv) == 3:
        project_name = sys.argv[1]
        build_num = sys.argv[2]
    elif len(sys.argv) == 2:
        project_name = sys.argv[1]
        build_num = get_latest_build_num(project_name)
    else:
        print('Usage: python main.py project link [build number]')
    
    print(build_num)
    link = project_name + '/' + build_num + '/consoleFull'
    
    with urllib.request.urlopen(link) as response:
        html = response.read()
        matchstart = re.search('<pre>', html)
        matchend = re.search('</pre>', html)

        with open('log.txt', 'w') as file:
            file.write(html[matchstart.end():matchend.start()])
   
if __name__ == '__main__':
    main()