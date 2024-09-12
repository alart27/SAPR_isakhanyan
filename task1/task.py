import pandas as pd
import sys

def get_cell_value(file_path: str, row: int, column: int):
    # Чтение CSV-файла в DataFrame
    try:
        df = pd.read_csv(file_path, delimiter = ";")#ПРИ НЕОБХОДИМОСТИ ПОМЕНЯТЬ РАЗДЕЛИТЕЛЬ
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    
    #print(df,len(df), len(df.columns), df.columns.tolist() )
    # Проверка, что строка и колонка находятся в допустимых пределах
    if row < 0 or row >= len(df) or column < 0 or column >= len(df.columns):
        print("Ошибка: номер строки или колонки вне допустимого диапазона.")
        return None

    # Получение значения ячейки
    cell_value = df.iloc[row, column]
    print(f"Значение ячейки на пересечении строки {row+1} и колонки {column+1}: {cell_value}")

    
    return df

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: python script.py <путь_к_csv> <номер_строки> <номер_колонки>")
        sys.exit(1)

    file_path = sys.argv[1]
    #print(sys.argv)
    try:
        row = int(sys.argv[2]) - 1  # Смещение на 1, чтобы переданная строка соответствовала индексу
        column = int(sys.argv[3]) - 1  # Смещение на 1, чтобы переданная колонка соответствовала индексу
    except ValueError:
        print("Ошибка: номер строки и номера колонки должны быть целыми числами.")
        sys.exit(1)

    table = get_cell_value(file_path, row, column)

