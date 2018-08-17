import factory
import random
from faker import Factory as Faker_factory
from quizze import (
    Student as Student_model,
    Classroom as Classroom_model,
    Question as Question_model, Teacher as Teacher_model
)


fake = Faker_factory.create()


class Teacher( factory.Factory ):
    name = factory.lazy_attribute( lambda x: fake.name() )

    class Meta:
        model = Teacher_model


class Student( factory.Factory ):
    name = factory.lazy_attribute( lambda x: fake.name() )

    class Meta:
        model = Student_model


class Classroom( factory.Factory ):
    name = factory.lazy_attribute( lambda x: fake.sentence() )

    class Meta:
        model = Classroom_model


class Question( factory.Factory ):
    question = factory.lazy_attribute( lambda x: fake.sentence() )
    correct_option = factory.lazy_attribute(
        lambda self: random.choice( range( len( self.options ) ) ) )
    options = factory.lazy_attribute(
        lambda x: [ fake.sentence()
                    for i in range( random.randint( 3, 10 ) ) ] )

    class Meta:
        model = Question_model

    @classmethod
    def _build( cls, model_class, *args, **kw ):
        options = kw.pop( 'options' )
        return model_class( *options, **kw )
