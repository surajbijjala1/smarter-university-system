import unittest
from datetime import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Adjust the file name as necessary; here 'quizzes_test.json' is used for clarity
        self.ctrl = QuizzesController('quizzes_test.json')
        
    def test_expose_failure_01(self):
        """
        Tests adding a quiz with None as the title to induce a TypeError. This test
        checks the robustness of the `add_quiz` method in handling None inputs for the quiz title.
        """
        current_date = datetime.now()
        deadline_date = current_date 
        self.ctrl.add_quiz(None, "Sample Text", current_date, deadline_date)
        '''
        Crash info:
        Traceback (most recent call last):
        File "/home/rohith/smarter-university-system/test/quizzes_test.py", line 18, in test_expose_failure_01
        self.ctrl.add_quiz(None, "Sample Text", current_date, deadline_date)
        File "/home/rohith/smarter-university-system/./app/controllers/quizzes_controller.py", line 63, in add_quiz
        quiz_id = utils.generate_id(title + updated_date.isoformat())
        TypeError: unsupported operand type(s) for +: 'NoneType' and 'str
        '''

    def test_expose_failure_02(self):
        """
        A test that induces a crash by attempting to retrieve a quiz with a corrupted
        (NoneType) data list. This simulates data corruption leading to a system failure.
        """
        self.ctrl.clear_data()  # Ensure there is no residual data that could affect the test
        self.ctrl.quizzes = None  # Simulate data corruption

        self.ctrl.get_quiz_by_id("sdvfc441e5c41d4c41")
        '''
        Crash info:
        Traceback (most recent call last):
        File "/home/rohith/smarter-university-system/test/quizzes_test.py", line 37, in test_expose_failure_02
        self.ctrl.get_quiz_by_id("sdvfc441e5c41d4c41")
        File "/home/rohith/smarter-university-system/./app/controllers/quizzes_controller.py", line 117, in get_quiz_by_id
        quizzes = [q for q in self.quizzes if q.id == quiz_id]
        TypeError: 'NoneType' object is not iterable
        '''

    def test_expose_failure_03(self):
        """
        This test induces a crash due to providing a None as the file name for initializing
        the QuizzesController, which should handle file path errors gracefully.
        """
        fileName=None
        self.ctrl = QuizzesController(fileName)
        self.ctrl.clear_data()
        current_date = datetime.now()
        deadline_date = current_date
        self.ctrl.add_quiz("q2", 'test', current_date, deadline_date)
        '''
        Crash info:
        "Traceback (most recent call last):
        File "/home/rohith/smarter-university-system/test/quizzes_test.py", line 51, in test_expose_failure_03
        self.ctrl = QuizzesController(fileName)
        File "/home/rohith/smarter-university-system/./app/controllers/quizzes_controller.py", line 19, in __init__
        self.quizzes:List[Quiz] = self._load_data()
        File "/home/rohith/smarter-university-system/./app/controllers/quizzes_controller.py", line 27, in _load_data
        for qobj in load_data(self.file_name):
        File "/home/rohith/smarter-university-system/./app/utils/data_loader.py", line 9, in load_data
        fpath = os.path.join('data',file_name)
        File "/usr/lib/python3.10/posixpath.py", line 90, in join
        genericpath._check_arg_types('join', a, *p)
        File "/usr/lib/python3.10/genericpath.py", line 152, in _check_arg_types
        raise TypeError(f'{funcname}() argument must be str, bytes, or '
        TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'
        '''

if __name__ == '__main__':
    unittest.main()
