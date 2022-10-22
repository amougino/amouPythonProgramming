
!PROGRAM pi
!     IMPLICIT NONE
!     integer precision
!     real*16 answer
!     PRINT *, 'Welcome, please enter the number of iteration to compute pi.'
!     READ *, precision
!     call pi_calculator(precision,answer)
!     WRITE(*,"(F53.50)") answer
!END PROGRAM pi

SUBROUTINE pi_calculator(precision,answer)
    IMPLICIT NONE
    real*16 answer,sign
    integer i, precision

    sign = 1.0
    answer = 0.0
    DO i=1,precision+1
        answer = answer + sign/(real(i) * 2.0 - 1.0)
        sign = -1.0*sign
    ENDDO 

    answer=4.0*answer
END SUBROUTINE pi_calculator