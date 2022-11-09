#lang racket
#|
(define (inverso lista n)
  (length lista)
  ;crear la lista de numeros hasta n-1 (list)
  ;recorrer la lista y recuperar numero por numero (num)
  if((andmap igual-igual num list) "Sacar el numero" "Mantener el numero")
  ;Realizar el codigo
  
  )

(define (igual-igual num list) (not(boolean? (member num list))))
|#
(define (lista-factorial n list)
  (if(= n 0)(append list 0)
     (append list (- n 1))))
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