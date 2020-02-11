from evaluator import *
call=0
current_state=[]
def new_move():
    global call
    global current_state
    if call == 0:
        data=get_data()
    else:
        data=current_state
    g=data[0]
    time=data[1]
    if call == 0:
        current_state.extend([g,time])
    answer=[]
    for x in data[2:]:
        mass=x[0]
        x_co=x[1]
        y_co=x[2]
        v_x=x[3]
        v_y=x[4]
        particlesf=data[(data.index(x)+1):]
        particlesb=data[2:(data.index(x))]
        sumfgx=0
        sumfgy=0
        for y in data[(data.index(x)+1):]:
            if y == []:
                break
            nmf=y[0]
            x_cof=y[1]
            y_cof=y[2]
            x_comp=(x_cof-x_co)**2
            y_comp=(y_cof-y_co)**2
            sumfgx=sumfgx+((g*mass*nmf)/((((x_cof-x_co)**2)+((y_cof-y_co)**2))**1.5))*(x_cof-x_co)
            sumfgy=sumfgy+((g*mass*nmf)/((((x_cof-x_co)**2)+((y_cof-y_co)**2))**1.5))*(y_cof-y_co)
        for z in data[2:data.index(x)]:
            if z == []:
                break
            nmb=z[0]
            x_cob=z[1]
            y_cob=z[2]
            sumfgx=sumfgx+((g*mass*nmb)/((((x_cob-x_co)**2)+((y_cob-y_co)**2))**1.5))*(x_cob-x_co)
            sumfgy=sumfgy+((g*mass*nmb)/((((x_cob-x_co)**2)+((y_cob-y_co)**2))**1.5))*(y_cob-y_co)
        ax=sumfgx/mass
        ay=sumfgy/mass
        if call == 0:
            delx=v_x*(time)
            dely=v_y*(time)
            v_xn=v_x
            v_yn=v_y
            x_con=x_co + delx
            y_con=y_co + dely
        else:
            v_xn=v_x +(ax*(time))
            v_yn=v_y +(ay*(time))
            delx=v_xn*(time)
            dely=v_yn*(time)
            x_con=x_co + delx
            y_con=y_co + dely
        answer.append([delx,dely])
        if call == 0:
            current_state.append([mass,x_con,y_con,v_xn,v_yn])
        else:
            current_state[data.index(x)]=[mass,x_con,y_con,v_xn,v_yn]
    call = call + 1
    return answer


    







        

