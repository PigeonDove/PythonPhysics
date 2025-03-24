Web VPython 3.2
ball = sphere()
ball.pos.x = 0
ball_v_x = 0
ball_a_x = 0

t = 0
dt = 0.1

t2 = 0
t1 = 0

motion_graph1 = graph(title = 'a-time', xtitle = 't', ytitle ='a')
g_ball_ax = gcurve(color = color.green)

motion_graph2 = graph(title = 'v-time', xtitle = 't', ytitle ='v')
g_ball_vx = gcurve(color = color.blue)

motion_graph3 = graph(title = 'position-time', xtitle = 't', ytitle ='r')
g_ball_posx = gcurve(color = color.red)

def v(t):
    return t

while True :
    sleep(dt)
    ball.pos.x = 0.5*(v(t2) + v(t1)) * (t2 - t1) + ball.pos.x
    ball_a_x = (v(t2) - v(t1)) / (t2 - t1)
    g_ball_posx.plot(pos = (t, ball.pos.x))
    g_ball_vx.plot(pos = (t, v(t)))
    g_ball_ax.plot(pos = (t, ball_a_x))
    t = t + dt
    t1 = t2
    t2 = t
    print('t : ', t, ", r : ", ball.pos.x) 

