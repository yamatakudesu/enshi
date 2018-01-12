(defun summit (lst)
  (if lst
      (+ (or (car lst) 0) (summit (cdr lst)))
    0))

#|
空リストでの考慮が抜けている
|#
