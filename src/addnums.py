# Author: Conan C. Albrecht <doconix@gmail.com>

############################################
###  Exported function

def addnums(a, b):
    return a + b


######################################################
###  Export the library, depending on the environment

# CommonJS (node/npm)
if typeof(module) is 'object' and module.exports:
    module.exports = addnums

# AMD / requirejs
elif typeof(define) is 'function' and define.amd:
    define([], addnums)

# assume browser
else:
    # add the function to the top-level window object
    window['addnums'] = addnums
