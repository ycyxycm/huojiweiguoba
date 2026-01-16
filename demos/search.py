from huojiweiguoba.lbw_pscript import RabbitMQ, PsdTask, ResultFormat, ScriptType

rabbitmq1 = RabbitMQ("卢本伟9")
data=rabbitmq1.get_queue_info()
print(data)