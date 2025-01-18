import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_1 = runner.Runner('1')
        for i in range(10):
            walk_1.walk()
        self.assertEqual(walk_1.distance, 50)

    def test_run(self):
        run_1 = runner.Runner("run1")
        for i in range(10):
            run_1.run()
        self.assertEqual(run_1.distance,100)

    def test_chalange(self):
        walk_2 = runner.Runner("walk2")
        run_2 = runner.Runner("run2")
        for i in range(10):
            walk_2.walk()
            run_2.run()
        self.assertNotEqual(run_2.distance,walk_2.distance)



