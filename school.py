class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
    def add_student(self, student_name, grade_level):
        if grade_level in self.roster:
            self.roster[grade_level].append(student_name)
        else:
            self.roster[grade_level] = [student_name]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        new_dict = self.roster
        for key in self.roster:
            new_dict[key].sort()
        return new_dict