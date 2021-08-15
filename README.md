
# Conway's Game of Life

Conway's Game of Life es un metodo de automatizacion celular creado por John Conway.

Este juego fue creado con la biologia en mente pero ha sido aplciado en varios campos, como en diseño grafico, generaccion de terreno, etc.

El "juego" es para cero jugadores, la evolucion esta determinado por su estado inicial, no necesita mas interraccion. El jugador crea la configuracion inicial del tablero y observa como evoluciona, o para jugadores mas avanzados, intentar crear patrones con propiedades especiales.

**Como funciona el juego**
Ya que Game of Life esta construido sobre un grid de nueve cuadrados, cada celula tiene ocho celulas vecinas. La evolucion sigue cuatro reglas:
- Si una celula esta viva y tiene menos de dos vecinos vivos, muere.
- Si una celula esta viva y tiene o dos o tres vecinos vivos, sigue viviendo.
- Si una celula esta viva y tiene mas de tres vecinos vivos, muerte (por sobrepoblacion).
- Si una celula esta muerta y tiene exactamente tres vecinos vivos, vuelve a la vida.

**Requisitos**
- numpy
- matplotlib
- argparse
- pygame

