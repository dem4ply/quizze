import pytest
import random
from faker import Factory as Faker_factory
from .factories import (
    Teacher as Teacher_factory,
    Student as Student_factory,
    Classroom as Classroom_factory,
    Question as Question_factory,
)


fake = Faker_factory.create()


@pytest.fixture
def a_teacher():
    return Teacher_factory.build()


@pytest.fixture
def a_list_of_teachers():
    return Teacher_factory.build_batch( size=5 )


@pytest.fixture
def a_student():
    return Student_factory.build()


@pytest.fixture
def a_student_in_a_classroom( a_student, a_classroom ):
    a_student.add_classroom( a_classroom )
    return a_student


@pytest.fixture
def a_classroom():
    return Classroom_factory.build()


@pytest.fixture
def a_classroom_with_a_student( a_classroom, a_student ):
    a_classroom.add_student( a_student )
    return a_classroom


@pytest.fixture
def list_of_options():
    return [ fake.sentence() for i in range( random.randint( 3, 10 ) ) ]


@pytest.fixture
def a_question( list_of_options ):
    return Question_factory.build()


@pytest.fixture
def a_list_of_questions():
    return Question_factory.build_batch( size=10 )
