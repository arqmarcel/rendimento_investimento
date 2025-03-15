def calcular_valor_futuro(aporte, taxa_anual, meses, valor_inicial=0):
    """
    Calcula o valor futuro de um investimento com aportes mensais e juros compostos.
    A taxa de juros anual é convertida para mensal.
    """
    # Converter taxa anual para mensal
    taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1
    
    # Cálculo do valor futuro
    vf = valor_inicial * (1 + taxa_mensal) ** meses + aporte * (((1 + taxa_mensal) ** meses - 1) / taxa_mensal)
    return vf

def imposto_renda(prazo_dias):
    """
    Retorna a alíquota do imposto de renda com base no prazo do investimento em dias.
    """
    if prazo_dias <= 180:
        return 0.225  # 22,5%
    elif prazo_dias <= 360:
        return 0.20   # 20%
    elif prazo_dias <= 720:
        return 0.175  # 17,5%
    else:
        return 0.15   # 15%

# Entrada de dados
aporte_mensal = float(input("Digite o aporte mensal: "))
taxa_anual = float(input("Digite a taxa de juros anual (em %): ")) / 100
meses = int(input("Digite o número de meses: "))
valor_inicial = float(input("Digite o valor inicial do investimento (se houver, senão digite 0): "))

# Cálculo do valor futuro
valor_futuro = calcular_valor_futuro(aporte_mensal, taxa_anual, meses, valor_inicial)

# Cálculo do imposto de renda
prazo_dias = meses * 30  # Aproximação de um mês como 30 dias
aliquota_ir = imposto_renda(prazo_dias)

# O imposto incide sobre o rendimento (ganho líquido)
rendimento = valor_futuro - (valor_inicial + aporte_mensal * meses)
imposto = rendimento * aliquota_ir
valor_liquido = valor_futuro - imposto

# Exibição dos resultados
print(f"\nValor Futuro Bruto: R$ {valor_futuro:.2f}")
print(f"Imposto de Renda ({aliquota_ir * 100:.1f}%): R$ {imposto:.2f}")
print(f"Valor Líquido após IR: R$ {valor_liquido:.2f}")