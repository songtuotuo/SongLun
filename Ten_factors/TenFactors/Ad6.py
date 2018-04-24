def run_formula(dv, param=None):
    defult_param = {'t': 10}
    if not param:
        param = defult_param

    t = param['t']

    Ad6 = dv.add_formula("Ad6", "-1*((Ts_Sum(Ts_Min((high+close+open+low),%s),%s)/Ts_Sum((high+close+open+low),%s))*Ts_Mean(volume,%s))"
                         %(t,t,t,t),
                        is_quarterly=False)
    return Ad6