class CodeMetier:
    def __init__(self, a):
        print("dans code metier")
        self.a = a


def code_factory():
    code_metier = CodeMetier("toto")
    return code_metier


print("dans a importer")
code = code_factory()
