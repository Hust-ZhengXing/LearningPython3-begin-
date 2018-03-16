# 导入只会模块在流程中第一次导入时，加载和执行该模块的代码
# 之后的导入只会使用已加载的模块对象，而不会重载或重新执行文件的代码
# 与from和import相比,reload是内置函数,而不是语句；传给reload的是已经存在的模块对象,而不是变量名。因为reload期望得到的是对象，在重载之前，一定要预先导入模块。
import m6testReload
print(1)
m6testReload.printer()
print(2)
import m6testReload
print(3)

from imp import reload
reload(m6testReload)
print(4)
m6testReload.printer()