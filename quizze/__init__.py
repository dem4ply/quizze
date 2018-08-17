from string import ascii_lowercase


"""
Assumptions:
    * each classroom can have N students
    * each teacher can be assigned to N classroom
    * each quiz can have N amount of questions
    * each question can have N amount of options
    * the students can be in multiple classrooms
    * the students can have N quiz assigned
    * the same students in the same classroom can have different amount
    of quizzes assinged
    * by default when a student has assigned a quiz is assumed
    he not answer any question
    * is assumed all the quizzes assigned are from the same semester
    * a teacher cannot assign a quiz to a student is not in any of his class
    * the grades are number between 0 and 1
"""


class Teacher:
    def __init__( self, name, *classrooms ):
        self.name = name
        self.classrooms = list( classrooms )
        self.quizzes = []

    def create_quiz( self ):
        """
        start a empty quizz
        """
        new_quiz = Quiz()
        self.quizzes.append( new_quiz )
        return new_quiz

    def add_classroom( self, classroom ):
        if classroom not in self.classrooms:
            self.classrooms.append( classroom )
            classroom.assign_teacher( self )

    def assign_quiz_to_student( self, quiz, student, classroom ):
        if quiz not in self.quizzes:
            raise ValueError( "the teacher no own this quiz" )
        if student not in self.all_students:
            raise ValueError(
                "this student is no in any of the classroom of this teacher" )
        if classroom not in self.classrooms:
            raise ValueError( "this teacher no have this classroom" )
        return Assingment( student, quiz, classroom, self )

    def assign_a_quizz_to_classroom( self, quiz, classroom ):
        if quiz not in self.quizzes:
            raise ValueError( "the teacher no own this quiz" )
        if classroom not in self.classrooms:
            raise ValueError( "this teacher no have this classroom" )
        return [
            self.assign_quiz_to_student( quiz, student, classroom )
            for student in classroom.students ]

    def get_grades_by_classroom( self ):
        """
        get a dict with the grades of each classroom the teacher have
        assigned
        """
        return { c: self.get_grade_of_classroom( c ) for c in self.classrooms }

    def get_grade_of_classroom( self, classroom ):
        """
        return a dict with the students be the key and the value the grade
        for the classroom in the parameters
        """
        if classroom not in self.classrooms:
            raise ValueError( "this teacher no have this classroom" )
        results = {}
        for student in classroom.students:
            assigments = list( filter(
                lambda a: a.teacher is self and a.classroom is classroom,
                student.assigments ) )
            results[ student ] = (
                sum( a.grade for a in assigments ) / len( assigments ) )
        return results

    @property
    def all_students( self ):
        """
        get a list with all the students assigned in his class
        """
        return [ s for c in self.classrooms for s in c.students ]


class Student:
    def __init__( self, name, *classrooms ):
        self.name = name
        self.classrooms = list( classrooms )

        for classroom in self.classrooms:
            if self not in classroom.students:
                classroom.students.append( self )

        self.assigments = []

    def add_classroom( self, classroom ):
        if classroom not in self.classrooms:
            self.classrooms.append( classroom )
            classroom.add_student( self )

    def add_assigment( self, assigment ):
        self.assigments.append( assigment )

    @property
    def grade( self ):
        """
        avg of all grades of this student
        """
        return sum( a.grade for a in self.assigments ) / len( self.assigments )

    def __str__( self ):
        return self.name

    def __repr__( self ):
        return "Student( {} )".format( self.name )


class Assingment:
    """
    intermediate object for join student, quiz, teacher, and classroom
    and used for graded a quiz
    """
    def __init__( self, student, quiz, classroom, teacher ):
        self.student = student
        self.quiz = quiz
        self.student.add_assigment( self )
        self.classroom = classroom
        self.teacher = teacher

    @property
    def answers( self ):
        try:
            return self._answers
        except AttributeError:
            self._answers = [ Answer( q ) for q in self.quiz.questions ]
            return self._answers

    @property
    def grade( self ):
        """
        get the grade of this quiz
        """
        return sum( self.answers ) / len( self.answers )


class Classroom:
    def __init__( self, name, *students ):
        self.name = name
        self.students = list( students )
        self.teacher = None

        for student in self.students:
            if self not in student.classrooms:
                student.classrooms.append( self )

    def add_student( self, student ):
        if student not in self.students:
            self.students.append( student )
            student.add_classroom( self )

    def assign_teacher( self, teacher ):
        self.teacher = teacher
        self.teacher.add_classroom( self )

    def __str__( self ):
        return self.name

    def __repr__( self ):
        return "Classroom( {} )".format( self.name )


class Quiz:
    """
    container with all the questions
    """
    def __init__( self, *questions ):
        self.questions = list( questions )

    def add_questions( self, *questions ):
        self.questions += list( questions )


class Question:
    """
    A question in the quiz

    Attributes
    ==========
    question: str
        text of the question
    correct_option: int
        correct position of the correct option
    options: list of strings
        the list of options for a question
    """
    def __init__( self, *options, question, correct_option, ):
        self.question = question
        self.correct_option = int( correct_option )
        self.options = list( options )

        try:
            self.options[ self.correct_option ]
        except IndexError as e:
            raise IndexError(
                "the correct option is out range with the options" )

    def __str__( self ):
        options = (
            "{letter}) {option}".format( letter=letter, option=option )
            for letter, option in zip( ascii_lowercase, self.options ) )
        return "{question}\n{options}".format(
            question=self.question, options="\n".join( options ) )

    def check_is_the_correct_option( self, option ):
        return option == self.correct_option


class Answer:
    """
    Answer of a question of one quiz

    the object can be cast in bool and int

    Attributes
    ==========
    question: py:class:`~.Question`
        questions is answer
    option: int
        option answer for the question
    """
    def __init__( self, question, option=None ):
        self.question = question
        self.option = option
        self.was_correct = self.question.check_is_the_correct_option(
            self.option )

    @property
    def option( self ):
        return self._option

    @option.setter
    def option( self, value ):
        self._option = value
        self.was_correct = self.question.check_is_the_correct_option(
            self.option )

    def __bool__( self ):
        return self.was_correct

    def __radd__( self, other ):
        if isinstance( other, Answer ):
            return int( self ) + int( other )
        else:
            return int( self ) + other

    def __int__( self ):
        return int( bool( self ) )
