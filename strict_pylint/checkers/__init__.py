from strict_pylint.checkers.basic import ReturnChecker


def register_checkers(linter):
    """Register checkers."""
    linter.register_checker(ReturnChecker(linter))
