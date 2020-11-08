import matplotlib.pyplot as plt

def Drawellipse(xc, yc, rx, ry):
    xs = []
    ys = []
    x = 0
    y = ry
    p = (ry * ry) - (rx * rx * ry) + ((rx * rx) / 4)
    while (x * ry * ry) < (y * rx * rx):
        xs.append(x)
        ys.append(y)
        if p < 0:
            x += 1
            p += (2 * ry * ry * x) + (ry * ry)
        else:
            x += 1
            y -= 1
            p += (2 * ry * ry * x + ry * ry) - (2 * rx * rx * y)
    p = (x + 0.5) * (x + 0.5) * ry * ry + (y - 1) * (y - 1) * rx * rx - rx * rx * ry * ry
    while (y > 0):
        xs.append(x)
        ys.append(y)
        if p > 0:
            y -= 1
            p -= (2 * rx * rx * y) + (rx * rx)
        else:
            x += 1
            y -= 1
            p += (2 * ry * ry * x) - (2 * rx * rx * y) - (rx * rx)
    plt.show()
    plt.axis('equal')
    plt.axvline(x=0, linewidth=1, color='k')
    plt.axhline(y=0, linewidth=1, color='k')
    #plt.axis([-100, 100, -100, 100])
    plt.title('midpoint_ellipse algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(xs)):
        if i == 0:
            plt.scatter(xs[i] + xc, ys[i] + yc, color='k', s=1)
            plt.scatter(xs[i] + xc, -ys[i] + yc, color='k', s=1)
            plt.pause(0.1)
        else:
            plt.scatter(xs[i] + xc, ys[i] + yc, color='k', s=1)
            plt.scatter(-xs[i] + xc, ys[i] + yc, color='k', s=1)
            plt.scatter(xs[i] + xc, -ys[i] + yc, color='k', s=1)
            plt.scatter(-xs[i] + xc, -ys[i] + yc, color='k', s=1)
            plt.pause(0.1)
            plt.draw()
    plt.show()