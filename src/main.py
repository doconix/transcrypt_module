# Author: Conan C. Albrecht <doconix@gmail.com>

############################################
###  Exported function

def addnums(a, b):
    return a + b


######################################################
###  Export the library, depending on the environment

def factory():
    # return a reference to the function that should be exported
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
    f = factory()
    window[f.js_name] = f
