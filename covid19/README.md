## `covid19`
Custom code written for the project that is *not* executed directly, but is
called from files in the `code` directory.

#### **Installing module**
In order to use the functions within the `covid19` module it is necessary to
install the package locally. This can simply be done by navigating in the
terminal to the main project directory and typing the command
```
pip install -e ./
```
The `setup.py` file will take care of the installation. The `-e` option within
the package allows for the constant update of the package as it might be
subject to changes as the project is being developed.

The modules contained in the package include:
- `viz.py` : functions for data visualization and plot styling.