import pytest
from faker import Factory as Faker_factory
from quizze import Answer

fake = Faker_factory.create()


@pytest.fixture
def correct_answer( a_question ):
    return Answer( a_question, a_question.correct_option )


@pytest.fixture
def incorrect_answer( a_question ):
    return Answer( a_question, a_question.correct_option - 1 )


@pytest.fixture
def unanswered_answer( a_question ):
    return Answer( a_question, None )


def test_correct_answer_should_be_true( correct_answer ):
    assert correct_answer


def test_incorrect_answer_should_be_false( incorrect_answer ):
    assert not incorrect_answer


def test_unanswered_answer_should_be_false( unanswered_answer ):
    assert not unanswered_answer
