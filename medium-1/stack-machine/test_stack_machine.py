'''A module to test the stack_machine module'''
import unittest
from stack_machine import minilang

class TestStackMachine(unittest.TestCase):
    '''A class to test the stack_machine module'''
    def test_printing_an_default_register(self):
        '''Print a zero since the register defaults to 0'''
        cmds = 'PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '0')

    def test_perform_an_operation_with_a_value_from_stack_and_register(self):
        '''Perform an operation that involves both the stack and the
           regiser'''
        cmds = '5 PUSH 3 MULT PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '15')

    def test_perform_multiple_print_operations(self):
        '''Perform multiple print operations'''
        cmds = '5 PRINT PUSH 3 PRINT ADD PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '5 3 8')

    def test_push_and_pop_with_a_single_register_value(self):
        '''Push and pop with a single register value'''
        cmds = '5 PUSH POP PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '5')

    def test_multiple_operations_and_prints(self):
        '''Multiple operations and prints'''
        cmds = '3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '5 10 4 7')

    def test_dividing_and_multiplying_operations(self):
        '''Series of operations including divisino and multiplication,
           plus ending whitespace char'''
        cmds = '3 PUSH PUSH 7 DIV MULT PRINT '
        output = minilang(cmds)
        self.assertEqual(output, '6')

    def test_modulus_operations_(self):
        '''Series of operations including modulus'''
        cmds = '4 PUSH PUSH 7 MOD MULT PRINT '
        output = minilang(cmds)
        self.assertEqual(output, '12')

    def test_negative_number(self):
        '''Series of operations including a negative number'''
        cmds = '-3 PUSH 5 SUB PRINT'
        output = minilang(cmds)
        self.assertEqual(output, '8')

    def test_multiple_operations_without_printing(self):
        '''Series of operations not including printing'''
        cmds = '6 PUSH'
        output = minilang(cmds)
        self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
