import pytest
from .factories import (
    Classroom as Classroom_factory,
    Student as Student_factory,
    Question as Question_factory,
)


@pytest.fixture
def a_classroom_with_students():
    classroom = Classroom_factory.build()
    students = Student_factory.build_batch( size=10 )
    for student in students:
        classroom.add_student( student )
    return classroom


def test_classroom_have_a_name( a_classroom ):
    assert isinstance( a_classroom.name, str )
    assert a_classroom.name


def test_classroom_should_no_have_students( a_classroom ):
    assert not a_classroom.students


def test_classroom_when_assing_a_student_should( a_classroom_with_a_student ):
    assert a_classroom_with_a_student.students
    student = a_classroom_with_a_student.students[0]
    assert a_classroom_with_a_student in student.classrooms


def test_classroom_can_add_students( a_classroom, a_student ):
    assert not a_classroom.students
    assert not a_student.classrooms
    a_classroom.add_student( a_student )
    assert a_student in a_classroom.students
    assert a_classroom in a_student.classrooms


def test_classroom_can_get_grade_of_the_classroom(
        a_teacher, a_classroom_with_students, a_list_of_questions ):
    classroom = a_classroom_with_students
    assert classroom.students
    a_teacher.add_classroom( classroom )
    quiz = a_teacher.create_quiz()
    quiz.add_questions( *a_list_of_questions )
    a_teacher.assign_a_quizz_to_classroom( quiz, classroom )
    grades = a_teacher.get_grades_by_classroom()
    assert classroom in grades
    for student in classroom.students:
        assert student in grades[ classroom ]
        assert grades[ classroom ][ student ] == 0.0


def test_classroom_when_have_multiple_teacher_should_no_mix_grades(
        a_list_of_teachers, a_classroom_with_students, a_list_of_questions ):
    classroom = a_classroom_with_students
    assert classroom.students
    # for each teacher is going to assign one quizz to the classroom
    for teacher in a_list_of_teachers:
        teacher.add_classroom( classroom )
        quiz = teacher.create_quiz()
        quiz.add_questions( *Question_factory.build_batch( size=10 ) )
        assigments = teacher.assign_a_quizz_to_classroom( quiz, classroom )

    # this is only going to make the students of the last teacher
    # have all the correct answer
    for assigment in assigments:
        for answer in assigment.answers:
            answer.option = answer.question.correct_option

    # the grades of all the teachers except the last one
    # should be 0
    for teacher in a_list_of_teachers[:-1]:
        grades = teacher.get_grades_by_classroom()
        assert classroom in grades
        for student in classroom.students:
            assert student in grades[ classroom ]
            assert grades[ classroom ][ student ] == 0.0

    # the grades of the last teacher should be 1
    for teacher in a_list_of_teachers[-1:]:
        grades = teacher.get_grades_by_classroom()
        assert classroom in grades
        for student in classroom.students:
            assert student in grades[ classroom ]
            assert grades[ classroom ][ student ] == 1.0
