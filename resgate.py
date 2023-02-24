#   Ransomware para decriptografia
#
#   Desenvolvido por Pedro Figueira, Jean Alves, Vinicius Bonicio, Kathellin Ribeiro

f = open("notas.txt", "r")

mensagemResgate = "\n\nEste arquivo foi sequestrado! Para resgatar-lo faça um pix para\n0bc75dc0-823d-47e3-b290-c6c9c8abf459"
chave = 7

texto = f.read()
f.close()

criptografado = ""

for caracter in texto.replace(mensagemResgate, ""):
    criptografado = criptografado + chr(ord(caracter) - chave)

f = open("notas.txt", "w")
f.write(criptografado)
f.close()

f = open("notas.txt", "r")
sequestrado = f.read()
f.close()

g = open("backup.txt", "r")
original = g.read()

if sequestrado == original:
    print("Texto resgatado com sucesso!")
else:
    print("Texto foi quebrado :(")