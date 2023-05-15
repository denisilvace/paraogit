while True:
  print('''1 - Cadastrar uma pessoa
2 - Listar pessoas cadastradas
3 - Encerrar programa''')
  opc = input("Digite uma opção: ")
  try:
    opcint = int(opc)
    if opcint == 1:
      while True:
        Nome = input("Digite seu nome: ")
        try:
          myint = int(Nome)
          print("nome invalido")
        except ValueError:
          break
      while True:
        CPF = input("Digite seu cpf: ")
        try:
          myint2 = int(CPF)
          if len(CPF) == 11:
            break
          else:
            print("cpf invalido")
        except ValueError:
          print("Digite somente números")
      while True:
        RG = input("Digite seu RG: ")
        try:
          myint3 = int(RG)
          break
        except ValueError:
          print("Digite somente números")
      while True:
        nasc = input("Digite sua data de nascimento: ")
        try:
          myint4 = int(nasc)
          if len(nasc) == 8:
            break
          else:
            print("data de nascimento errada")
        except ValueError:
          print("Digite somente números")
      while True:
        Telefone = input("Digite seu telefone: ")
        try:
          myint5 = int(Telefone)
          if len(Telefone) == 11:
            break
          else:
            print("Telefone de celular inválido")
        except ValueError:
          print("Digite somente números")
      while True:
        Endereco = input("Digite seu endereço: ")
        try:
          myint6 = int(Endereco)
          print("Digite um endereço válido")
        except ValueError:
          break
      while True:
        Numero = input("Digite o número da casa: ")
        try:
          myint7 = int(Numero)
          break
        except ValueError:
          print("Digite somente números")
      while True:
        Complemento = input("Digite o complemento da casa: ")
        try:
          myint8 = int(Complemento)
          print("Digite um complemento válido")
        except ValueError:
          break
      while True:
        CEP = input("Digite o seu CEP: ")
        try:
          myint9 = int(CEP)
          if len(CEP) == 8:
            break
          else:
            print("Digite um Cep Válido")
        except ValueError:
          print("Digite somente números")
      while True:
        Cidade = input("Digite sua cidade: ")
        try:
          myint10 = int(Cidade)
          print("Digite uma cidade válida")
        except ValueError:
          break
      while True:
        UF = input("Digite a sigla do seu estado: ")
        try:
          myint11 = int(UF)
          print("Digite a UF de maneira correta")
        except ValueError:
          if len(UF) == 2:
            break
          else:
            print("digite a UF correta")
      while True:
        Nome_Pai = input("Digite o nome completo do pai: ")
        try:
          myint12 = int(Nome_Pai)
          print("Digite o nome do Pai de maneira correta")
        except ValueError:
          break
      while True:
        Nome_mae = input("Digite o nome completo da mãe: ")
        try:
          myint13 = int(Nome_mae)
          print("Digite o nome da mãe de maneira correta")
        except ValueError:
          break
      novo_ser = (f"Nome: {Nome}", f"CPF: {CPF}", f"RG: {RG}",
                  f"Data de nascimento: {nasc}", f"Telefone: {Telefone}",
                  f"Endereço: {Endereco}", f"Número: {Numero}",
                  f"Complemento: {Complemento}", f"CEP: {CEP}",
                  f"Cidade: {Cidade}", f"UF: {UF}", f"Nome do Pai: {Nome_Pai}",
                  f"Nome da mãe: {Nome_mae}")
      nome_do_arquivo = Nome
      with open(f"{nome_do_arquivo}.txt", 'a') as arquivo:
        for i in novo_ser:
          arquivo.write(str(i) + '\n')
    elif opcint == 2:
      Dados = input("Digite o nome do usuário: ")
      with open(f"{Dados}.txt", 'r') as arquivo:
        for i in arquivo:
          print(arquivo.read())
    elif opcint == 3:
      print("Programa finalizado com sucesso, até breve!")
      break
    else:
      print("digite um opção válida")
  except ValueError:
    print("Digite somente números")
