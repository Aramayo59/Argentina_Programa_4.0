
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880


num_paginas = int(input("Ingrese el número de páginas del libro: "))


costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)


if num_paginas > 600:
    costo += COSTO_ENC_ESPECIAL

if 300 < num_paginas <= 600:
    costo += COSTO_ENC_RUSTICA


print("El costo del libro es: $", costo)
