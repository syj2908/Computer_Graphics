import matplotlib.pyplot as plt

def Drawcircle(x_off, y_off, r, time_gap):
    xs =[]
    ys =[]
    x = 0
    y = r
    p = 5 / 4.0 - r
    xs.append(x)
    ys.append(y)
    while x < y:
        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 2 * (x - y) + 1
        xs.append(x)
        ys.append(y)
    plt.show()
    plt.axis('equal')
    plt.axvline(x=0,linewidth=1, color='k')
    plt.axhline(y=0,linewidth=1, color='k')
    #plt.axis([-100, 100, -100, 100])
    plt.title('midpoint_circle algorithm')
    plt.xlabel('X')
    plt.ylabel('Y')
    for i in range(0,len(xs)):
        if i == 0:
            plt.scatter(xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.pause(time_gap)
        else:
            plt.scatter(xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(-xs[i] + x_off, ys[i] + y_off, color='k', s=1)
            plt.scatter(xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(-xs[i] + x_off, -ys[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(-ys[i] + x_off, xs[i] + y_off, color='k', s=1)
            plt.scatter(ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.scatter(-ys[i] + x_off, -xs[i] + y_off, color='k', s=1)
            plt.pause(time_gap)
            plt.draw()
    plt.show()