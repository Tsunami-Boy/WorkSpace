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

;(inverso '() 10)
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

;(umbral_simple '(15 2 1 3 27 5 10) 5 #\M)
;(umbral_simple '(15 2 1 3 27 5 10) 5 #\m)
;----------------------------------------------------------------------------------------------------------
#|
(define (umbral_cola lista umbral tipo)
  ;Realizar el codigo
  )
|#
;----------------------------------------------------------------------------------------------------------
(define (modsel_simple lista seleccion f)
  (modsel_simple_ lista seleccion f (list ) 0)
  )

(define (modsel_simple_ lista seleccion f lista_ i)
  (if (equal? empty lista)
      (append lista_ empty)
      (if (> (length lista) 1)
          (if (confirmar seleccion i)
              (modsel_simple_ (rest lista) seleccion f (append lista_ (list (f (car lista)))) (+ i 1))
              (modsel_simple_ (rest lista) seleccion f (append lista_ (list (car lista))) (+ i 1)))
          (if (confirmar seleccion i)
              (append lista_ (list (f (car lista))))
              (append lista_ (list (car lista)))))))

(define (confirmar lista num)
  (not (boolean? (member num lista))))

;(modsel_simple '(15 2 1 3 27 5 10) '(0 4 6) (lambda (x) (modulo x 2)))
;(modsel_simple '(15 2 1 3 27 5 10) '(3 1 2) (lambda (x) (+ x 5)))
;----------------------------------------------------------------------------------------------------------
#|
(define (modsel_cola lista seleccion f)
  ;Realizar el codigo
  )
;----------------------------------------------------------------------------------------------------------
(define (estables lista umbral fM fm)
  (list (estables_fM lista umbral fM)(estables_fm lista umbral fm)))

(define (estables_fM lista umbral fM)
  (if (equal? lista empty)
      0
      (length (umbral_simple
               (umbral_simple lista umbral #\M); Aplicarles f
               umbral
               #\M))))

(define (estables_fm lista umbral fm)
  (if (equal? lista empty)
      0
      (length (umbral_simple
               (umbral_simple lista umbral #\m); Aplicarles f
               umbral
               #\m))))
;----------------------------------------------------------------------------------------------------------
(define (query lista pos op params)
  ;Reaalizar el codigo
  )
|#