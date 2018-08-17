import math
from quizze import Student, Classroom, Question, Teacher


def test_school():
    teacher = Teacher( name='Dr. Gregory House' )

    student_1 = Student( name='Caring Student' )
    student_2 = Student( name='Rebellious Student' )
    student_3 = Student( name='Keen Student' )

    classroom = Classroom( 'tree stories', student_1, student_2, student_3 )
    teacher.add_classroom( classroom )

    q_1 = Question(
        'Injury to the head', 'Broken bones', 'Bleeding, blood loss',
        correct_option=2, question='What is the definition of Hemorrhage?' )
    q_2 = Question(
        'A+', 'B-', 'LOL', correct_option=2,
        question='Which one below is not a blood type?' )
    q_3 = Question(
        'The lung', 'The Liver', 'The heart', correct_option=1,
        question='When someone has Hepatitis, which organ is affected?' )

    quiz = teacher.create_quiz()
    quiz.add_questions( q_1, q_2, q_3 )
    teacher.assign_a_quizz_to_classroom( quiz, classroom )

    student_2.assigments[0].answers[0].option = 2
    student_2.assigments[0].answers[1].option = 1

    student_3.assigments[0].answers[0].option = 2
    student_3.assigments[0].answers[1].option = 2
    student_3.assigments[0].answers[2].option = 1

    grades = teacher.get_grade_of_classroom( classroom )

    assert grades[ student_1 ] == 0
    assert math.isclose( grades[ student_2 ], 0.33, rel_tol=0.01 )
    assert grades[ student_3 ] == 1
