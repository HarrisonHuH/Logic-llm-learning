from z3 import *

# 1. 声明一个求解器
s = Solver()

# 2. 声明我们要讨论的对象类型 (Sort) 和属性 (Function)
Object = DeclareSort('Object')
Human = Function('Human', Object, BoolSort())
Mortal = Function('Mortal', Object, BoolSort())

# 3. 声明实体变量
Socrates = Const('Socrates', Object)
x = Const('x', Object)

# 4. 添加前提 (Premises)
# 前提 1: 所有人都是必死的 (For all x, if x is Human, then x is Mortal)
s.add(ForAll(x, Implies(Human(x), Mortal(x))))
# 前提 2: 苏格拉底是人
s.add(Human(Socrates))

# 5. 我们要验证的假设 (Hypothesis): 苏格拉底是必死的
hypothesis = Mortal(Socrates)

# 6. 反证法推理：检查“前提成立”且“假设不成立”的情况是否存在
s.add(Not(hypothesis))

result = s.check()
if result == unsat:
    print("推理成功: 假设必定成立 (True)")
elif result == sat:
    print("推理失败: 假设不成立，或者信息不足以推出结论 (False/Unknown)")