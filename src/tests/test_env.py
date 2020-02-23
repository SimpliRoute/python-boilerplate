from settings import SOME_EXAMPLE_ENV_VAR
import unittest


class TestEnv(unittest.TestCase):
    def test_env_var_available(self):
        self.assertEqual(SOME_EXAMPLE_ENV_VAR, "something")


if __name__ == "__main__":
    unittest.main()
