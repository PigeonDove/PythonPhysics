Web VPython 3.2
ball1 = sphere()
ball1.pos.x = 0 #초기 위치 설정
ball1.pos.y = 0 #초기 위치 설정


ball2 = sphere()
ball2.pos.x = 0 #초기 위치 설정
ball2.pos.y = 3 #초기 위치 설정

ball1_a_x = 0 #초기 가속도 설정
ball2_a_x = 1 #초기 가속도 설정

ball1_v_x = 3 #초기 속도 설정
ball2_v_x = 0 #초기 속도 설정

t = 0 #초기 시각 설정
dt = 1 #시간 간격 설정

motion_graph = graph(title = 'xPosition-yPosition', xtitle = 'xPosition', ytitle ='yPosition') #그래프 종이 생성
g_ball_x1 = gcurve(color = color.green) #펜 생성(초록색)
g_ball_x2 = gcurve(color = color.red) #펜 생성(빨간색)

while True :
    sleep(dt) #시간 간격 대기    
    ball1.pos.x = ball1_v_x * dt + ball1.pos.x #ball1 변위 적분 식
    ball2.pos.x = (0.5 * ball2_a_x * dt**2) + (ball2_v_x * dt) + ball2.pos.x #ball2 변위 적분 식
    ball2_v_x = ball2_a_x*dt + ball2_v_x #ball2 속도 적분 식
    t = t + dt  #시간 누적
    print('t : ', t, ', r1 : ', ball1.pos.x, ', r2 : ', ball2.pos.x) #값 출력
    g_ball_x1.plot(pos = (t, ball1.pos.x)) #그래프 그리기
    g_ball_x2.plot(pos = (t, ball2.pos.x)) #그래프 그리기
    if t > 10 : #만약 시간이 10초가 지나면
        break #무한 반복 멈춤
