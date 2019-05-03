import os, sys
USER = None
PWD = None

PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
path = os.path.join(PATH, 'db')

STUDENT_LIST = os.path.join(path, 'student_list.txt')
STUDENT_LIST1 = os.path.join(path, 'student_list1.txt')

COURSE_LIST = os.path.join(path, 'course_list.txt')

SELECT_INFO = os.path.join(path, 'select_info.txt')
SELECT_INFO1 = os.path.join(path, 'select_info1.txt')

LOG_NAME = os.path.join(os.path.join(PATH, 'log'), 'log.log')
