Proceedings
===========

You can create the proceedings as follows:

    $ git clone https://github.com/cloudmesh-community/proceedings-fa18.git
    $ cd proceedings-fa18

First, you have to clone and update all directories. This can be done with

    $ make update

If you ever want to update the content again, simply repeat the command

We have two proceedings, one for papers, and one for projects. To create them you need to create them separately.

Paper Proceedings
-----------------

Do the following

    $ make bib-papers
    $ make papers

The proceedings will be in a file called

Project Proceedings
-------------------

Do the following

    $ make bib-papers
    $ make papers

The proceedings will be in a file called

Create both proceedings
-----------------------

Do the following

    $ make all
