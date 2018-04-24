def run_formula(dv, param=None):
    defult_param = {'t1': 15, 't2': 9, 't3': -1}
    if not param:
        param = defult_param

    alpha141 = dv.add_formula('alpha141',
                         "Rank(Correlation(Rank(high), Rank(Ts_Mean(volume,%s)), %s))* %s" %(
                         param['t1'], param['t2'], param['t3']),is_quarterly=False)
    return alpha141