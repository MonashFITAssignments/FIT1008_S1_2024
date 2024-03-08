"""Running tests"""
from __future__ import print_function

import sys
import json
import inspect

from unittest import result
from unittest.signals import registerResult
import ed_utils.decorators as decorators

DECORATOR_CLASSES = [
    klass for _name, klass in inspect.getmembers(decorators)
    if (
        inspect.isclass(klass)
        and issubclass(klass, decorators.Decorator)
        and klass != decorators.Decorator
    )
]


class JSONTestResult(result.TestResult):
    """A test result class that can print formatted text results to a stream.

    Used by JSONTestRunner.
    """
    def __init__(self, stream, descriptions, verbosity, results):
        super(JSONTestResult, self).__init__(stream, descriptions, verbosity)
        self.descriptions = descriptions
        self.results = results

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return doc_first_line
        else:
            return str(test)

    def getOutput(self):
        if self.buffer:
            out = self._stdout_buffer.getvalue()
            err = self._stderr_buffer.getvalue()
            if err:
                if not out.endswith('\n'):
                    out += '\n'
                out += err
            return out

    def buildResult(self, test, err=None):
        output = self.getOutput() or ""
        result = {
            "name": self.getDescription(test),
            "ok": True,
        }
        for dec in DECORATOR_CLASSES:
            method = getattr(test, test._testMethodName)
            val = getattr(method, dec.get_attr_name(), None)
            dec.change_result(val, result, output, err)
        return result

    def processResult(self, test, err=None):
        self.results.append(self.buildResult(test, err))

    def addSuccess(self, test):
        super(JSONTestResult, self).addSuccess(test)
        self.processResult(test)

    def addError(self, test, err):
        super(JSONTestResult, self).addError(test, err)
        # Prevent output from being printed to stdout on failure
        self._mirrorOutput = False
        self.processResult(test, err)

    def addFailure(self, test, err):
        super(JSONTestResult, self).addFailure(test, err)
        self._mirrorOutput = False
        self.processResult(test, err)


class JSONTestRunner(object):
    """A test runner class that displays results in JSON form.
    """
    resultclass = JSONTestResult

    def __init__(self, stream=sys.stdout, descriptions=True, verbosity=1,
                 failfast=False, buffer=True,
                 stdout_visibility=None):
        """
        Set buffer to True to include test output in JSON
        """
        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer
        self.json_data = {
            "testcases": [],
        }
        if stdout_visibility:
            self.json_data["stdout_visibility"] = stdout_visibility

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity,
                                self.json_data["testcases"])

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()

        json.dump(self.json_data, self.stream, indent=4)
        self.stream.write('\n')
        return result
