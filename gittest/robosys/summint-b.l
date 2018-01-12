(defun summit (lst)
  (if lst
      (+ (or (car lst) 0) (summit (cdr lst)))
    0))
