(defun make-disc nil
  (let (b1 b2)
    (setq b1 (make-cylinder 100 30))
    (setq b2 (make-cylinder 95 25))
    (setq b1 (body- b1 b2))
    (send b1 :locate #f(0 0 0))
    (send b1 :set-color :white)
    b1))

(defun make-minute-hand nil
  (let (b1 b2)
    (setq b1 (make-cube 10 90 5))
    (send b1 :locate #f(0 40 20))
    (setq b2 (make-cylinder 2 15))
    (send b2 :locate #f(0 0 15))
    (setq b2 (body+ b2 b1))
    (send b2 :set-color :gray20) 
    b2))

(defun make-hour-hand nil
  (let (b1 b2)
    (setq b1 (make-cube 10 50 5))
    (send b1 :locate #f(0 20 10))
    (setq b2 (make-cylinder 2 15))
    (send b2 :locate #f(0 0 0))
    (setq b2 (body+ b2 b1))
    (send b2 :set-color :black)
    b2))

(defclass clock
  :super cascaded-link
  )

(defmethod clock
  (:init ()
	 (let (l1 l2 l3)
	   (send-super :init)

	   (setq l3 (instance bodyset-link :init (make-cascoords)
			      :bodies (list (make-hour-hand))))
	   (setq l2 (instance bodyset-link :init (make-cascoords)
			      :bodies (list (make-minute-hand))))
	   (setq l1 (instance bodyset-link :init (make-cascoords)
			      :bodies (list (make-disc))))
	   (send self :assoc l1)
	   (send l1 :assoc l2)
	   (send l1 :assoc l3)
	   
	   (setq joint-list
		 (list
		  (instance rotational-joint
			    :init :parent-link l1 :child-link l2
			    :axis :z
			    :max 4320 :min 0)
		  (instance rotational-joint
			    :init :parent-link l1 :child-link l3
			    :axis :z
			    :max 360 :min 0)))

	   (setq links (list l1 l2 l3))
	   (send self :init-ending)
	   )))

(setq r (instance clock :init))
(objects (list r))

(dotimes (i (* 360 12))
  (send r :angle-vector (float-vector i (/ i 12)))
					  
  (send *irtviewer* :draw-objects)
  (x::window-main-one))
