
To run selenium with Raspberry Pi 2. Install firefox esr version that ships
with Raspbian.

    >>> sudo apt-get install firefox-esr

Geckodriver is also required for it to work. The version of geckodriver
is very important as it won't run otherwise. The correct version to use
with the Raspbian 2 is geckodriver-v0.17.0-arm7hf.tar.gz. This can be done
as follows:

    >>> wget
    https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-arm7hf.tar.gz
    >>> tar -xvzf geckodriver-v0.17.0-arm7hf.tar.gz
    >>> rm geckodriver-v0.17.0-arm7hf.tar.gz
    >>> chmod +x geckodriver
    >>> cp geckodriver /usr/local/bin/
    >>> rm -rf geckodriver

