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