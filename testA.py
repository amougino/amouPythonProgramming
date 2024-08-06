import operator

comparators = ['==','!=','>','<','>=','<=']

comparators_processes = {
    '==':operator.eq,
    '!=':operator.ne,
    '>':operator.gt,
    '<':operator.lt,
    '>=':operator.ge,
    '<=':operator.le
}

operations = ['+','-','*','/','%','//','**']

operations_processes = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '%':operator.mod,
    '//':operator.floordiv,
    '**':operator.pow
}
print(operator.is_(4,4))