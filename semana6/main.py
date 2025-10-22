import regex as re

R=r"[a-z]+"
p = re.compile(r"(?P<numero>\d+)(?P<letra>[a-z]+)");
m=p.fullmatch("3d")

print(m.group(0), m.group(1), m.group(2))
print(m.group("numero"), m.group("letra"))

print(p.sub(r"Numero:\g<numero>, Letra:\g<letra>", m.group(0)))
def entre3(m):
    n=int(m.group(0))
    return str(n/3)


p1 = re.compile(r"(\d+)");

print(p1.sub(entre3,"ab cd 33 fg"))