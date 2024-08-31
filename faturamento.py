import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento_diario']

faturamento_valido = [f for f in faturamento_diario if f > 0]


menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([f for f in faturamento_valido if f > media_mensal])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
