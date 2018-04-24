def run_formula(dv, param=None):
    defult_param = {'t': 30}
    if not param:
        param = defult_param

    t = param['t']

    Ad4 = dv.add_formula("Ad4", "-1*(StdDev(Return(close,1),%s)*Correlation(open,volume,%s) + Covariance(close,volume,%s))"
                         % (t, t, t),
                        is_quarterly=False,)
    return Ad4