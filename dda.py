import matplotlib.pyplot as plt

def ROUND(a):
	return int(a + 0.5)

def DrawDDA(x1, y1, x2, y2, time_gap, fixed_axis):
    xs = []
    ys = []
    x, y = x1, y1
    xs.append(ROUND(x))
    ys.append(ROUND(y))
    dx = int(x2 - x1)
    dy = int(y2 - y1)
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xInc = float(dx) / float(steps)
    yInc = float(dy) / float(steps)
    for i in range(steps):
        x += xInc
        y += yInc
        xs.append(ROUND(x))
        ys.append(ROUND(y))
    plt.show()
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
    if (fixed_axis):
        plt.axis([-100, 100, -100, 100])
    plt.title("DDA algorithm")
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(xs)):
        plt.scatter(xs[i], ys[i], color='k', s=1)
        plt.pause(float(time_gap))
        plt.draw()
    plt.show()