;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname 1a_boolean_if_expressions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(= 1 1)
(= 2 1)
(> 2 1)

(string=? "foo" "bar")

(define I1 (rectangle 10 20 "solid" "red"))
(define I2 (rectangle 20 10 "solid" "blue"))

I1
I2

(if (< (image-width I2)
       (image-height I2))
    "tall"
    "wide")
;---------------------------
(if (< (image-width I2)
       (image-height I2))
    (image-width I2)
    (image-height I2))
; ----------step_1----------
(if (< 20 10)
    (image-width I2)
    (image-height I2)
    )
; ----------step_2----------
(if false
    (image-width I2)
    (image-height I2)
    )

; ----------step_3----------
   
    (image-height I2)

; ----------step_4----------
   
    10