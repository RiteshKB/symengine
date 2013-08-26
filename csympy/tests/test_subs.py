from csympy import Symbol, sin, cos, sqrt, Add, function_symbol

def test_basic():
    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    e = x+y+z
    assert e.subs({x: y, z: y}) == 3*y

def test_sin():
    x = Symbol("x")
    y = Symbol("y")
    e = sin(x)
    assert e.subs({x: y}) == sin(y)
    assert e.subs({x: y}) != sin(x)

def test_f():
    x = Symbol("x")
    y = Symbol("y")
    f = function_symbol("f", x)
    g = function_symbol("g", x)
    assert f.subs({function_symbol("f", x): function_symbol("g", x)}) == g
    assert (f+g).subs({function_symbol("f", x): function_symbol("g", x)}) == 2*g

    e = (f+x)**3
    assert e.subs({f: y}) == (x+y)**3
    e = e.expand()
    assert e.subs({f: y}) == ((x+y)**3).expand()
