def run_formula(dv, param=None):
    defult_param = {'t1': 20 ,'t2':10}
    if not param:
        param = defult_param

    Ad7 = dv.add_formula("Ad7", "-1*(Correlation(close,volume,%s)*Rank(Correlation(close,Delay(close,%s),%s))*(StdDev(Abs(close-Delay(close,%s)),%s)))"
                         % (param['t1'], param['t1'],param['t2'],param['t1'],param['t1']),
                        is_quarterly=False)
    return Ad7
