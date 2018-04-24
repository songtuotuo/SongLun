def run_formula(dv, param=None):
    defult_param = {'t1': 5, 't2':15}
    if not param:
        param = defult_param

    Ad10 = dv.add_formula("Ad10", "-1*Rank(Correlation(Ts_Mean(turnover_ratio,%s),close,%s))*Rank(Ts_Mean((Abs(close-open)+high-low),%s))"
                          % (param['t1'],param['t1'], param['t2']),
                        is_quarterly=False)
    return Ad10
