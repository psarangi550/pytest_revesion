class TestCheck:
    def test_check(self):
        self.x = 10
        assert self.x.__class__.__name__ == "int"
