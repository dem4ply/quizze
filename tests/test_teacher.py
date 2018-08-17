import pytest
from faker import Factory as Faker_factory
from quizze import Quiz, Assingment

fake = Faker_factory.create()


@pytest.fixture
def a_quiz( a_teacher, a_question ):
    quiz = a_teacher.create_quiz()
    quiz.add_questions( a_question )
    return quiz


def test_teachers_have_names( a_teacher ):
    assert isinstance( a_teacher.name, str )
    assert a_teacher.name


def test_teachers_can_create_a_quizz( a_teacher ):
    new_quiz = a_teacher.create_quiz()
    assert isinstance( new_quiz, Quiz )


def test_teachers_start_without_quizzes( a_teacher ):
    assert not a_teacher.quizzes


def test_teacher_when_assign_a_quiz_should_return_a_assigment_object(
        a_teacher, a_student, a_classroom, a_quiz ):

    a_teacher.add_classroom( a_classroom )
    a_classroom.add_student( a_student )
    assigment = a_teacher.assign_quiz_to_student(
        a_quiz, a_student, a_classroom )

    assert isinstance( assigment, Assingment )


def test_teacher_assign_a_quiz_outside_to_their_classroom_should_do_a_raise(
        a_teacher, a_student, a_quiz, a_classroom ):
    with pytest.raises( ValueError ) as e:
        a_teacher.assign_quiz_to_student( a_quiz, a_student, a_classroom )

    assert str( e.value ) == (
        "this student is no in any of the classroom of this teacher" )


def test_teacher_when_assign_a_quiz_he_no_own(
        a_teacher, a_classroom, a_student, a_question ):
    quiz = Quiz( a_question )

    with pytest.raises( ValueError ) as e:
        a_teacher.assign_quiz_to_student( quiz, a_student, a_classroom )

    assert str( e.value ) == "the teacher no own this quiz"
