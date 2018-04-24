def run_formula(dv, param=None):
    defult_param = {'t1': 6, 't2': 2}
    if not param:
        param = defult_param

    alpha36 = dv.add_formula('alpha36',
                         "Rank(Ts_Sum(Correlation(Rank(volume),Rank(vwap),%s),%s))" %(
                         param['t1'], param['t2']),is_quarterly=False)
    return alpha36