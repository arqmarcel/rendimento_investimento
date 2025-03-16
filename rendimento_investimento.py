from functions.imposto_renda import imposto_renda
from functions.iof_regressivo import iof_regressivo

def calcular_valor_futuro(aporte, taxa_anual, dias_aplicacao, valor_inicial=0):
    """
    Calcula o valor futuro de um investimento com aportes mensais e juros compostos.
    A taxa de juros anual é convertida para mensal.
    """
    meses = dias_aplicacao // 30  # Aproximação: 1 mês = 30 dias
    if meses == 0:
        meses = 1  # Garante pelo menos 1 ciclo de juros
    
    # Converter taxa anual para mensal
    taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1
    
    # Cálculo do valor futuro
    vf = valor_inicial * (1 + taxa_mensal) ** meses + aporte * (((1 + taxa_mensal) ** meses - 1) / taxa_mensal)
    return vf

# Entrada de dados
aporte_mensal = float(input("Digite o aporte mensal: "))
taxa_anual = float(input("Digite a taxa de juros anual (em %): ")) / 100
valor_inicial = float(input("Digite o valor inicial do investimento (se houver, senão digite 0): "))
dias_aplicacao = int(input("Digite o prazo da aplicação em dias: "))  # Agora essa é a única variável de tempo

# Cálculo do valor futuro
valor_futuro = calcular_valor_futuro(aporte_mensal, taxa_anual, dias_aplicacao, valor_inicial)

# Cálculo do imposto de renda
aliquota_ir = imposto_renda(dias_aplicacao)
rendimento = valor_futuro - (valor_inicial + (aporte_mensal * (dias_aplicacao // 30)))
imposto_ir = rendimento * aliquota_ir

# Cálculo do IOF (apenas se for resgatado em menos de 30 dias)
aliquota_iof = iof_regressivo(dias_aplicacao)
imposto_iof = rendimento * aliquota_iof

# Valor líquido após impostos
valor_liquido = valor_futuro - imposto_ir - imposto_iof

# Exibição dos resultados
print(f"\nValor Futuro Bruto: R$ {valor_futuro:.2f}")
print(f"Imposto de Renda ({aliquota_ir * 100:.1f}%): R$ {imposto_ir:.2f}")
print(f"IOF ({aliquota_iof * 100:.1f}%): R$ {imposto_iof:.2f}")
print(f"Valor Líquido após IR e IOF: R$ {valor_liquido:.2f}")
