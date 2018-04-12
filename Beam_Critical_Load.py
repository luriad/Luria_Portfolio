# Critical Buckling Load of a Beam
# Programmer: David Luria

import numpy as np
import scipy.linalg as la

def generate_matrix_A(L,N,J):
    """
    Generates matrix A, the finite differences approximation matrix, in banded form
    Also generates vectors of its main and sub diagonal entries
      
    Inputs:
    L : Length of beam
    N : Size of the matrix A, which approximates the differential equation
    J : Moment of inertia of the beam, as a function of x
    
    Outputs:
    a : Vector of subdiagonal entries of matrix A 
    d : Vector of main diagonal entries of matrix A
    matrix_a : Matrix A, in banded form
    
    """
    matrix_a = np.zeros((3,N))
    d = np.zeros(N)
    a = np.zeros(N-1)
    #populate vector d, main diagonal entries
    for i in range(N):
        k = i + 1.5
        J1 = J(L * k / (N+1))
        k = i + 0.5
        J2 = J(L * k / (N+1))
        d[i] = J2 + J1
    #populate vector a, sub diagonal entries
    for j in range(N-1):
        k = j + 1.5
        a[j] = -J(L * k / (N+1))
    #generate banded form of matrix A from a and d  
    for i in range(N-1):
        matrix_a[0,i+1] = a[i]
        matrix_a[2,i] = a[i]    
    for i in range(N):
        matrix_a[1,i] = d[i]

    return (a,d,matrix_a)


def tridiagonal_product(a,d,q):
    """
    Computes the product of subdiagonal matrix A and vector q using vectors
    a and d
    
    Inputs:
    a : Vector of subdiagonal entries of matrix A 
    d : Vector of main diagonal entries of matrix A
    q : Vector to be multiplied by matrix A
    
    Outputs:
    z : solution of the product A . q = z
    """
    N = len(d)
    z = np.zeros(N)
    #This algorithm is simply a direct matrix multiplication
    z[0] = d[0] * q[0] + a[0] * q[1]
    for i in range(1,N-1):
        z[i] = a[i-1] * q[i-1] + d[i] * q[i] + a[i] * q[i+1]
    z[N-1] = a[N-2] * q[N-2] + d[N-1] * q[N-1]
   
    return z


def InversePowerMethod(a, d, matrix_a, tol, maxIter):
   """
   Estimates the lowest magnitude eigenvalue of matrix A using the reverse 
   power method, with a banded matrix solver
   
   Inputs:
   a : Vector of subdiagonal entries of matrix A 
   d : Vector of main diagonal entries of matrix A
   matrix_a : Matrix A, the approximation of the differential equation, in 
              banded form 
   tol : tolerance of convergence of the eigenvalue estimation
   maxIter: maximum allowed iterations for convergence
   
   Outputs:
   nu : estimation of the lowest magnitude eigenvalue of matrix A
   """
   N = len(d)
   q = np.ones(N)
   delta = 1
   nu = np.infty
   converged = False   
   nIter = 0
   
   while not converged and (nIter < maxIter):
       z = la.solve_banded((1,1), matrix_a, q)
       q = z/la.norm(z)
       nu_old = nu
       nu = np.dot(q, tridiagonal_product(a,d,q))
       delta = abs(nu - nu_old)       
       converged = (delta < tol)
       nIter += 1
       
   return (nu)


def critical_load(E,L,N,J):
    """
    Computes the critical load of a beam using the lowest eigenvalue of the 
    differential approximation matrix A.
    
    Inputs:
    E : Young's modulus of the beam
    L : Length of beam
    N : Size of the matrix A
    J : Moment of inertia of the beam, as a function of x
   
    Outputs:
    Pcrit : Critical load of the beam
    """
    a,d,matrix_a = generate_matrix_A(L,N,J)
    lam = InversePowerMethod(a, d, matrix_a, 1e-12, 1000)
    h = L / (N+1)
    Pcrit = lam * E / h**2
    return Pcrit
