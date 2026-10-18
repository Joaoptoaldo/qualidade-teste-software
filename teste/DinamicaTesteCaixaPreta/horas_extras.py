"""
Dinâmica de Teste Caixa Preta
Funcionalidade 1: percentual de horas extras semanais.

Regras:
- Jornada padrão semanal: 40 horas.
- Horas extras = horas trabalhadas - 40 (nunca negativo).
- Percentual de horas extras = horas extras / 40 * 100.
- Alerta se o percentual for MAIOR que 25% (ou seja, mais de 50 horas).
"""

HORAS_PADRAO = 40.0
LIMITE_PERCENTUAL = 25.0
LIMITE_HORAS_SEMANA = 7 * 24  # 168 h = máximo fisicamente possível


def calcular(horas_trabalhadas: float) -> dict:
    """Retorna horas extras, percentual e se excede o limite de 25%"""
    if horas_trabalhadas < 0:
        raise ValueError("O número de horas não pode ser negativo.")
    if horas_trabalhadas > LIMITE_HORAS_SEMANA:
        raise ValueError("Uma semana tem no máximo 168 horas.")

    horas_extras = max(0.0, horas_trabalhadas - HORAS_PADRAO)
    percentual = horas_extras / HORAS_PADRAO * 100
    return {
        "horas_extras": horas_extras,
        "percentual": percentual,
        "excede_limite": percentual > LIMITE_PERCENTUAL,
    }


def ler_horas() -> float:
    texto = input("Informe o número de horas trabalhadas na semana: ").strip()
    texto = texto.replace(",", ".")  # aceita vírgula decimal
    return float(texto)


def main() -> None:
    print("Controle de Horas Extras (RH)")
    try:
        resultado = calcular(ler_horas())
    except ValueError as erro:
        # cobre tanto texto não numérico quanto as regras de validação
        print(f"Entrada inválida: {erro}")
        return

    print(f"Horas extras: {resultado['horas_extras']:.2f} h")
    print(f"Percentual de horas extras: {resultado['percentual']:.2f}%")
    if resultado["excede_limite"]:
        print("ATENÇÃO: funcionário com mais de 25% de horas extras na semana.")
    else:
        print("Dentro do limite de 25% de horas extras.")


if __name__ == "__main__":
    main()
