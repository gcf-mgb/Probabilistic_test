from scipy.stats import invgamma

IG_SHAPE = 1.7084
IG_LOC = -167.8416
IG_SCALE = 2753.7792

def compute_probability(aL):
    """Compute P(A_L > aL) using inverse gamma"""
    if aL <= IG_LOC:
        return 1.0
    cdf = invgamma.cdf(aL - IG_LOC, a=IG_SHAPE, scale=IG_SCALE)
    return 1 - cdf  # probability A_L > aL
