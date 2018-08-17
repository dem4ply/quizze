import pytest
from faker import Factory as Faker_factory
from quizze import Question

fake = Faker_factory.create()


def test_quiz_should_have_question( a_question ):
    assert isinstance( a_question.question, str )
    assert a_question.question


def test_quiz_should_have_options( a_question ):
    assert isinstance( a_question.options, list )
    assert a_question.options


def test_quiz_when_the_correct_answer_is_out_range_should_raise_a_index_error(
        list_of_options ):
    with pytest.raises( IndexError ):
        Question(
            *list_of_options, question=fake.sentence(), correct_option=100, )
