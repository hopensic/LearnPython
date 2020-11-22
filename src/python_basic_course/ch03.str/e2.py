from string import Template

tmpl = Template("Hello ,$who! $what enough for ya?")
d = tmpl.substitute(who="Mars", what="Dusty")
print(d)
