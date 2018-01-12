(defun summit (lst)
  (apply #'+ (remove nil lst)))

#|
(remove nil lst)の返り値が(apply #'+ lst)に渡されていない。
|#
