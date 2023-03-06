from jinja2 import Template

# name = "Алексей"
# age = 25

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age

# per = Person("Алексей", 25)

per = {'name': 'Алексей', 'age': 25}

# tm = Template("Мне {{ a*2 }} лет и зовут {{ n.upper() }}")
# tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}")
# tm = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}")
tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}")
# msg = tm.render(n=name, a=age)
msg = tm.render(p=per)

print(msg)

# {%%} - спецификатор шаблона
# {{}} - выражение  для вставки конструкций Python в шаблон
# {##} - блок комментариев
#  # ## - строковый комментарий
