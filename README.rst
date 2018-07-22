===================================
Test Driven Development with Python
===================================

To run selenium with Raspberry Pi 2. Install firefox esr version that ships
with Raspbian.

    $ sudo apt-get install firefox-esr

Geckodriver is also required for it to work. The version of geckodriver
is very important as it won't run otherwise. The correct version to use
with the Raspbian 2 is geckodriver-v0.17.0-arm7hf.tar.gz. This can be done
as follows:

    $ wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-arm7hf.tar.gz
    $ tar -xvzf geckodriver-v0.17.0-arm7hf.tar.gz
    $ rm geckodriver-v0.17.0-arm7hf.tar.gz
    $ chmod +x geckodriver
    $ cp geckodriver /usr/local/bin/
    $ rm -rf geckodriver

You will also need bootstrap for this project

    $ wget -O bootstrap.zip https://github.com/twbs/bootstrap/releases/download/v3.3.4/bootstrap-3.3.4-dist.zip
    $ unzip bootstrap.zip
    $ mkdir lists/static
    $ mv bootstrap-3.3.4-dist lists/static/bootstrap
    $ rm bootstrap.zip

Deployment Instructions
=======================

Deployment is done using Fabric.

    $ git push
    $ cd deploy_tools
    $ fab deploy:host=steve@DOMAIN

On Server:

    steve@server:$ sudo systemctl restart GUNICORN_SERVICE

Staging Server: superlists-staging.ga
Prod Server: superlists.ga


