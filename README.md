harhacker
=========

### Setup Development

    # Install virtualenv (if not already installed)
    sudo pip install virtualenv

    # Build and install dependencies
    virtualenv deps

    # Active virtualenv
    source deps/bin/activate

    # Install requirements
    pip install -Ur harhacker/requirements/project.txt

### Run Development

    # Active virtualenv
    source deps/bin/activate

    # Start server
    python harhacker/manage.py runserver

### Tips and Tricks

If you checkout the project with `git clone git@github.com:danmcc/har-rage.git harhacker`
you can use the following [bash function][bash] to quickly interact with
manage.py.

[bash]: https://github.com/silas/config/blob/f6df7008510b34a5a40eb20c976234dcd42d82c6/.bashrc#L33
