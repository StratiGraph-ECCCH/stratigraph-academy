StratiGraph Manual
==================

The manual of the `StratiGraph <https://github.com/StratiGraph-ECCCH>`_ ecosystem: written
for the person who uses the tools, not for the machine that talks to them.

It is the front door — what StratiGraph is and the map of the tools — and it holds, in its
own body, the manual of **the node and StratiField**, because for whoever works those two
are one thing: the room where the graph lives and the tool that fills it from a trench.

Until 19 November 2026 this repository was called ``stratigraph-server-doc``. The old name
still redirects; the scope is wider now, and the name says so.

What is deliberately elsewhere
------------------------------

**EMStudio** and **EM Tools** keep their manuals in their own repositories: they are
Extended Matrix tools with their own identity, and two identities is a choice, not an
oversight.

**Courses** belong to the StratiGraph Academy (promised in the project's own Grant
Agreement, and covering the whole toolset, partners' tools included); the **Extended
Matrix method** is taught by EM Academy.

The datamodel is owned by `s3Dgraphy <https://github.com/ExtendedMatrix/s3Dgraphy>`_.

Each sentence lives in one place. This manual cites the others; it does not copy them.

Building locally
----------------

.. code-block:: bash

   python3 -m venv .venv && .venv/bin/pip install -r docs/requirements.txt
   .venv/bin/python -m sphinx -W docs docs/_build

The documentation is built with `Sphinx <https://www.sphinx-doc.org/>`_ and hosted on
`Read the Docs <https://readthedocs.org/>`_.
