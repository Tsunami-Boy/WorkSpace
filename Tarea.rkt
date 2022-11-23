#lang racket (current-namespace
(make-base-namespace))

(define (inverso lista n)
  (inverso_ lista n (list ) 0 0)
  )

;;inverso_ : realiza recursividad de la funcion inverso a partir de una lista auxiliar 
;;
;;lista: lista con los numeros que no deben ser agregados
;;n: numero maximo (no se debe tomar en cuenta) al que se debe llegar en la lista_
;;lista_: lista vacia auxiliar
;;i: entero auxiliar
;;j: entero auxiliar
(define (inverso_ lista  n lista_ i j)
  (if (> (length lista) 1)
      (inverso_ (rest lista) n (Aux lista_ (car lista) (if (= j 0) 0 (+ i 1))) (car lista) (+ j 1))
      (if (= (length lista) 1)
          (inverso_ (list ) n (Aux lista_ (car lista) (if (= j 0) 0 (+ i 1))) (car lista) (+ j 1))
          (Aux lista_ n (if (= j 0) 0 (+ i 1))))))

;;Aux: agrega los numeros a la lista a partir de un numero limite
;;
;;lista_: lista auxiliar que se guardan los numeros
;;num: numero limite
;;i: numero entero auxiliar
(define (Aux lista_ num i) 
  (cond
    [(= i num) (append empty lista_)]
    [(< i num) (Aux (append lista_ (list i)) num (+ i 1))]))

;(inverso '(1 3 7) 10)
;----------------------------------------------------------------------------------------------------------

(define (umbral_cola lista umbral tipo)
  (if (equal? tipo #\M)
      (mayor_cola lista umbral 0 (list ))
      (menor_cola lista umbral 0 (list ))))

;;mayor_cola: retorna una lista con las posiciones de la lista ingresada que los valores sean mayores a umbral
;;
;;lista: lista que se desea aplicar la funcion
;;umbral: numero que se desea comparar en la lista
;;i: numero entero auxiliar
;;lista_: lista auxiliar que se guardan las posiciones
(define (mayor_cola lista umbral i lista_)
  (if (equal? empty lista)
      (append lista empty)
      (if (> (length lista) 1)
          (if (> (car lista) umbral)
              (mayor_cola (rest lista) umbral (+ i 1) (append lista_ (list i)))
              (mayor_cola (rest lista) umbral (+ i 1) lista_))
          (if (> (car lista) umbral)
              (append lista_ (list i))
              (append lista_ empty)))))

;;menor_cola: retorna una lista con las posiciones de la lista ingresada que los valores sean menores a umbral
;;
;;lista: lista que se desea aplicar la funcion
;;umbral: numero que se desea comparar en la lista
;;i: numero entero auxiliar
;;lista_: lista auxiliar que se guardan las posiciones
(define (menor_cola lista umbral i lista_)
  (if (equal? empty lista)
      (append lista empty)
      (if (> (length lista) 1)
          (if (< (car lista) umbral)
              (menor_cola (rest lista) umbral (+ i 1) (append lista_ (list i)))
              (menor_cola (rest lista) umbral (+ i 1) lista_))
          (if (< (car lista) umbral)
              (append lista_ (list i))
              (append lista_ empty)))))

;(umbral_cola '(15 2 1 3 27 5 10) 5 #\M)
;(umbral_cola '(15 2 1 3 27 5 10) 5 #\m)
;----------------------------------------------------------------------------------------------------------
(define (umbral_simple lista umbral tipo)
  (umbral_simple_ lista umbral tipo 0))

;;umbral_simple_: retorna una lista con las posiciones de la lista ingresada que los valores sean menores o mayores al umbral dependiendo del "tipo" que se ingrese.
;;
;;lista: lista que se desea aplicar la funcion
;;umbral: numero que se desea comparar en la lista
;;tipo: tipo de operacion, si es #\m, se operaran con numeros menores al umbral. Si es #\M, se operaran con numeros mayores al umbral.
;;i: numero entero auxiliar
(define (umbral_simple_ lista umbral tipo i)
  (if (equal? tipo #\M)
      (if (equal? empty lista)
          (append lista empty)
          (if (> (length lista) 1)
              (if (> (car lista) umbral)
                  (append (list i) (umbral_simple_ (rest lista) umbral tipo (+ i 1)))
                  (append (list ) (umbral_simple_ (rest lista) umbral tipo (+ i 1))))
              (if (> (car lista) umbral)
                  (list i)
                  (list ))))
      
      (if (equal? empty lista)
          (append lista empty)
          (if (> (length lista) 1)
              (if (< (car lista) umbral)
                  (append (list i) (umbral_simple_ (rest lista) umbral tipo (+ i 1)))
                  (append (list ) (umbral_simple_ (rest lista) umbral tipo (+ i 1))))
              (if (< (car lista) umbral)
                  (list i)
                  (list ))))))

;(umbral_simple '(15 2 1 3 27 5 10) 5 #\M)
;(umbral_simple '(15 2 1 3 27 5 10) 5 #\m)
;----------------------------------------------------------------------------------------------------------
(define (modsel_cola lista seleccion f)
  (modsel_cola_ lista seleccion f (list ) 0)
  )

;;modsel_cola_: se le aplica la funcion f a los elementos de la lista "lista" que sus indices esten contenidos en la lista "seleccion" a través de un proceso de cola.
;;
;;lista: lista que se desea implementar las funciones
;;seleccion: lista con los respectivos indices de la lista "lista"
;;f: funcion a implementar
;;lista_: lista auxiliar que se guardan los datos
;;i: numero entero auxiliar
(define (modsel_cola_ lista seleccion f lista_ i)
  (if (equal? empty lista)
      (append lista_ empty)
      (if (> (length lista) 1)
          (if (confirmar seleccion i)
              (modsel_cola_ (rest lista) seleccion f (append lista_ (list (f (car lista)))) (+ i 1))
              (modsel_cola_ (rest lista) seleccion f (append lista_ (list (car lista))) (+ i 1)))
          (if (confirmar seleccion i)
              (append lista_ (list (f (car lista))))
              (append lista_ (list (car lista)))))))

;;confirmar: confirma que el numero ingresado esté en la lista ingresada
;;
;;lista: lista con los indices
;;num: indice que se desea confirmar
(define (confirmar lista num)
  (not (boolean? (member num lista))))

;(modsel_cola '(15 2 1 3 27 5 10) '(0 4 6) (lambda (x) (modulo x 2)))
;(modsel_cola '(15 2 1 3 27 5 10) '(3 1 2) (lambda (x) (+ x 5)))
;----------------------------------------------------------------------------------------------------------
(define (modsel_simple lista seleccion f)
  (modsel_simple_ lista seleccion f 0))

;;modsel_simple_: se le aplica la funcion f a los elementos de la lista "lista" que sus indices esten contenidos en la lista "seleccion" a través de un proceso simple.
;;
;;lista: lista que se desea implementar las funciones
;;seleccion: lista con los respectivos indices de la lista "lista"
;;f: funcion a implementar
;;i: numero entero auxiliar
(define (modsel_simple_ lista seleccion f i)
  (if (equal? empty lista)
      (append (list ) empty)
      (if (> (length lista) 1)
          (if (confirmar seleccion i)
              (append (list (f (car lista))) (modsel_simple_ (rest lista) seleccion f (+ i 1)))
              (append (list (car lista)) (modsel_simple_ (rest lista) seleccion f (+ i 1))))
          (if (confirmar seleccion i)
              (list  (f (car lista)))
              (list (car lista))))))

;(modsel_simple '(15 2 1 3 27 5 10) '(0 4 6) (lambda (x) (modulo x 2)))
;(modsel_simple '(15 2 1 3 27 5 10) '(3 1 2) (lambda (x) (+ x 5)))
;----------------------------------------------------------------------------------------------------------
(define (estables lista umbral fM fm)
  (list (estables_FM lista umbral fM) (estables_Fm lista umbral fm)))

;;estables_FM: llama al umbral_mayor con la lista "lista", con la lista que retorna se le aplica la funcion fM, a la lista que retorna se le aplica umbral_mayor y retorna la cantidad de numeros restantes
;;
;;lista: lista que se desea implementar
;;umbral: numero que se desean ver valores mayores
;;fM: funcion que se desea implementar
(define (estables_FM lista umbral fM);fM
  (if (equal? lista empty)
      (0)
      (length (umbral_cola
               (modsel_cola lista (umbral_cola lista umbral #\M) fM)
               umbral
               #\M))))

;;estables_FM: llama al umbral_menor con la lista "lista", con la lista que retorna se le aplica la funcion fm, a la lista que retorna se le aplica umbral_menor y retorna la cantidad de numeros restantes
;;
;;lista: lista que se desea implementar
;;umbral: numero que se desean ver valores menores
;;fm: funcion que se desea implementar
(define (estables_Fm lista umbral fm);fm
  (if (equal? lista empty)
      0
      (length (umbral_cola
               (modsel_cola lista (umbral_cola lista umbral #\m) fm)
               umbral
               #\m))))

;(estables '(15 2 1 3 27 5 10) 5 (lambda (x) (/ x 2)) (lambda (x) (* x 2)))
;----------------------------------------------------------------------------------------------------------

(define (query lista pos op params)
  (query_ lista pos op params 0))

;;query_: dependiendo del op, se puede llamar a la funcion umbral, modsel o estables. Dependiendo de pos se usará la lista que está contenida en "lista". Los params dependen de su operacion.
;;
;;lista: lista de listas que se usará una de estas.
;;pos: posicion de la lista que está contenida en la lista "lista"
;;op: numero entero, el cual dependiendo su valor se hará una accion distinta
;;params: lista de marametros necesarios
;;i: numero entero auxiliar
(define (query_ lista pos op params i)
  (if (= pos i)
      (cond
        [(= op 1) (query_1 (car lista) params)]
        [(= op 2) (query_2 (car lista) params)]
        [(= op 3) (query_3 (car lista) params)])
      (query_ (rest lista) pos op params (+ i 1))))

;;query_1: llama a la funcion umbral
;;
;;lista: lista que se desea implementar
;;params: lista con parametros necesarios para la funcion invocada
(define (query_1 lista params)
  (umbral_cola lista (car params) (last params)))

;;query_2: llama a la funcion modsel
;;
;;lista: lista que se desea implementar
;;params: lista con parametros necesarios para la funcion invocada
(define (query_2 lista params)
  (modsel_cola lista (car params) (eval (last params))))

;;query_3: llama a la funcion estables
;;
;;lista: lista que se desea implementar
;;params: lista con parametros necesarios para la funcion invocada
(define (query_3 lista params)
  (estables lista (car params) (eval (car (rest params))) (eval (last params))))

;(query '((0 1 2 3 4) (4 3 2 1 0) (15 2 1 3 27 5 10)) 1 1 '(1 #\M))
;(query '((0 1 2 3 4) (4 3 2 1 0) (15 2 1 3 27 5 10)) 0 2 '((0 4) (lambda (x) (+ x 100))))
;(query '((0 1 2 3 4) (4 3 2 1 0) (15 2 1 3 27 5 10)) 2 3 '(5 (lambda (x) (/ x 2)) (lambda (x) (* x 2))))