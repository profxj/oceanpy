******************
Installing oceanpy
******************

This document describes how to install the `oceanpy`
repository.

Installing Dependencies
=======================

We will aim to keep the number of dependencies low.

In general, we recommend that you use Anaconda for the majority of
these installations.

Detailed installation instructions are presented below:

Standard Dependencies
---------------------

oceanpy depends on the following list of standard Python packages.

We recommend that you use `Anaconda <https://www.continuum.io/downloads/>`_
to install and/or update these packages.

* `python <http://www.python.org/>`_ versions 3.7 or later
* `numpy <http://www.numpy.org/>`_ version 1.18 or later
* `scipy <http://www.scipy.org/>`_ version 1.2 or later
* `pandas <https://pandas.pydata.org/>`_ version 0.25 or later

If you are using Anaconda, you can check the presence of these packages with::

	conda list "^python|numpy|scipy|pandas"

If the packages have been installed, this command should print
out all the packages and their version numbers.


Less Standard Dependencies
--------------------------

* `healpy <https://healpy.readthedocs.io/en/latest/index.html>`_ version 1.12 or later
* `iris <https://scitools.org.uk/iris/docs/latest/installing.html>`_ version 2.4 or later
