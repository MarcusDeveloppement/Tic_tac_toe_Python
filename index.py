map = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ']]

player = 'Joueur 1'

def draw():
    for i in range(3): 
        for j in range(3):
            print (map[i][j], end="")
        print()

while True: 
    choice = int(input(f'{player}[1-9] : '))
    row = (choice - 1) // 3 
    column = (choice - 1) % 3
    if map[row][column] == ' . ':
        map[row][column] = ' X ' if player == 'Joueur 1' else ' O '
    draw()
    player = 'Joueur 1' if player == 'Joueur 2' else 'Joueur 2'