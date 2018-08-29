import pytest

class Testclass:
    def test_one(self):
        x="this"
        assert 'h' in x

    def test_two(self):
        x="hello"
        assert hasattr(x,'check')

    def test_three(self):
        x="hello"
        assert 'h' in x

if __name__ == '__main__':
    pytest.main('-q test_class.py')