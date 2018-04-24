def run_formula(dv, param=None):
    defult_param = {'t': 5}
    if not param:
        param = defult_param

    t = param['t']

    Ad3 = dv.add_formula("Ad3", "-1*Rank(Covariance(Rank(high),Rank(volume),%s)+Ts_Mean(Return(close,%s),%s))"
                         % (t, t, t),
                        is_quarterly=False)
    return Ad3
