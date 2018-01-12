(defclass rat
  :super propertied-object
  :slots (numer denom))

(defmethod rat
  (:init (&optional n d)
	 (send self :set-n n)
	 (send self :set-d d)
	 self)
  (:print-info () (format t "answer = ~A/~A~%" numer denom))

  (:set-n (n) (setq numer n))
  (:set-d (d) (setq denom d))
  (:get-n () numer)
  (:get-d () denom)
  (:add-rat (x y) (setq result (instance rat :init
					 (+ (* (send x :get-n) (send y :get-d))
					    (* (send x :get-d) (send y :get-n)))
					 (* (send x :get-d) (send y :get-d))))
	    result))


(setq one-half (instance rat :init))
(setq one-third (instance rat :init))
(send one-half :set-n 1)
(send one-half :set-d 2)
(send one-third :set-n 1)
(send one-third :set-d 3)
(setq l (instance rat :init))
(send l :add-rat one-half one-third)
(send result :get-n)
(send result :get-d)
(send result :print-info)
