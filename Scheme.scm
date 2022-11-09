#lang racket
(define (cuadrado x)
  (* x x))
;Valor absoluto de un numero
(define (val-abs x)
  (if(>= x 0)(+ x)(- x)))

(define lista (list 1 2 3 4 5))

;largo de la lista
(define (largo lista)
  (length lista))

;confirma que el numero no esté en la lista
(define (confirmar lista x)
  (not(boolean? (member x lista))))

;Lista factorial
(define (factorial x y list)
  (if (= x y) list
      (factorial x (+ y 1) (ap-list y list))))
;Agregar un elemento a la lista
(define (ap-list y list)
  (let* ( (y list ) )) y)