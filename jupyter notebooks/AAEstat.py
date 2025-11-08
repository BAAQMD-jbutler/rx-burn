"""
Python Module with functions to calculate linear regression and the absorption Angstrom exponent with numpy and statsmodels modules.

Last Updated: 25 October 2025
Author: James Butler

"""

import numpy as np
import pandas as pd
import statsmodels.api as sm

def linReg95(X,Y):
    '''
    A function to compute a linear regression with no constant and 95% CI    
    '''
    mask = ~np.isnan(X) & ~np.isnan(Y) # filter out NaNs
    X = X[mask]
    Y = Y[mask]
    
    model = sm.OLS(Y,X) # initialize statsmodel
    r = model.fit()     # compute linear fit
    
    m = r.params[0]     # 
    r2 = r.rsquared

    m_u = r.conf_int().values[0,0]
    m_l = r.conf_int().values[0,1]
    
    return m,m_l,m_u,r2,r


# define linear regression function to calculate AAE
def calcAAE(row,wl,label):
    import pandas as pd
    b_abs = row[['b_' + str(wl[i]) for i in range(len(wl))]].to_list()
    
    log_wl = np.log(wl)
    log_b = np.log(b_abs)
        
    log_wl = sm.add_constant(log_wl)

    model = sm.OLS(log_b,log_wl)
    r = model.fit()
    
    m = r.params[1]
    b = r.params[0]
    r2 = r.rsquared

    AAE = -m
    C = np.exp(b)
    
    series = pd.Series([AAE,r2,C],index=['AAE_'+label,'r2_'+label,'C_'+label])
    
    return series

# define linear regression function to calculate AAE
def calcBrCAAE(row,wl,label):
    
    b_abs = row[['b_' + str(wl[i]) + '_BrC' for i in range(len(wl))]].to_list()
    
    log_wl = np.log(wl)
    log_b = np.log(b_abs)
        
    log_wl = sm.add_constant(log_wl)

    model = sm.OLS(log_b,log_wl)
    r = model.fit()
    
    m = r.params[1]
    b = r.params[0]
    r2 = r.rsquared
    #mu = r.conf_int().values[1,0]
    #ml = r.conf_int().values[1,1]
    AAE = -m
    C = np.exp(b)
    #AAE_u = -mu
    #AAE_l = -ml
    
    series = pd.Series([AAE,r2,C],index=['AAE_'+label,'r2_'+label,'C_'+label])
    
    return series


# define linear regression function to calculate AAE
def calcAAE_CI(meanAbs,wl):
    
    log_wl = np.log(wl)
    log_b = np.log(meanAbs)
        
    log_wl = sm.add_constant(log_wl)

    model = sm.OLS(log_b,log_wl)
    r = model.fit()
    
    m = r.params[1]
    b = r.params[0]
    r2 = r.rsquared
    
    mu = r.conf_int().values[1,0]
    ml = r.conf_int().values[1,1]
    
    Cu = np.exp(r.conf_int().values[0,1])
    Cl = np.exp(r.conf_int().values[0,0])
    AAE = -m
    C = np.exp(b)
    AAE_u = -mu
    AAE_l = -ml
    
    return AAE,AAE_l,AAE_u,C,Cl,Cu,r2