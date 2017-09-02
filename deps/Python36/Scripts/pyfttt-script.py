#!c:\users\trendy\appdata\local\programs\python\python36\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyfttt==0.3','console_scripts','pyfttt'
__requires__ = 'pyfttt==0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyfttt==0.3', 'console_scripts', 'pyfttt')()
    )
