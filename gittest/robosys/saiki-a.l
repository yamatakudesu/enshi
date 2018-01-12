(defun rec-period (n)
  (if (> n 0)
      (progn
	(format t ".")
	(rec-period (- n 1)))))
