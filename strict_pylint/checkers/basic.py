
import sys

import astroid
import astroid.bases
import astroid.scoped_nodes

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import check_messages


PY33 = sys.version_info >= (3, 3)
PY3K = sys.version_info >= (3, 0)
PY35 = sys.version_info >= (3, 5)


class ReturnChecker(BaseChecker):

    __implements__ = IAstroidChecker
    name = 'returnchecker'

    msgs = {
        'W7001': ('Only one item in tuple on return',
                  'single-item-tuple',
                  'It\'s possible the "return" statement line ends with comma'),
    }

    @check_messages('single-item-tuple')
    def visit_return(self, node):
        chld = node.last_child()
        if isinstance(chld, astroid.Tuple):
            if len(list(chld.get_children())) == 1:
                self.add_message('single-item-tuple', node=node)
