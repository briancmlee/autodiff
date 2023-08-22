class Add:
    def __init__(self, a, b, grad=0):
        self.a = a
        self.b = b
        self.result = None
        self.grad = grad

    def __str__(self):
        return f"({self.a} + {self.b})"

    def __repr__(self):
        return f"({self.a} + {self.b})"

    def __call__(self):
        if not self.result:
            self.result = self.a() + self.b()
            self.a.grad += self.grad
            self.b.grad += self.grad
        
        return self.result

class Mul:
    def __init__(self, a, b, grad=0):
        self.a = a
        self.b = b
        self.result = None
        self.grad = grad

    def __str__(self):
        return f"({self.a} * {self.b})"

    def __repr__(self):
        return f"({self.a} * {self.b})"

    def __call__(self):
        if not self.result:
            self.result = self.a() * self.b()
            self.a.grad += self.grad * self.b()
            self.b.grad += self.grad * self.a()
        
        return self.result

class Div:
    def __init__(self, a, b, grad=0):
        self.a = a
        self.b = b
        self.result = None
        self.grad = grad

    def __str__(self):
        return f"({self.a} / {self.b})"

    def __repr__(self):
        return f"({self.a} / {self.b})"

    def __call__(self):
        if not self.result:
            self.result = self.a() / self.b()
            self.a.grad += self.grad / self.b()
            self.b.grad += self.grad * self.a() / (self.b() ** 2)
        
        return self.result


class Sub:
    def __init__(self, a, b, grad=0):
        self.a = a
        self.b = b
        self.result = None
        self.grad = grad

    def __str__(self):
        return f"({self.a} - {self.b})"

    def __repr__(self):
        return f"({self.a} - {self.b})"
    
    def __call__(self):
        if not self.result:
            self.result = self.a() - self.b()
            self.a.grad += self.grad
            self.b.grad -= self.grad
        
        return self.result

class Const:
    def __init__(self, a, name=None, grad=0):
        self.a = a
        self.name = name
        self.grad = grad

    def __call__(self):
        return self.a

    def __str__(self):
        return f"({self.name}: {self.a})"

    def __repr__(self):
        return f"({self.name}: {self.a})"

def get_f(x,y):
    x = Const(x, "x")
    y = Const(y, "y")
    compute_graph = ([x, y], Add(Mul(x, x), Mul(x, y), grad=1))
    return compute_graph