import rospy
from std_msgs.msg import String


rospy.init_node('node2')
matricula='0'
def trataDados(dados):
    global matricula
    matricula = dados.data
sub = rospy.Subscriber('/topico1', String, trataDados)
def timerCallBack(event):
    print("matricula: " + matricula)
    soma = 0
    for numero in matricula:
        soma +=int(numero)
    print("soma: " + str(soma))
    msg = String()
    msg.data = str(soma)
    pub.publish(msg)
pub = rospy.Publisher('/topico2', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()