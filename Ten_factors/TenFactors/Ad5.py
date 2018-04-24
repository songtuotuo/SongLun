def run_formula(dv, param=None):
    defult_param = {'t1': 15,'t2':30,'t3':60}
    if not param:
        param = defult_param

    Ad5 = dv.add_formula("Ad5", "-1*(Rank(Ts_Mean(StdDev(Return(close,%s),%s)+StdDev(Return(close,%s),%s)+StdDev(Return(close,%s),%s),3)))"
                         % (param['t1'],param['t1'],param['t2'],param['t2'],param['t3'],param['t3']),
    is_quarterly=False)
    return Ad5