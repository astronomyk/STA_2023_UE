# FAQs for installing Python

Please note:
- The code lines below are to be run in the command line of your choice:
- Code lines beginning with `$` are to be run in the command line tool of your choice
- Lines beginning with `>>>` are to be run inside python. 
  - Enter python by either starting Jupyter Lab, or from the command line


## What you need for STA_2023_UE:
- A working installation of Python (v3.12)
  - https://www.python.org/downloads/
- A working installation of Jupyter Lab
  - `$ pip install jupyterlab`
- The following 3rd-party python packages
  - `$ pip install numpy scipy astropy matplotlib`

## FAQs for the introduction to Python

### What is the command line?

Answer: That black box with green text used by hackers and computer nerds. 
Might be white or off-white too.

### How do I open the command line?

Answer (Windows): Windows key. Type `cmd`. Hit enter.

Answer (Apple Macs): ??? 

### Do I need PyCharm or any other IDE (e.g. Spyder)?
Answer: No. For STA_2023W you will only need Jupyter Lab for running python notebooks.
But there is no harm in using it and it might make your life easier at times.

### Python runs from Windows start menu, but not from the command line
Answer: Reinstall python and click the "Add Python to PATH" box 

See Step 3 of <https://linuxhint.com/add-python-windows-path/>

### I have no `pip` on my laptop to install extra packages
Answer: In command line type: 

    $ python -m ensurepip --upgrade

<https://pip.pypa.io/en/stable/installation/>

### Pip install error: `Microsoft Visual C++ 14.0 required`
Answer: Install certain elements of Visual Studio

<https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst>

### Pip install error: `Rust not found - "Cargo, the Rust package manager, is not installed or is not on PATH"`

Answer: Install Rust via <https://rustup.rs/>

### How to start Python?
Answer: In command line type:
    
    $ python

### How to start Jupyter Lab?
Answer: In command line type:

    $ jupyter lab

### How to check whether 3rd-party packages are installed
Answer: In python import the packages

    >>> import astropy

If the package is installed, nothing will be printed and
you can now use all the functionality from the `astropy` module.
Otherwise, if a package is not installed, Python will complain:

    >>> import does_not_exist
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'does_not_exist'
