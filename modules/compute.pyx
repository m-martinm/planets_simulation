from libc.math cimport fmod, cos, sin, fabs, sqrt

"""
Lower accuracy formula for planetary positions based on:
    https://ssd.jpl.nasa.gov/planets/approx_pos.html

"""
cdef struct Point:
    double x
    double y

cdef double rad(double x):
    return x * 3.1415926535 / 180

cdef double wrapto180(double angle):
    angle = fmod(angle + 180.0, 360.0)
    if angle < 0:
        angle += 360.0
    return angle - 180.0

cpdef Point compute_coordinates(double dt, double a0, double da, double e0,
                                 double de, double L0,
                                 double dL, double w0, double dw, double b, double c, double s,
                                 double f):

    cdef double a = a0 + dt * da
    cdef double e = e0 + dt * de
    cdef double L = L0 + dt * dL
    cdef double w = w0 + dt * dw

    cdef double tol = 10**-6
    cdef double mAnomaly = L - w + b * dt * dt + cos(rad(f * dt)) + s * sin(rad(f * dt))
    mAnomaly = wrapto180(mAnomaly)
    cdef double e_x = 57.29578 * e

    cdef double eAnomaly = mAnomaly - e_x * sin(rad(mAnomaly));
    cdef double dE;
    cdef double dM;

    while(1):
        dM = mAnomaly - (eAnomaly - e_x * sin(rad(eAnomaly)))
        dE = dM / (1.0 - e * cos(rad(eAnomaly)))
        eAnomaly = eAnomaly + dE
        if round(fabs(dE), 10) <= tol:
            break
    
    cdef Point coordinates
    coordinates.x = a * (cos(rad(eAnomaly)) - e)
    coordinates.y = a * sqrt(1 - (e * e)) * sin(rad(eAnomaly))
    return coordinates