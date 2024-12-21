import math
import itertools

EPSILON = 1e-9


class Expr:
    """
    A small expression tree class to hold either:
      1) a single number, or
      2) an operator with left and right children
    This will help us generate a string with minimal parentheses.
    """

    def __init__(self, value=None, left=None, op=None, right=None):
        # If value is not None, this node is a leaf (a single number).
        # Otherwise, it's an internal node with an operator and two children.
        self.value = value
        self.left = left
        self.op = op
        self.right = right

    def is_leaf(self):
        return self.value is not None

    def evaluate(self):
        """Evaluate the expression's numeric value (float)."""
        if self.is_leaf():
            return self.value
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            # Avoid division by zero
            if abs(right_val) < EPSILON:
                return None
            return left_val / right_val
        else:
            return None

    def __str__(self):
        """
        Convert the expression to a string with minimal parentheses
        according to standard operator precedence and associativity.
        """
        if self.is_leaf():
            # If it's basically an integer, print it as int. Else float.
            # Or you can just always print as float if you prefer.
            if abs(self.value - int(self.value)) < EPSILON:
                return str(int(self.value))
            else:
                return f"{self.value:.4f}"

        # Otherwise, handle operator precedence for the children
        left_str = self.child_str(self.left, self.op, is_left=True)
        right_str = self.child_str(self.right, self.op, is_left=False)
        return f"{left_str} {self.op} {right_str}"

    def child_str(self, child, parent_op, is_left):
        """
        Return string for child, adding parentheses only if necessary.
        We'll use numeric precedence ranks for the operators:
            * and / have higher precedence than + and -.
        For simplicity:
            +, - => precedence 1
            *, / => precedence 2
        """
        if child.is_leaf():
            return str(child)

        # Determine precedence of the child op
        child_op = child.op
        child_precedence = op_precedence(child_op)
        parent_precedence = op_precedence(parent_op)

        # If parent's precedence > child's precedence, we must add parentheses
        # If they have the same precedence, we sometimes need parentheses
        #   especially for '-' and '/' because they are not associative
        #   e.g. (a - b) - c != a - (b - c)
        #        (a / b) / c != a / (b / c)
        need_parens = False
        if parent_precedence > child_precedence:
            need_parens = True
        elif parent_precedence == child_precedence:
            # Check for left-right associativity:
            if parent_op == '-' or parent_op == '/':
                # if we are in the right child for '-' or '/', parentheses needed
                # e.g. a - (b - c) or a / (b / c)
                if not is_left:
                    need_parens = True
                # for the left child in '-' or '/', we do not need parentheses
                #   if it is the same operator, e.g. (a - b) - c is fine
                #   but if child is + or -, we don't necessarily need parentheses
                # This can get more subtle for certain combos,
                # but the logic here is a simplified version.
            # For '+' and '*', which are associative, we do not need parentheses
            # if they have the same precedence.

        child_str_val = str(child)
        if need_parens:
            return f"({child_str_val})"
        else:
            return child_str_val


def op_precedence(op):
    """Return a numerical precedence rank for the four operators."""
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0  # For leaf or unknown operator


def generate_expressions(expressions):
    """
    expressions is a list of Expr objects.
    We pick two expressions from it, combine them with an operator,
    and yield new lists of expressions that have one fewer expression.
    """
    if len(expressions) == 1:
        yield expressions[0]
    else:
        for i in range(len(expressions)):
            for j in range(i + 1, len(expressions)):
                # Pick two different expressions
                A = expressions[i]
                B = expressions[j]
                # All possible operator merges
                for op in ['+', '-', '*', '/']:
                    # A op B
                    new_expr = Expr(left=A, op=op, right=B)
                    new_list = [expressions[k] for k in range(len(expressions)) if k != i and k != j]
                    new_list.append(new_expr)
                    yield from generate_expressions(new_list)

                    # B op A (because - and / are not commutative)
                    # If op is commutative (+ or *), we can skip one direction
                    if op in ['-', '/']:
                        new_expr2 = Expr(left=B, op=op, right=A)
                        new_list2 = [expressions[k] for k in range(len(expressions)) if k != i and k != j]
                        new_list2.append(new_expr2)
                        yield from generate_expressions(new_list2)


def solve_24(nums):
    """
    Main solver for the 24 game. Returns a string expression or None.
    """
    # We will try all permutations of the 4 numbers
    for perm in set(itertools.permutations(nums)):
        # Start with a list of leaf expressions
        initial_exprs = [Expr(value=float(n)) for n in perm]
        # Recursively generate all possible combination expressions
        for expr_tree in generate_expressions(initial_exprs):
            val = expr_tree.evaluate()
            if val is not None and abs(val - 24) < EPSILON:
                return str(expr_tree)
    return None


if __name__ == "__main__":
    # Example usage:
    nums = [3, 6, 9, 11]
    result = solve_24(nums)
    if result:
        print(f"{result} = 24")
    else:
        print("No solution found!")
