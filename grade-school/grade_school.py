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
        self._roster.setdefault(grade, [])
        self._roster[grade].append(name)
        self._roster[grade].sort()

    def roster(self):
        """
        Get a sorted list of all students in all grades.
        Grades should sort as 1, 2, 3, etc., and students
        within a grade should be sorted alphabetically by name.
        :return:
        """
        return [name
                for grade in sorted(list(self._roster.keys()))
                for name in self._roster[grade]]

    def grade(self, grade_number):
        """
        Get a list of all students enrolled in a grade
        :param grade_number:
        :return:
        """

        # If you find yourself looking to see if
        # something is in a dict,
        # and if not, giving it a default value,
        # consider using dict.get(key, default)
        return self._roster.get(grade_number, []).copy()
