def saisie_nombre_valide(input_message) -> int:
     nb = input(input_message)
     while True:
            try:
                nb = int(nb)
                break
            except:
                print('nombre invalide')

     return nb


def convertir_heures_en_minutes(heures:int):
    print(f'{heures}h = {heures * 60}m')

def convertir_minutes_en_heures(minutes:int):
    print(f'{minutes}m = {minutes // 60}h {minutes % 60}m')