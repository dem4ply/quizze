import pytest
import math
from .factories import Question as Question_factory


@pytest.fixture
def a_student_with_assigments(
        a_student, a_teacher, a_classroom ):
    a_teacher.add_classroom( a_classroom )
    a_classroom.add_student( a_student )
    for i in range( 3 ):
        quiz = a_teacher.create_quiz()
        quiz.add_questions( *Question_factory.build_batch( 10 ) )
        a_teacher.assign_quiz_to_student( quiz, a_student, a_classroom )

    return a_student


def test_student_when_all_answer_of_one_signature_the_grade_should_be_a_third(
        a_student_with_assigments ):
    student = a_student_with_assigments
    assigment = student.assigments[0]
    assert student.grade == 0.0
    for answer in assigment.answers:
        choice = answer.question.correct_option
        answer.option = choice
    assert math.isclose( student.grade, 0.3, rel_tol=0.1 )
