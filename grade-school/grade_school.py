class School:
    """
    The roster for the school.

    Contains given students' names along
    with the grade that they are in.

    Note that all our students only have
    one name.
    """

    def __init__(self):
        self._roster = dict()

    def add_student(self, name, grade):
        """
        Add a student's name to the roster for a grade
        :param name:
        :param grade:
        :return:
        """

        if grade in self._roster:
            self._roster[grade].append(name)
            self._roster[grade] = sorted(self._roster[grade])
        else:
            self._roster[grade] = [name]

    def roster(self):
        """
        Get a sorted list of all students in all grades.
        Grades should sort as 1, 2, 3, etc., and students
        within a grade should be sorted alphabetically by name.
        :return:
        """
        grades = sorted(list(self._roster.keys()))
        names = list()
        
        for grade in grades:
            for name in self._roster[grade]:
                names.append(name)
        
        return names

    def grade(self, grade_number):
        """
        Get a list of all students enrolled in a grade
        :param grade_number:
        :return:
        """
        return self._roster.get(grade_number, []).copy()
