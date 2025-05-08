import Hundir_la_flota_utils as utils
import Hundir_la_flota_variables as vr
import time

def main():

    print("*Bienvenido al juego 'Hundir la flota*")
          
    #crear tableros
    tablero_rival_barcos = utils.crear_tablero()
    tablero_rival_disparos = utils.crear_tablero()  
    tablero_jugador_barcos = utils.crear_tablero()  
    tablero_jugador_disparos = utils.crear_tablero()  

    #colocar barcos
    tablero_jugador_barcos = utils.colocar_barcos(tablero_jugador_barcos, vr.barco_jugador)
    tablero_rival_barcos = utils.colocar_barcos(tablero_rival_barcos, vr.barco_rival)

    #flujo del juego
    juego_en_marcha = True #On
    turno_jugador = True #On
    disparos_maquina = set() #Almacen de disparos rival

    #bucle del juego
    while juego_en_marcha:
        if turno_jugador:
            print("\n--- Tu turno ---")
            print("El tablero del rival es:")
            print(tablero_rival_disparos)
            tablero_rival_barcos, vr.lista_disparos = utils.disparo(tablero_rival_barcos, vr.lista_disparos)
            utils.actualizar_tablero_disparos(tablero_rival_disparos, tablero_rival_barcos)
            if utils.comprobar_hundido(tablero_rival_barcos):
                print("\n¡Has ganado!! ;)")
                juego_en_marcha = False
            turno_jugador = False
        else:
            print("\n--- Turno del rival... ---")
            time.sleep(5) 
            fila_maquina, columna_maquina = utils.disparo_rival(tablero_jugador_barcos, disparos_maquina)
            print(f"El rival ha disparado a...: ({fila_maquina}, {columna_maquina})")
            print(tablero_jugador_disparos, tablero_jugador_barcos)
            print("Tu tablero es:")
            print(tablero_jugador_barcos)
            if utils.comprobar_hundido(tablero_jugador_barcos):
                print("\n¡Oh, tu rival ha ganado.... :'( )")
                juego_en_marcha = False
            turno_jugador = True

    if not juego_en_marcha:
            print("\n--- Fin del juego ---")
            print("\nTablero final del rival:")
            print(tablero_rival_barcos)
            print("\nTu tablero final:")
            print(tablero_jugador_barcos)
            
if __name__ == "__main__":
    main()
