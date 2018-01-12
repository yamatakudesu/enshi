(defclass 6dof
  :super cascaded-link
  :slots (end-coords l1 l2 l3 l4 l5 l6 l7 j1 j2 j3 j4 j5 j6))
(defmethod 6dof
  (:init
   ()
   (let (b)
     (send-super :init)

     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :white)
     (setq l7 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l7))
     (setq end-coords (make-cascoords :pos #f(0 0 20)))
     (send l7 :assoc end-coords)

     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :blue)
     (setq l6 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l6))
     (send l6 :assoc l7)

     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :green)
     (setq l5 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l5))
     (send l5 :assoc l6)

     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :yellow)
     (setq l4 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l4))
     (send l4 :assoc l5)

     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :orange)
     (setq l3 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l3))
     (send l3 :assoc l4)
     
     (setq b (make-cube 10 10 10))
     (send b :locate #f(0 0 5))
     (send b :set-color :red)
     (setq l2 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l2))
     (send l2 :assoc l3)
     
     (setq b (body+ (make-cube 10 10 10 :pos #f(0 0 5)) (make-cube 300 300 2)))
     (send b :set-color :white)
     (setq l1 (instance bodyset-link :init (make-cascoords)
			:bodies (list b) :name 'l1))
     (send l1 :assoc l2)
     
     (send l2 :locate #f(0 0 10))
     (send l3 :locate #f(0 0 10))
     (send l4 :locate #f(0 0 10))
     (send l5 :locate #f(0 0 10))
     (send l6 :locate #f(0 0 10))
     (send l7 :locate #f(0 0 10))
     
     (setq j1 (instance rotational-joint :init :name 'j1
			:parent-link l1 :child-link l2 :axis :z :min -150 :max 150)
	   j2 (instance rotational-joint :init :name 'j2
			:parent-link l2 :child-link l3 :axis :y :min -150 :max 150)
	   j3 (instance rotational-joint :init :name 'j3
			:parent-link l3 :child-link l4 :axis :x :min -150 :max 150)
	   j4 (instance rotational-joint :init :name 'j4
			:parent-link l4 :child-link l5 :axis :z :min -150 :max 150)
	   j5 (instance rotational-joint :init :name 'j5
			:parent-link l5 :child-link l6 :axis :y :min -150 :max 150)
	   j6 (instance rotational-joint :init :name 'j6
			:parent-link l6 :child-link l7 :axis :x :min -150 :max 150))
	   
     ;;
     (setq links (list l1 l2 l3 l4 l5 l6 l7))
     (setq joint-list (list j1 j2 j3 j4 j5 j6))
     (send self :init-ending)
     self))
  (:end-coords (&rest args) (forward-message-to end-coords args))
  )

(setq r (instance 6dof :init))
(objects (list r (send r :end-coords)))
(setq rotation-axis :x)
(setq translation-axis t)

(dotimes (i 2000)
  (setq c (make-cascoords :pos (float-vector (* 50 (sin (/ i 100.0))) (* 50 (cos (/ i 100.0))) 150)))
  (send r :inverse-kinematics c
	:link-list (send r :link-list (send r :end-coords :parent))
	:move-target (send r :end-coords)
	:translation-axis translation-axis
	:rotation-axis rotation-axis
	:revert-if-fail nil
	:cog-null-space t)
  (x::window-main-one)
  (send *irtviewer* :draw-objects :flush nil)
(send c :draw-on :flush t)
  )
