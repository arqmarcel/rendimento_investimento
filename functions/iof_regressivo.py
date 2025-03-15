def iof_regressivo(dias):
    """
    Retorna a alíquota do IOF com base na tabela regressiva para investimentos resgatados antes de 30 dias.
    Se o prazo for maior que 30 dias, a alíquota é 0%.
    """
    if dias > 30:
        return 0.0  # Sem IOF
    else:
        # Tabela regressiva do IOF (simplificada)
        tabela_iof = {
            1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66,
            11: 0.63, 12: 0.60, 13: 0.56, 14: 0.53, 15: 0.50, 16: 0.46, 17: 0.43, 18: 0.40, 19: 0.36, 20: 0.33,
            21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 25: 0.16, 26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03, 30: 0.00
        }
        return tabela_iof.get(dias, 1.0)  # Se não encontrar, assume 100% (caso improvável)
