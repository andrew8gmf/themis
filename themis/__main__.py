import sys

from pyfiglet import Figlet

def main():
    f = Figlet(font='slant')
    print(f.renderText('themis')) 

if __name__ == '__main__':
    main()