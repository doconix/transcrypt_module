# Author: Conan C. Albrecht <doconix@gmail.com>

############################################
###  Exported function

def addnums(a, b):
    return a + b


######################################################
###  Export the library, depending on the environment

def factory():
    '''Return the exported function from this module.'''
    return addnums

# CommonJS (node/npm)
if typeof(module) is 'object' and module.exports:
    module.exports = factory()

# AMD / requirejs
elif typeof(define) is 'function' and define.amd:
    define([], factory)

# assume browser
else:
    # add the function to the top-level window object
    window['addnums'] = factory()
