# Proyecto 1: Sistema de Nómina y Bonificaciones Automáticas
# Cliente: Small Business LLC (EE. UU.)

empleados = [
    {"nombre": "Carlos", "horas": 15, "tarifa": 20},
    {"nombre": "Ana", "horas": 8, "tarifa": 25},
    {"nombre": "David", "horas": 20, "tarifa": 22}
]

gran_total = 0

print("==========================================")
print("     SISTEMA DE NÓMINA AUTOMATIZADO      ")
print("==========================================\n")

for emp in empleados:
    pago_base = emp["horas"] * emp["tarifa"]
    
    # Aplica bonificación si gana más de $300
    if pago_base > 300:
        bono = pago_base * 0.10
        pago_total = pago_base + bono
        nota = f"(Incluye $ {bono:.2f} de bono)"
    else:
        pago_total = pago_base
        nota = "(Sin bono)"
        
    gran_total += pago_total
    print(f"• {emp['nombre']}: {emp['horas']} hrs x ${emp['tarifa']}/hr = ${pago_total:.2f} USD {nota}")

print("\n------------------------------------------")
print(f"COSTO TOTAL DE NÓMINA: ${gran_total:.2f} USD")
print("==========================================")
