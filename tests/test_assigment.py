import pytest


@pytest.fixture
def a_assigment( a_teacher, a_student, a_classroom, a_question ):
    a_teacher.add_classroom( a_classroom )
    a_classroom.add_student( a_student )
    quiz = a_teacher.create_quiz()
    quiz.add_questions( a_question )
    return a_teacher.assign_quiz_to_student( quiz, a_student, a_classroom )


@pytest.fixture
def a_assigment_with_all_correct_answers( a_assigment ):
    for answer in a_assigment.answers:
        answer.option = answer.question.correct_option
    return a_assigment


def test_assigment_by_default_should_have_all_the_answer_in_none(
        a_assigment ):
    answers = a_assigment.answers
    assert isinstance( answers, list )
    assert all( a.option is None for a in answers )


def test_assigment_can_be_graded( a_assigment ):
    assert a_assigment.grade == 0.0


def test_assigment_all_correct_answers_the_grade_should_be_1(
        a_assigment_with_all_correct_answers ):
    assert a_assigment_with_all_correct_answers.grade == 1.0
