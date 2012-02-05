harhacker
=========

### Setup RabbitMQ (OS X)

Install homebrew

    ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

Install rabbitmq

    brew install rabbitmq

Ensure hostname never changes (required for rabbitmq)

    sudo scutil --set HostName myhost.local

Add hostname to `/etc/hosts`

    127.0.0.1       localhost myhost myhost.local

Start rabbitmq

    sudo rabbitmq-server -detached

Stop rabbitmq (just an FYI)

    sudo rabbitmqctl stop

### Setup BrowserMob Proxy

Download latest binary release

    wget https://github.com/downloads/webmetrics/browsermob-proxy/browsermob-proxy-2.0-beta-3-bin.zip

Extract and rename

    unzip browsermob-proxy*.zip
    mv $( ls -d browsermob-proxy* ) browsermob-proxy

Make shell script executable

    chmod 755 browsermob-proxy/bin/browsermob-proxy

### Setup Python

Install pip

    sudo easy_install pip

Install virtualenv

    sudo pip install virtualenv

### Setup Django Project

Checkout repository

    git clone git@github.com:danmcc/har-rage.git harhacker

Build and install dependencies

    virtualenv deps

Active virtualenv

    source deps/bin/activate

Install requirements

    pip install -Ur requirements.txt

Create sqlite database

    python harhacker/manage.py syncdb

### Run Django Project

Active virtualenv

    source deps/bin/activate

Run web

    python harhacker/manage.py runserver

Run tasks

    python harhacker/manage.py celeryd -l debug

### Tips and Tricks

 * Use `python harhacker/manage.py shell` to experiment
 * If you checkout the project to a directory named `harhacker` you can use the
following [bash function][bash] to quickly interact with manage.py.

[bash]: https://github.com/silas/config/blob/f6df7008510b34a5a40eb20c976234dcd42d82c6/.bashrc#L33
[rabbitmq-osx]: http://ask.github.com/celery/getting-started/broker-installation.html
