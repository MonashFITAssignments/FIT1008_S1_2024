import abc


class InvalidValueException(Exception):
    pass


class Decorator(abc.ABC):

    def __init__(self, v) -> None:
        res = self.validate(v)
        if res:
            raise InvalidValueException(res)
        self.v = v

    def validate(self, v):
        return None

    def __call__(self, func):
        setattr(func, self.get_attr_name(), self.v)
        return func

    @classmethod
    def get_attr_name(cls):
        return f"__{cls.__name__}__"

    @classmethod
    @abc.abstractmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        """
        Apply your change to the test.
        This method is called *regardless* of whether you applied the decorator or not.

        If you did not apply the decorator, saved_value will be none.
        """
        pass


class weight(Decorator):
    def validate(self, v):
        if not isinstance(v, (float, int)):
            return "Weight should be a float/int."
        if v < 0:
            return "Weight should be non-negative."

    @classmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        """
        Handles the `score`, `passed` fields for results.
        """
        if saved_value is None:
            saved_value = 1
        failed = err is not None
        if failed:
            results["score"] = 0
        else:
            results["score"] = saved_value
        results["passed"] = not failed


class number(Decorator):

    @classmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        if saved_value is not None:
            results["name"] = "{}: {}".format(str(saved_value), results["name"])


class visibility(Decorator):
    VISIBILITY_SHOW = "visible"
    VISIBILITY_HIDDEN = "hidden"
    VISIBILITY_PRIVATE = "private"
    VALID_CHOICES = [
        VISIBILITY_SHOW,
        VISIBILITY_HIDDEN,
        VISIBILITY_PRIVATE,
    ]
    def validate(self, v):
        if v not in self.VALID_CHOICES:
            return "Visibility given is not a valid selection."

    @classmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        """
        Handles the `hidden` and `private` fields for results.
        """
        if saved_value is None:
            saved_value = cls.VISIBILITY_SHOW
        results["hidden"] = saved_value == cls.VISIBILITY_HIDDEN
        results["private"] = saved_value == cls.VISIBILITY_PRIVATE


class hide_errors(Decorator):
    """
    By default, the assertion failing the test will be shown.
    To override this, use this decorator.

    Usage: @hide_errors("Error message to be shown upon test failure")
    """

    @classmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        """
        Handles the `feedback` field for results.
        """
        failed = err is not None
        if failed:
            addition = ""
            if output:
                if not output.endswith("\n\n"):
                    addition = "\n"
                elif not output.endswith("\n"):
                    # Double newline
                    addition = "\n\n"
            if saved_value:
                output = output + addition + saved_value
            else:
                output = output + addition + "{0}{1}\n".format("Test Failed: ", err[1])
        results["feedback"] = output


class advanced(Decorator):

    def __init__(self) -> None:
        self.v = True

    @classmethod
    def change_result(cls, saved_value, results:dict, output:str, err):
        """
        Skips the test if student is not advanced.
        Doesn't currently work as no access to student info. So just add to test name.
        """
        if saved_value is not None:
            results["name"] = "[ADV] {}".format(results["name"])
