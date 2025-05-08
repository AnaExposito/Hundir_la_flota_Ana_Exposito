# Hundir_la_flota_Ana_Exposito
Juego naval por turnos para hundir barcos

El juego de Hundir la Flota consiste en un tablero donde se colocan barcos y el objetivo es "hundir" todos los barcos del oponente adivinando sus posiciones. 

***

Se crea un tablero y se definen los barcos de los jugadores.

Las acciones principales son colocar barcos (aunque en esta versión ya están colocados para el jugador) y disparar a posiciones del tablero enemigo

 El juego se centra en gestionar el flujo de turnos contra la máquina, donde ambos jugadores intentan hundir la flota del otro adivinando sus ubicaciones.


***

Reglas del juego: 

Tableros: Cada jugador tiene dos tableros de cuadrícula. En uno coloca sus barcos de forma secreta. El otro se usa para marcar los disparos al oponente.

Flota: Cada jugador tiene una flota de barcos de diferentes tamaños (ej: portaaviones, acorazado, destructor, submarino, patrullera).

Colocación: Los barcos se colocan horizontal o verticalmente en el tablero, sin superponerse y, tradicionalmente, dejando al menos un espacio de "agua" entre ellos.

Turnos: Los jugadores se turnan para "disparar" a una casilla del tablero enemigo, nombrando la fila y la columna.

Resultados: El oponente indica si el disparo es:

Agua: No hay barco en esa casilla.

Tocado: Parte de un barco ha sido alcanzada.

Hundido: Todas las partes de un barco han sido alcanzadas. El jugador debe indicar qué barco ha sido hundido.

Marcado: Los jugadores marcan en su tablero de "disparos" los aciertos y fallos para llevar un registro de sus ataques. En su tablero de barcos, marcan los impactos recibidos.

Victoria: El primer jugador en hundir todos los barcos de la flota enemiga gana la partida.