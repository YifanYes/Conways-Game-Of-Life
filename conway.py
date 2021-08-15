import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ALIVE = 255
DEAD = 0
vals = [ALIVE, DEAD]

def randomGrid(N):
    #Devuelve un grid de valores random NxN
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    #Añade un glider con una celda arriba a la izquierda en (i, j)
    glider = np.array([[0,    0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def addGosperGliderGun(i, j, grid):
    #Añade a Gosper Glider Gun con una celda arriba a la izquierda en (i, j)
    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255

    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255

    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255

    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255

    grid[i:i+11, j:j+38] = gun

def update(frameNum, img, grid, N):
    # Una copia del grid ya que necesitamos 8 vecinos para hacer los calculos y aplicar las reglas
    # Vamos de linea en linea

    newGrid = grid.copy()

    for i in range(N):
        for j in range(N):
            # Calcula la suma de los 8 vecinos usando una superficie toroidal
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # Aplica las reglas de Conway 
            if grid[i, j]  == ALIVE:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = DEAD

            else:
                if total == 3:
                    newGrid[i, j] = ALIVE

    # Actualiza los datos 
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# funcion main() 
def main():

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
    
    # Fija el tamaño del grid 
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
        
    # Fija el intervalo de actualizacion del intervalo 
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # Declara el grid 
    grid = np.array([])

    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)

    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)

    else:
        # populate grid with random on/off - more off than on
        grid = randomGrid(N)

    # Crea la animacion 
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    # Numero de frames y fija el fichero de salida
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

# Llamada a la main()
if __name__ == '__main__':
    main()