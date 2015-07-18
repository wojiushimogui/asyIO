#异步IO中协程的理解,以生产消费者为例
#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
#coding:utf-8
def consumer():
	r=''
	while True:
		n=yield r  #consumer通过yield拿到消息，处理，又通过yield把结果传回；
		if not n:
			return 
		print ('[CONSUMER]consuming %s...'%n)
		r='returnConsumer'
def produce(c):
	c.send(None) #启动生成器
	n=0
	while n<10:
		n=n+1
		print('[PRODUCE]:producing %s'%n)
		r=c.send(n)#切换到consumer中去执行
		print('[PRODUCE]consumer return %s'% r)
	c.close()  #通过c.close()关闭consumer，整个过程结束
	
	
c=consumer()
produce(c)
		
		
		
		
	