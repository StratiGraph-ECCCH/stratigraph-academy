# The backbone, from trench to cloud

Eight steps, each one a tool, and the same thing travelling between them: the graph. This
is the shape StratiGraph was presented with at ArcheoVirtual in Paestum on 29 October
2026, and it is the shape the Academy teaches. Nobody uses all eight on the same day; the
point is that each one hands on what the next one needs, without anybody exporting,
converting or re-typing.

**1 · The field node.** A node that travels with the team, or an institutional one that
stays. It holds the rooms where studies live, and it works in a trench with no network —
the field one is often a small computer in a box.
→ the manual of StratiGraph Server

**2 · StratiField.** The field assistant, on a tablet or a laptop on site: stratigraphic
units, photographs and observations, recorded by voice or by hand and signed with the iD
of whoever spoke.
→ the manual of StratiField

**3 · The recording forms.** The sheets a national tradition requires, and the controlled
vocabularies behind their fields, mapped onto CIDOC-CRM so that two excavations that never
met still use the same words.
→ stratigraph-templates

**4 · Aïoli.** Annotation on the 3D surface itself: what you see on the stones, written on
the stones, and brought back as evidence into the study.

**5 · EMStudio.** Where the graph is drawn, read and argued: units, relations, epochs, and
the reconstruction's claims with the sources that hold them up.
→ the manual of EMStudio

**6 · Heriverse.** Where a reconstruction becomes something a visitor can walk through,
with the graph still underneath it.

**7 · The catalogue.** What a node publishes of itself to whoever is allowed to look:
studies, resources, and the words they use.
→ the manual of StratiGraph Server

**8 · The ECCCH.** The European collaborative cloud: a federated node, where a study joins
the common space of European heritage.

## What runs inside a node

A node is not one program but a small household of services, and on most days nobody needs
to know their names. It keeps a **graph store** for the relations, a **database** for the
documents and their revisions, an **object store** for the files a study brings with it, an
**identity service** that knows who signed what, and an **image service** that serves
photographs at the size a screen asks for — in the IIIF way, so that another institution's
viewer can show them without making a copy. Over all of them sits the node's own interface:
one address, one set of doors.

Which of these services the house provides and which the node brings with it is the first
decision of an installation, and it is taken value by value: the deployment page of the node
manual lists what a node refuses to start without, and what it will run itself if nobody
offers it.

## Specialised tools that join a step

Some work needs a tool that does one thing well. The ecosystem calls it where that thing
happens, rather than growing a weaker copy of it inside.

**The point cloud toolbox (FBK)** turns what a survey measured into the proxies a graph can
talk about: the shapes that stand for a unit when the unit is a volume rather than a line on
a plan. It belongs beside step 4, where a measurement becomes something a study can refer
to.

**The models for voice and language (ARC)** are what «recorded by voice» means in step 2:
speech turned into text on the device itself, and a language model small enough to run in a
box in a trench — so that a sentence said with both hands busy arrives in the record as a
unit, and not as a note to type up in the evening.

**The web interface of the graph** is where a published study can be questioned rather than
only read: the same relations, reached with a query instead of a page, for whoever asks
something the manuals did not foresee.

## Two circles around the backbone

The first circle is made of the tools the consortium brings, which are developed alongside
the node and speak the graph natively. On the desktop they are **EM Tools**, the Blender
add-on where a reconstruction is modelled against the units it represents; **Tropy**
(UniLu), where the photographs of an archive become described, searchable material; and
**pyArchInit** (AdArte), the QGIS environment many Italian excavations already record in.
**Aïoli** (CNRS) and the point cloud toolbox (FBK) belong to this circle too, each at its
step.

The second circle is everything an excavation already uses and will keep using: other
recording systems, photogrammetry suites, GIS, archives with their own catalogues, open and
proprietary alike. They plug in rather than being replaced — the ecosystem asks them for
what they are good at, and keeps the interpretation in the graph.

What travels between the steps, in both circles, is never a file format anybody has to care
about. It is the study: the units, the relations between them, the sources, and who said
what and when. That is the reason a reading survives the tool it was made in — and the
reason this is worth learning once rather than eight times.

## The five working phases

Over these eight steps lie the five working phases of an investigation, 0 to 4, which are
how the Academy's path is organised: a phase is a module to pass, and it borrows the
competence nodes it needs. The mapping between the phases and the steps comes from the
drawings used in teaching, and is being written with them rather than invented here:
[a day, in eight pictures](a-day-in-eight-pictures.md) shows the same cycle from the side
of the work, and says which phase each moment belongs to.
