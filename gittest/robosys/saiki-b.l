(defun rec-count-a (lst)
  (if lst
      (+ (if (eql (car lst) 'a)
	     1
	   0)
	 (rec-count-a (cdr lst)))
    0))
