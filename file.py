import pandas as pd
import matplotlib.pyplot as plt
import os
from platform import system

def get_username_path() -> str:
    return os.getenv("USER") if system() != "Windows" else os.getenv("USERNAME")

def generate_graph(file:str) -> None:
    data = None
    plot_types = ['line', 'bar', 'barh', 'hist', 'box', 'area']

    try:
        match file:
            case _ if file.endswith(".xlsx"):
                data = pd.DataFrame(pd.read_excel(file))
            
            case _ if file.endswith(".json"):
                data = pd.DataFrame(pd.read_json(file))

            case _ if file.endswith(".csv"):
                data = pd.DataFrame(pd.read_csv(file))

            case _:
                print("ERROR: ingrese un archivo Excel, JSON o CSV")
                return
    except PermissionError:
        print("ERROR: Verifique si el archivo no esta en uso")
        return
    
    if data is not None: 
        header()

        while True:
            print("\nGraphs:")
            for i, kind in enumerate(plot_types, start=1):
                print(f"{i} - {kind.capitalize()}")
            
            kind_input = input(f"\nIngrese el tipo de Grafica:").strip().lower()

            if kind_input.isdigit(): 
                if plot_types[int(kind_input)-1]: 
                    break
            elif type(kind_input) == str:
                if kind_input in plot_types:
                    break
            else:
                print("\ERROR: Ingrese un tipo de Grafica valida")
                continue

        kind_chart = plot_types[int(kind_input)-1] if kind_input.isdigit() else kind_input

        try:
            type_chart: str = str(kind_chart)
            if type_chart == "pie":
                data.plot(title=f"Grafico Generado, {os.path.dirname(file)}", kind=str(kind_chart), subplots=True)
            else:
                data.plot(title=f"Grafico Generado, {os.path.dirname(file)}", kind=str(kind_chart))
                plt.show()
        except KeyError as e:
            print("Error Ocurrido: ", e)
    else:
        print(f"\ERROR: No se pudo leer los datos del archivo: {os.path.basename(file)}")
        return

def show_directories(path:str=f"{os.path.curdir}", extensions: list = [".json", ".xlsx", ".csv"]) -> None | list[str]:
    file_count = 0
    files: list[str] = []
    for file in os.listdir(path=path):
        filename, ext = os.path.splitext(file)
        if ext in extensions:
            file_count += 1
            files.append(filename+ext)
            print(f"{file_count} - {filename+ext} ")  
            continue
    print("\n")
    if file_count == 0: 
        print(f"\nNo Se econtraron Archivos Excel, JSON o CSV en el directorio: {path}\n")
        return None 
    return files

def header() -> None:
    print('''\n

 ▗▄▄▖ ▄▄▄ ▗▞▀▜▌▄▄▄▄  ▐▌        ▗▄▄▖▗▞▀▚▖▄▄▄▄  ▗▞▀▚▖ ▄▄▄ ▗▞▀▜▌   ■   ▄▄▄   ▄▄▄ 
▐▌   █    ▝▚▄▟▌█   █ ▐▌       ▐▌   ▐▛▀▀▘█   █ ▐▛▀▀▘█    ▝▚▄▟▌▗▄▟▙▄▖█   █ █    
▐▌▝▜▌█         █▄▄▄▀ ▐▛▀▚▖    ▐▌▝▜▌▝▚▄▄▖█   █ ▝▚▄▄▖█           ▐▌  ▀▄▄▄▀ █    
▝▚▄▞▘          █     ▐▌ ▐▌    ▝▚▄▞▘                            ▐▌             
               ▀                                               ▐▌                      
''')
    print("______________________________________________________________________________________\n")

def main() -> None:  

    allowed_types = [".xlsx", ".json", ".csv"]
    files_list: list[str] = []

    os.system('cls') if system() == "Windows" else os.system("clear")
    
    while True:
        header()
        files_list = show_directories(extensions=allowed_types)
        file: str = input("Ingrese el directorio del Archivo a Leer (.xlsx, .json, .csv) o ('exit' para salir): ").strip()

        if file.lower() != "exit":
            if file.isdigit():
                generate_graph(file=files_list[int(file)-1])
            else:
                generate_graph(file=file)
        else:
            exit()

if __name__ == "__main__":
    main()