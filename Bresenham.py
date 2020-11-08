import matplotlib.pyplot as plt

def DrawBre(x1, y1, x2, y2, time_gap):
    steep = 0
    dx = abs(x2 - x1)
    if (x2 - x1) > 0:
        sx = 1
    else:
        sx = -1
    dy = abs(y2 - y1)
    if (y2 - y1) > 0:
        sy = 1
    else:
        sy = -1
    if dy > dx:
        steep = 1
        x1, y1 = y1, x1
        dx, dy = dy, dx
        sx, sy = sy, sx
    d = (2 * dy) - dx
    xs = []
    ys = []
    x = x1
    y = y1
    for i in range(0, dx):
        if steep: 
            xs.append(y)
            ys.append(x)
        else:
            xs.append(x)
            ys.append(y)
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    xs.append(x2)
    ys.append(y2)
    plt.show()
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
    #plt.axis([-100, 100, -100, 100])
    plt.title("Bresenham algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(len(xs)):
        plt.scatter(xs[i], ys[i], color='k', s=1)
        plt.pause(time_gap)
        plt.draw()
    plt.show()