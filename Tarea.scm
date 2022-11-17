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
;----------------------------------------------------------------------------------------------------------

(define (umbral_simple lista umbral tipo)
  (if (equal? tipo #\M)
      (mayor_simple lista umbral 0 (list ))
      (menor_simple lista umbral 0 (list ))))

(define (mayor_simple lista umbral i lista_)
  (if (equal? empty lista)
      (append lista empty)
      (if (> (length lista) 1)
          (if (> (car lista) umbral)
              (mayor_simple (rest lista) umbral (+ i 1) (append lista_ (list i)))
              (mayor_simple (rest lista) umbral (+ i 1) lista_))
          (if (> (car lista) umbral)
              (append lista_ (list i))
              (append lista_ empty)))))

(define (menor_simple lista umbral i lista_)
  (if (equal? empty lista)
      (append lista empty)
      (if (> (length lista) 1)
          (if (< (car lista) umbral)
              (menor_simple (rest lista) umbral (+ i 1) (append lista_ (list i)))
              (menor_simple (rest lista) umbral (+ i 1) lista_))
          (if (< (car lista) umbral)
              (append lista_ (list i))
              (append lista_ empty)))))
;----------------------------------------------------------------------------------------------------------
#|
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