def run_formula(dv, param=None):
    defult_param = {'t': 15}
    if not param:
        param = defult_param

    t = param['t']

    Ad9 = dv.add_formula("Ad9", "-1*Rank(Correlation(StdDev(Return(close,1),%s),(close/volume),%s))*Covariance(close,volume,%s)"
                         % (t, t, t),
                        is_quarterly=False)
    return Ad9