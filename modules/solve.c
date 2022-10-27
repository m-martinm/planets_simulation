#include <math.h>
#include <stdio.h>

struct Point {
  double x;
  double y;
};

double rad(double x) { return x * M_PI / 180; }

double wrapto180(double angle) {

  angle = fmod(angle + 180.0, 360.0);
  if (angle < 0) {
    angle += 360;
  }
  return angle - 180;
}

struct Point compute_coordinates(double dt, double a0, double da, double e0,
                                 double de, double I0, double dI, double L0,
                                 double dL, double w0, double dw, double W0,
                                 double dW, double b, double c, double s,
                                 double f) {

  /*
  dt: centuries past J2000
  a0, da : semi-major axis [au, au/century]
  e0, de : eccentricity
  I0, dI : inclination [degrees, degrees/century]
  L0, dL : mean longitude [degrees, degrees/century]
  w0, dw (omega): longitude of perihelion [degrees, degrees/century]
  W0, dW (capital omega) : longitude of the ascending node [degrees,
  degrees/century] b, c, s, f additional terms for Jupiter through Neptune
  */

  // six values of the planet based on time
  double a = a0 + dt * da;
  double e = e0 + dt * de;
  double I = I0 + dt * dI;
  double L = L0 + dt * dL;
  double w = w0 + dt * dw;
  double W = W0 + dt * dW;

  // tolerance 10^-6
  double tol = pow(10, -6);

  // mean anomaly M = L - w + b*T^2 + cos(f*T) + s*sin(f*T)
  double mAnomaly = L - w + b * dt * dt + cos(rad(f * dt)) + s * sin(rad(f * dt));
  mAnomaly = wrapto180(mAnomaly);
  double e_x = 57.29578 * e;

  // eccentric anomaly
  double eAnomaly = mAnomaly - e_x * sin(rad(mAnomaly));
  double dE;
  double dM;
  do {

    dM = mAnomaly - (eAnomaly - e_x * sin(rad(eAnomaly)));
    dE = dM / (1 - e * cos(rad(eAnomaly)));
    eAnomaly = eAnomaly + dE;
    if (fabs(dE) <= tol)
      break;

  } while (1);

  // found eccentric anomaly, calculating the heliocentric coordinates
  struct Point coordinates;
  coordinates.x = a * (cos(rad(eAnomaly)) - e);
  coordinates.y = a * sqrt(1 - (e * e)) * sin(rad(eAnomaly));

  return coordinates;
}