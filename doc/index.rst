.. logilab common documentation master file, created by
   sphinx-quickstart on Thu May 23 03:36:04 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to logilab common's documentation!
==========================================

Logilab common's is a bunch of modules providing low level functionnalities
shared among some python projects devel by Logilab.

What's this ?
-------------

This package contains some modules used by different Logilab projects.

It is released under the GNU Lesser General Public License.

There is no documentation available yet but the source code should be clean and
well documented.

Designed to ease:

* handling command line options and configuration files
* writing interactive command line tools
* manipulation of files and character strings
* manipulation of common structures such as graph, tree, and pattern such as visitor
* generating text and HTML reports
* more...


Installation
------------

Extract the tarball, jump into the created directory and run ::

    python setup.py install

For installation options, see ::

    python setup.py install --help


Provided modules
----------------

Here is a brief description of the available modules.

Modules providing high-level features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`cache <cache>`, a cache implementation with a least recently used algorithm.

* :ref:`changelog <changelog>`, a tiny library to manipulate our simplified ChangeLog file format.

* :ref:`clcommands <clcommands>`, high-level classes to define command line programs handling
  different subcommands. It is based on `configuration` to get easy command line
  / configuration file handling.

* :ref:`configuration <configuration>`, some classes to handle unified configuration from both
  command line (using optparse) and configuration file (using ConfigParser).

* :ref:`proc <proc>`, interface to Linux /proc.

* :ref:`umessage <umessage>`, unicode email support.

* :ref:`ureports <ureports>`, micro-reports, a way to create simple reports using python objects
  without care of the final formatting. ReST and html formatters are provided.


Modules providing low-level functions and structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`compat <compat>`, provides a transparent compatibility layer between different python
  versions.

* :ref:`date <date>`, a set of date manipulation functions.

* :ref:`daemon <daemon>`, a daemon function and mix-in class to properly start an Unix daemon
  process.

* :ref:`decorators <decorators>`, function decorators such as cached, timed...

* :ref:`deprecation <deprecation>`, decorator, metaclass & all to mark functions / classes as
  deprecated or moved

* :ref:`fileutils <fileutils>`, some file / file path manipulation utilities.

* :ref:`graph <graph>`, graph manipulations functions such as cycle detection, bases for dot
  file generation.

* :ref:`modutils <modutils>`, python module manipulation functions.

* :ref:`shellutils <shellutils>`, some powerful shell like functions to replace shell scripts with
  python scripts.

* :ref:`tasksqueue <tasksqueue>`, a prioritized tasks queue implementation.

* :ref:`textutils <textutils>`, some text manipulation functions (ansi colorization, line wrapping,
  rest support...).

* :ref:`tree <tree>`, base class to represent tree structure, and some others to make it
  works with the visitor implementation (see below).

* :ref:`visitor <visitor>`, a generic visitor pattern implementation.


Modules extending some standard modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`debugger <debugger>`,  `pdb` customization.

* :ref:`logging_ext <logging_ext>`, extensions to `logging` module such as a colorized formatter
  and an easier initialization function.

* :ref:`optik_ext <optik_ext>`, defines some new option types (regexp, csv, color, date, etc.)
  for `optik` / `optparse`


Modules extending some external modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`sphinx_ext <sphinx_ext>`, Sphinx_ plugin defining a `autodocstring` directive.

* :ref:`vcgutils <vcgutils>` , utilities functions to generate file readable with Georg Sander's
  vcg tool (Visualization of Compiler Graphs).


To be deprecated modules
~~~~~~~~~~~~~~~~~~~~~~~~

Those `logilab.common` modules will much probably be deprecated in future
versions:

* `testlib`: use `unittest2`_ instead
* `interface`: use `zope.interface`_ if you really want this
* `table`, `xmlutils`: is that used?
* `sphinxutils`: we won't go that way imo (i == syt)


Comments, support, bug reports
------------------------------

Project page https://www.logilab.org/project/logilab-common

Use the python-projects at lists.logilab.org mailing list.

You can subscribe to this mailing list at
https://lists.logilab.org/mailman/listinfo/python-projects

Archives are available at
https://lists.logilab.org/pipermail/python-projects/


.. _Sphinx: http://sphinx.pocoo.org/
.. _`unittest2`: http://pypi.python.org/pypi/unittest2
.. _`discover`: http://pypi.python.org/pypi/discover
.. _`zope.interface`: http://pypi.python.org/pypi/zope.interface

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* `genindex`
* `modindex`
* `search`
