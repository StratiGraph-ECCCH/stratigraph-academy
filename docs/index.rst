The StratiGraph manual
======================

StratiGraph is a set of tools for reading, recording and arguing archaeological
stratigraphy, and for keeping that reading alive as a graph other people and other
machines can use.

This manual is written for the person who uses those tools: an archaeologist at the edge
of a trench, a researcher who opens a room on a node, a colleague invited to read someone
else's study. It explains **how things work**.

At its centre is the node and the field — **StratiGraph Server** and **StratiField** —
because for whoever works those two are one thing: the room where the graph lives, and the
tool that fills it from a trench. A room has two doors: the live socket, for whoever stays
inside and wants every change as it happens, and the REST door, for whoever comes in,
reads, writes and leaves — a phone in the trench, a script, a partner's platform.

.. note::
   This manual is being written. Working in a room, the field node, people, profiles and
   roles, the REST door of a room and the API reference are here; the guide for client
   developers follows.

   StratiGraph is a Horizon Europe project, *StratiGraph — Knowledge Graphs for
   Stratigraphy* (2025–2029).

What is deliberately elsewhere
------------------------------

**EMStudio** and **EM Tools** keep their own manuals, in their own repositories: they are
Extended Matrix tools, with their own identity, and flattening them under StratiGraph
would say something untrue about what they are.

**Courses** belong to the StratiGraph Academy, which covers the whole toolset, partners'
tools included; the **Extended Matrix method** is taught by EM Academy. This manual cites
them and never copies them: a sentence lives in one place only. The last page says where
each thing is.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   introduction
   ecosystem/map
   room-guide
   dev-node
   field-node
   roles-and-users
   rest-api
   api-reference
   elsewhere
