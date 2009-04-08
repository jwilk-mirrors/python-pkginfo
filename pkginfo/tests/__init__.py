# requirements

def additional_tests():
    import doctest
    return doctest.DocFileSuite('../../README.txt',
                                module_relative=True,
                               )
