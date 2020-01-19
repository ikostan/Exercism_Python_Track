STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANTS_CONVERTER = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets',
}


class Garden:
    """
    Given a diagram, determine which plants each child
    in the kindergarten class is responsible for.

    They've chosen to grow:
     - grass: G
     - clover: C
     - radishes: R
     - violets: V

    There are 12 children in the class:
        Alice, Bob, Charlie, David,
        Eve, Fred, Ginny, Harriet,
        Ileana, Joseph, Kincaid, and Larry.

    Each child gets 4 cups, two on each row. Their teacher assigns
    cups to the children alphabetically by their names.
    """

    _plants_per_student = 2

    def __init__(self, diagram: str, students=None):
        if students is None:
            self._students = STUDENTS
        else:
            self._students = sorted(students)

        self._diagram = diagram.split()

    def plants(self, name: str) -> list:
        """
        Determine which plants belong to each student
        """
        plants = list()

        start_index = self._students.index(name) * self._plants_per_student

        # first row
        for char in self._diagram[0][start_index:start_index + self._plants_per_student]:
            plants.append(PLANTS_CONVERTER[char])

        # second row
        for char in self._diagram[1][start_index:start_index + self._plants_per_student]:
            plants.append(PLANTS_CONVERTER[char])

        return plants
