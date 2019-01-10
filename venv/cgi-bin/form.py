#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "Ничего небыло заполнено, наверно может быть и логическим, по умолчанию вернёт нан")
text2 = form.getfirst("TEXT_2", "Ничего небыло заполнено, наверно может быть и логическим")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Значение переменной через директиву формат {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")