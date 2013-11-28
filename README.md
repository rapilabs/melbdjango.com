melbdjango.com
==============

Requirements found here https://gist.github.com/sesh/7132492

Stories: https://docs.google.com/document/d/1lJNEBDHu-F3Vz6MY7igz6z-T-7fAcVdyYTCXOKsSOH8

Getting Started
===============

Clone this repo:

    git clone git@github.com:danni/melbdjango.com.git

Set up virtualenv:

    virtualenv python_env
    . python_env/bin/activate

Update the packages:

    pip install -r requirements.txt
    
Initialise the database:

    cd melbdjango
    ./manage.py syncdb
    
Migrate the modules:

    ./manage.py sync <module-name>

Start hacking!
