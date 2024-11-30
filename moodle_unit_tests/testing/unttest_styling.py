import unittest

class MarkdownTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.results.append(f"- ✅ **{test.id()}** - Passed")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.results.append(f"- ❌ **{test.id()}** - Failed\n  ```\n  {self._exc_info_to_string(err, test)}\n  ```")

    def addError(self, test, err):
        super().addError(test, err)
        self.results.append(f"- ⚠️ **{test.id()}** - Error\n  ```\n  {self._exc_info_to_string(err, test)}\n  ```")



