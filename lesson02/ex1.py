from jinja2 import Template
from markupsafe import escape

# data = '''Модуль Jinja вместо
# определения {{ name }}
# подставляет соответствующее значение'''

# экранирование
# {% raw %} ... {% endraw %}

# data = '''{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставляет соответствующее значение{% endraw %}'''

# tm = Template(data)
# msg = tm.render(name='Алексей')
#
# print(msg)

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

# флаг e для экранирования специальных символов
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)

# использование escape
msg = escape(link)
print(msg)
