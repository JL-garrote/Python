from git import Repo

a = False

a = Repo(r"C:\\Users\\gilga\\Desktop\\Proyectospersonales\\projectoAstro")

if(a):
    print("Repositorio encontrado")
else:
    print("Repositorio no encontrado")
assert not a.bare