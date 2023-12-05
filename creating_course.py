

class QExcept(Exception):
    def __init__(self, m):
        super().__init__(m)


class Course:

    COURSE_NAME_LEN = 3
    MAX_COURSE_NUM = 499
    MIN_COURSE_NUM = 100
    MAX_CREDIT = 6
    MIN_CREDIT = 0

    def __init__(self, name, num, credit):
        if not len(name) == Course.COURSE_NAME_LEN:
            raise QExcept('Course name must be {:d} characters'.format(Course.COURSE_NAME_LEN))

        if not (Course.MIN_COURSE_NUM < num < Course.MAX_COURSE_NUM):
            raise QExcept('Course number must be between {:d} and {:d}'.format(Course.MIN_COURSE_NUM, Course.MAX_COURSE_NUM))

        if not (Course.MIN_CREDIT < credit < Course.MAX_CREDIT):
            raise QExcept('Credits must be between {:d} and {:d}'.format(Course.MIN_CREDIT, Course.MAX_CREDIT))

        self.name = name
        self.num = num
        self.credit = credit

    def __str__(self):
        return 'Name: {:s}\nNUM: {:d}\nCredit: {:d}'.format(self.name, self.num, self.credit)


course_list = []
NUMBER_OF_COURSE = 2

while True:
    try:
        name = input('Course Name:')
        num = int(input('ID NUM:'))
        credit = int(input('Credit:'))

        course = Course(name, num, credit)
        course_list.append(course)

    except QExcept as error:
        print('Error:', error)

    if len(course_list) == NUMBER_OF_COURSE:
        break

for x in course_list:
    print('\n')
    print(x)
