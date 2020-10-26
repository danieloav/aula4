import rospy
from std_msgs.msg import String


rospy.init_node('node1')
resposta = '...'
def recebe_volta(msg_volta):
    global resposta
    resposta = msg_volta.data
def timerCallBack(event):
    print(resposta)
    msg = String()
    msg.data = '30550'
    pub.publish(msg)
pub = rospy.Publisher('/topico1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)
sub = rospy.Subscriber('/topico2', String, recebe_volta)

rospy.spin()