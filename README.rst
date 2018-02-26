[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
.. image:: https://img.shields.io/badge/license-WTFPL-green.svg
   :target: https://github.com/SnoozeTime/kucoin-trade-report/blob/master/LICENSE.txt


Download your Kucoin trades as CSV file
----------------------------------------

Install
==========

You'll need python3 to run the downloader. Easiest way to set up is to create a new virtualenv and download the requirements
using the requirements.txt file and pip

.. code-block:: bash

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt


Config
======
Change the config.py file to use your API KEY and SECRET from Kucoin.
See how to create the API key and secret here: `post on steemit about API keys`_

Run
===
Just run with python

.. code-block:: bash

    python download_as_csv.py

Donation
========

If the tool was useful to you, please consider donating ;)

ETH at: 0xE58f3b911b04e997d9d21F39DFAB82c63275415D
BTC at: 1ByrzH4zJ9ArfqfN8NJGioyuweN7yamGtV

.. _post on steemit about API keys: https://steemit.com/cryptocurrency/@jeremypeng/tutorial-about-how-to-auto-manage-your-kucoin-portfolio-using-api-key
