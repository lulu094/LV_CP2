#LV 1st Gradebook
class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


    def get_all_averages(self):
        return [s.calculate_average() for s in self.students]

    def class_average(self):
        avgs = self.get_all_averages()
        return sum(avgs) / len(avgs) if avgs else 0

    def highest_average(self):
        avgs = self.get_all_averages()
        return max(avgs) if avgs else 0

    def lowest_average(self):
        avgs = self.get_all_averages()
        return min(avgs) if avgs else 0