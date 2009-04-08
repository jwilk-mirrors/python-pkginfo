# requirements

def additional_tests():
    import doctest
    return doctest.DocFileSuite('../../docs/index.rst',
                                module_relative=True,
                               )
