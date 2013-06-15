Kaylee Demo Projects
====================
Kaylee is a Python and JavaScript framework for developing in-browser
distributed and volunteer computing applications that allows programmers
to concentrate on business logic by leaving all the computational nodes
handling to Kaylee.

You can find all the information about Kaylee by these links:

* http://kaylee.znasibov.info
* https://github.com/basicwolf/kaylee


Running
-------
Install Kaylee, clone the demo projects repository and run ``demo.sh``.
This compiles all the available demo projects and creates Kaylee demo
environment and launches the demo with the tutorial application.


Demo projects
-------------

Monte-Carlo PI
..............
The *Monte-Carlo PI* is a project described in the documentation's Tutorial
section. It is an implementation of a PI calculation via a distributed
series of Monte-Carlo experiments.

Hash Cracker
............
The *Hash Cracker* is an implementation of distributed cracking of a
MD5-hash, which was obtained from a "salted" password. In the given
demo scenario, the hash salt is known, and the nodes are looking for a
correct password only.

Human OCR
.........
The *Human Optical Character Recognition (OCR)* is a simple implementation
of the reCAPTCHA (http://recaptcha.net). The project demonstrates a problem
which can be solved by distributing the images-to-be-recognized to various
end users.
