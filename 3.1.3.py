def stop_iteration():
    raise StopIteration

def zero_division():
    1 / 0

def assertion():
    assert False

def import_error():
    import something

def key_error():
    dictionary = {}
    print(dictionary["key"])

def syntax_error():
    compile("if True print('hello')", "", "exec")

def indentation_error():
    compile("if True:\nprint('hello')", "", "exec")

def type_error():
    5 + "hello"


stop_iteration()
zero_division()
assertion()
import_error()
key_error()
syntax_error()
indentation_error()
type_error()