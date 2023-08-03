# Crie um dicionário que guarde o nome, ano de nascimento a idade, o ano de
# contratação e o salário de um funcionário. Calcule e acrescente no
# dicionário quantos anos a pessoa se aposentará.

dict_guarda = {
    "nome": input("Informe o nome: "),
    "ano_nascimento": int(input("Informe o ano do nascimento: ")),
    "idade": int(input("Informe a sua idade: ")),
    "ano_contratacao": int(input("Informe o ano da contratação: ")),
    "salario": float(input("Informe o salário: ")),
}

dict_guarda["tempo_aposentadoria"] = 65 - dict_guarda["idade"]

print(dict_guarda)
