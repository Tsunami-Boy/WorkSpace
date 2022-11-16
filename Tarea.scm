#lang racket
#|
(define (inverso lista n)
  (inverso_ lista n (list ))
  )

(define (inverso_ lista  n lista_)
  ;Condicion de que si la lista es mayor estricta que 1 se hace el primer lenth, si es falso hacer las otras 2
  (cond
    [(>= (length(rest lista)) 1) (inverso_ (rest lista) n (Aux lista_ (car lista) (if (= (length lista_) 0) 0 (last lista_))))]
    [(= (length(rest lista)) 0) (inverso_ (list ) n (Aux lista_ (car lista) (if (= (length lista_) 0) 0 (last lista_))))]
    [(= (length lista) 0) (Aux lista_ n (if (= (length lista_) 0) 0 (last lista_)))]
    ))

(define (Aux lista_ num i) 
  (cond
    [(< i num) (Aux (append lista_ (list i)) num (+ i 1))]
    [(= i num) (append empty lista_)]
    ))
(inverso '(1 3 5 7) 8)
|#
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