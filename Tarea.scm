#lang racket

(define (inverso lista n)
  (inverso_ lista n (list ) 0 0)
  )

(define (inverso_ lista  n lista_ i j)
  (if (> (length lista) 1)
      (inverso_ (rest lista) n (Aux lista_ (car lista) (if (= j 0) 0 (+ i 1))) (car lista) (+ j 1))
      (if (= (length lista) 1)
          (inverso_ (list ) n (Aux lista_ (car lista) (if (= j 0) 0 (+ i 1))) (car lista) (+ j 1))
          (Aux lista_ n (if (= j 0) 0 (+ i 1))))))

(define (Aux lista_ num i) 
  (cond
    [(= i num) (append empty lista_)]
    [(< i num) (Aux (append lista_ (list i)) num (+ i 1))]))
;-----------------------------------------------------------------------------
#|
(define (umbral_simple lista umbral tipon)
  ;Realizar el codigo
  )
(define (umbral_cola lista umbral tipo)
  ;Realizar el codigo
  )

(define (modsel_simple lista seleccion f)
  ;Realizar el codigo
  )
(define (modsel_cola lista seleccion f)
  ;Realizar el codigo
  )

(define (estables lista umbral fM fm)
  ;Realizar el codigo
  )

(define (query lista pos op params)
  ;Reaalizar el codigo
  )
|#