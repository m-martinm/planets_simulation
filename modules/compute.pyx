from libc.math cimport fmod, cos, sin, fabs, sqrt, atan2, tan

"""
Lower accuracy positions of planets based on these links:
    https://ssd.jpl.nasa.gov/planets/approx_pos.html
    https://www.physicsforums.com/threads/position-and-velocity-in-heliocentric-ecliptic-coordinates.872682/
"""

cdef struct Point:
    double x
    double y

cdef double rad(double x):
    """Converting [deg] to [rad]"""
    return x * 3.1415926535 / 180

cdef double wrapto180(double angle):
    """Simplify an angle"""
    angle = fmod(angle + 180.0, 360.0)
    if angle < 0:
        angle += 360.0
    return angle - 180.0

cpdef Point compute_coordinates(double dt, double a0, double da, double e0,
                                 double de, double I0, double dI, double L0,
                                 double dL, double w0, double dw, double Omega0, double dOmega, double b, double c, double s,
                                 double f):

    # calculating the orbital elements at the given time
    cdef double a = a0 + dt * da
    cdef double e = e0 + dt * de
    cdef double I = I0 + dt * dI
    cdef double L = L0 + dt * dL
    cdef double w = w0 + dt * dw
    cdef double Omega = Omega0 + dt * dOmega

    # w = Omega + argument of the perihelion --> arg_per = w - Omega
    cdef rarg_per = rad(w-Omega)

    cdef double tol = 10**-6
    cdef double mAnomaly = L - w + b * dt * dt + cos(rad(f * dt)) + s * sin(rad(f * dt))
    mAnomaly = wrapto180(mAnomaly)
    cdef double e_x = 57.29578 * e

    cdef double eAnomaly = mAnomaly - e_x * sin(rad(mAnomaly));
    cdef double dE;
    cdef double dM;

    # compute the eccentric Anomaly, eAnomaly in [deg]
    while(1):
        dM = mAnomaly - (eAnomaly - e_x * sin(rad(eAnomaly)))
        dE = dM / (1.0 - e * cos(rad(eAnomaly)))
        eAnomaly = eAnomaly + dE
        if round(fabs(dE), 10) <= tol:
            break
    
    #canonical heliocentric position
    cdef reAnomaly = rad(eAnomaly)
    cdef x_3 = a * (cos(reAnomaly) - e)
    cdef y_3 = a * sin(reAnomaly) * sqrt(1 - e*e)

    # compute true anomaly in [rad]
    rtAnomaly = atan2(y_3, x_3)

    # Rotate the coordinates from canonical to ecliptic
    cdef x_2 = x_3 * cos(rarg_per) - y_3*sin(rarg_per)
    cdef y_2 = x_3 * sin(rarg_per) + y_3*cos(rarg_per)
    cdef x_1 = x_2
    cdef y_1 = y_2 * cos(rad(I))

    # Position in heliocentric ecliptic coordinates
    rOmega = rad(Omega)
    cdef Point coordinates 
    coordinates.x = x_1 * cos(rOmega) - y_1 * sin(rOmega)
    coordinates.y =-( x_1 * sin(rOmega) + y_1 * cos(rOmega)) #multiplied with -1 because of the pygame canvas

    return coordinates