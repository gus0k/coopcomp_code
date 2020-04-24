import numpy as np
import scipy as sp
import osqp

from scipy import sparse

def operate_battery_a(T):
    """TODO: 
    A matrix assocaited to the operation of one battery
    in T time-slots.

    :T: TODO
    :returns: TODO

    """
    base = np.tril(np.ones((T, T)), 0)
    res = np.hstack([base, -base])
    res = np.vstack([res, -res])
    res = np.vstack([res,
        np.hstack([np.diag(np.ones(T)), np.zeros((T, T))]),
        np.hstack([np.zeros((T, T)), np.diag(np.ones(T))])])
    return res 

def operate_battery_b(T, bmax, dmax, dmin):
    """
    Defines the right hand side of the matrix problem for
    one player.

    :bmax: TODO
    :dmax: TODO
    :dmin: POSITIVE!
    :returns: TODO

    """
    res = np.hstack([
        np.repeat(bmax, T),
        np.repeat(0, T),
        np.repeat(dmax, T),
        np.repeat(dmin, T),
        ]) 
    return res

def operate_battey_za(T, efc, efd):
    """
    submatrix with efficiencies for the load

    :T: TODO
    :effs: paris of (eta_c, eta_d) for each player.
    :returns: TODO

    """


#np.kron(np.eye(3), A)


