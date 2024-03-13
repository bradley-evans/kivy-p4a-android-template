import os
import sys
import traceback

from myapp.gui import gui


def main():
    print(f"sys.path: {sys.path}")
    try:
        gui()
    except Exception as err:
        print(f"Critical exception. Error:\n{err}")
        traceback.print_exc()

if __name__=='__main__':
    main()
