import os
from wb import system, config, home_fn, cd_home

os.environ['PATH'] += ";%s\\VC" % (os.path.normpath(config['MSVC']),)

def build_vc(cmd):
    system('cmd /c "vcvarsall.bat x86 && %s"' % (cmd,))

def main():
    cd_home()
    build_vc("nmake /f %s" % (home_fn('msvc.mak'),))

# if we are run directly, and not loaded as a module
if __name__ == "__main__":
    main()
