"""
建模相关程序
"""

import importlib
class B():
    pass




filename="reference.ReferenceModel"
className= "ReferenceModel"
models=__import__(filename)
print(models)
rm = getattr(models,className)()
print(rm)