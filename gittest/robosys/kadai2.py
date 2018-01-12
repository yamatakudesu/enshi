import rospy,actionlib
from move_base_msgs.msg import *        
from opencv_apps.msg import RotatedRectStamped

if __name__ == '__main__':
    try:
        rospy.init_node('client', anonymous=True)
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()
        
        def callback(msg):
            if(msg.rect.center.x != 0 or msg.rect.center.y != 0):
                goal = MoveBaseGoal()
                goal.target_pose.header.stamp = rospy.Time.now()
                goal.target_pose.header.frame_id = "/map"
                goal.target_pose.pose.position.x = 0
                goal.target_pose.pose.position.y = 0
                goal.target_pose.pose.orientation.w = 1
                client.send_goal(goal)
                client.wait_for_result()

        rospy.Subscriber('/camshift/track_box',RotatedRectStamped,callback)        
        rospy.spin()       
    except rospy.ROSInterruptException: pass
