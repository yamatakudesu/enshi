(defun make-cylinder1 nil
  (let (b1)
    (setq b1 (make-cylinder 3 60))
    (send b1 :locate #f(0 0 -30))
    (send b1 :set-color :gray80)
    b1))

(defun make-cylinder2 nil
  (let (b1 b2)
    (setq b2 (make-cylinder 6 60))
    (send b2 :locate #f(0 0 -30))
    (setq b1 (make-cylinder 3 60))
    (send b1 :locate #f(0 0 0))
    (setq b2 (body- b2 b1))
    (send b2 :set-color :gray20)
    b2))

(defclass servo-model
  :super cascaded-link
  :slots (h1 s1 j1))
(defmethod servo-model
  (:init ()
	 (let ()
	   (send-super :init)
	   (setq h1 (instance bodyset-link :init (make-cascoords)
			      :bodies (list (make-cylinder2))))
	   (setq s1 (instance bodyset-link :init (make-cascoords)
			      :bodies (list (make-cylinder1))))
	   (setq j1 (instance linear-joint :init
			      :parent-link h1 :child-link s1 :axis :z))
	   (setq links (list h1 s1))
	   (setq joint-list (list j1))
	   (send self :assoc h1)
	   (send h1 :assoc s1)
	   (send self :init-ending)
	   self))
  (:j1 (&rest args) (forward-message-to j1 args))
  )

(setq r (instance servo-model :init))

(objects (list r))
(setq i 0)
(do-until-key
 (send r :angle-vector (float-vector (* 90 (sin (/ i 100.0)))))
 (send *irtviewer* :draw-objects)
 (incf i))
