==============================================
Object Oriented Design Implementation Exercise
==============================================

Please use your most proficient programming language to create object oriented design and
use test driven development to implement classes and methods with appropriate data structure
and test the code for the following scenario.

Please add comments describing any assumptions you make:
There are Teachers
There are Students
Students are in classes that teachers teach
Teachers can create multiple quizzes with many questions (each question is multiple choice)
Teachers can assign quizzes to students
Students solve/answer questions to complete the quiz, but they don't have to complete it at
once. (Partial submissions can be made).
Quizzes need to get graded
For each teacher, they can calculate each student's total grade accumulated over a semester
for their classes


================
install and test
================

.. code-block:: shell

	git clone https://github.com/dem4ply/quizze.git
	cd quizze
	virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt
	pip install -e ./
	make test
	make style_test
