def make_generic_call(client_class, type):
    def c():
        return client_class.get(type)
    return c

def augment(client_class, types):
    for type in types:
        call = make_generic_call(client_class, type)
        setattr(client_class, type, call)