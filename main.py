user = "henrique"
senha = "123"

print("====login====")
login = input("Digite seu Login: ")
password = input("Digite sua senha: ")

if login == user and password == senha:
    print("acesso permitido")
else:
    print("acesso negado") 
    print("tente novamente")
