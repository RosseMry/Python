from give_bmi import give_bmi, apply_limit

if __name__ == "__main__":
    try:
        # Ejemplo con 3 personas
        alturas = [1.75, 1.60, 1.70]
        pesos   = [65,   "75",   85]

        # 1. Calcula los IMC de cada uno
        mis_bmis = give_bmi(alturas, pesos) 
        # Resultado aproximado: [21.2, 29.2, 29.4]

        # 2. Aplica el límite de 26 para detectar sobrepeso
        resultado = apply_limit(mis_bmis, 26)

        print(resultado) 
        # Imprime: [False, True, True]
        # (La primera persona está bien, las otras dos superan el límite)
        
    except TypeError as e:
        print(f"¡Éxito! El programa detectó el error correctamente: {e}")