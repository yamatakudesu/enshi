(defun iter-count-a (lst)
  (do ((newlst lst (cdr newlst))
       (n 0 (+ n (if (eql (car newlst) 'a)
		     1
		   0))))
      ((not newlst) n)))
