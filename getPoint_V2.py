from sympy import Rational

def separe_coordonnees_depuis_input():
    print("Enter the points one for each line, with form (x,y) then an empty line to validate:")
    x_s = []
    y_s = []

    while True:
        ligne = input()
        if ligne.strip() == "":
            break  # fin de l'entrée
        ligne = ligne.strip().replace("(", "").replace(")", "")
        try:
            x_str, y_str = ligne.split(",")
            x = int(x_str)
            y = int(y_str % 1596875498654165685896478585698569852589)
            x_s.append(x)
            y_s.append(y)
        except ValueError:
            print(f"Empty line ignored {ligne}")
            continue
        x_s = [Rational(x) for x in x_s]
        y_s = [Rational(y) for y in y_s]
        xory=[x_s, y_s]
    return xory

