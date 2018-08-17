def test_students_have_names( a_student ):
    assert isinstance( a_student.name, str )
    assert a_student.name


def test_students_not_in_classroom( a_student ):
    assert isinstance( a_student.classrooms, list )
    assert not a_student.classrooms


def test_students_in_a_classroom( a_student_in_a_classroom ):
    assert isinstance( a_student_in_a_classroom.classrooms, list )
    assert a_student_in_a_classroom.classrooms
    classroom = a_student_in_a_classroom.classrooms[0]
    assert a_student_in_a_classroom in classroom.students


def test_student_can_be_added_to_classrooms( a_classroom, a_student ):
    assert not a_classroom.students
    assert not a_student.classrooms
    a_student.add_classroom( a_classroom )
    assert a_student in a_classroom.students
    assert a_classroom in a_student.classrooms
