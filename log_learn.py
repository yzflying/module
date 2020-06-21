"""
1. logging.basicConfig(**kwargs)函数：
参数介绍：
filename 	指定日志输出目标文件的文件名，指定该设置项后日志信心就不会被输出到控制台了
filemode 	指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
format 	    指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
datefmt 	指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
level 	    指定日志器的日志级别
stream 	    指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常

logging模块中定义好的可以用于format格式字符串
字段/属性名称 	    使用格式 	            描述
asctime 	        %(asctime)s 	        日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
created 	        %(created)f 	        日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated 	%(relativeCreated)d 	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
msecs 	            %(msecs)d 	            日志事件发生事件的毫秒部分
levelname 	        %(levelname)s 	        该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
levelno 	        %(levelno)s 	        该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
name 	            %(name)s 	            所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message 	        %(message)s 	        日志记录的文本内容，通过 msg % args计算得到的
pathname 	        %(pathname)s 	        调用日志记录函数的源码文件的全路径
filename 	        %(filename)s 	        pathname的文件名部分，包含文件后缀
module 	            %(module)s 	            filename的名称部分，不包含后缀
lineno 	            %(lineno)d 	            调用日志记录函数的源代码所在的行号
funcName 	        %(funcName)s 	        调用日志记录函数的函数名
process 	        %(process)d 	        进程ID
processName 	    %(processName)s 	    进程名称，Python 3.1新增
thread 	            %(thread)d 	            线程ID
threadName 	        %(thread)s          	线程名称

备注：日志器（Logger）是有层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，其名称为'root'，它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的
"""
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


"""
2. logging日志模块四大组件
组件名称 	对应类名 	功能描述
日志器 	    Logger 	提供了应用程序可一直使用的接口
处理器 	    Handler 	将logger创建的日志记录发送到合适的目的输出
过滤器 	    Filter 	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器 	    Formatter 	决定日志记录的最终输出格式

日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
不同的处理器（handler）可以将日志输出到不同的位置；
每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方

Logger类
1) 向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
2）基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
3）将日志消息传送给所有感兴趣的日志handlers
Logger方法 	                                                            描述
Logger.setLevel() 	                            设置日志器将会处理的日志消息的最低严重级别
Logger.addHandler() 和 Logger.removeHandler() 	为该logger对象添加 和 移除一个handler对象
Logger.addFilter() 和 Logger.removeFilter() 	为该logger对象添加 和 移除一个filter对象
logger对象创建日志记录:Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()

Handler类
1）（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）
2）Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象
Handler方法 	                                    描述
logging.StreamHandler 	                    将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
logging.FileHandler 	                    将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
logging.handlers.RotatingFileHandler 	    将日志消息发送到磁盘文件，并支持日志文件按大小切割
logging.handlers.TimedRotatingFileHandler 	将日志消息发送到磁盘文件，并支持日志文件按时间切割
logging.handlers.HTTPHandler 	            将日志消息以GET或POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler 	            将日志消息发送给一个指定的email地址
logging.NullHandler 	                    该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。

Filter类
1）Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。
2）Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤

Formater类
1）Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。
2）另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成

logging日志流处理流程:
1）（在用户代码中进行）日志记录函数调用，如：logger.info(...)，logger.debug(...)等；
2）判断要记录的日志级别是否满足日志器设置的级别要求（要记录的日志级别要大于或等于日志器设置的级别才算满足要求），如果不满足则该日志记录会被丢弃并终止后续的操作，如果满足则继续下一步操作；
3）根据日志记录函数调用时掺入的参数，创建一个日志记录（LogRecord类）对象；
4）判断日志记录器上设置的过滤器是否拒绝这条日志记录，如果日志记录器上的某个过滤器拒绝，则该日志记录会被丢弃并终止后续的操作，如果日志记录器上设置的过滤器不拒绝这条日志记录或者日志记录器上没有设置过滤器则继续下一步操作--将日志记录分别交给该日志器上添加的各个处理器；
5）判断要记录的日志级别是否满足处理器设置的级别要求（要记录的日志级别要大于或等于该处理器设置的日志级别才算满足要求），如果不满足记录将会被该处理器丢弃并终止后续的操作，如果满足则继续下一步操作；
6）判断该处理器上设置的过滤器是否拒绝这条日志记录，如果该处理器上的某个过滤器拒绝，则该日志记录会被当前处理器丢弃并终止后续的操作，如果当前处理器上设置的过滤器不拒绝这条日志记录或当前处理器上没有设置过滤器测继续下一步操作；
7）如果能到这一步，说明这条日志记录经过了层层关卡允许被输出了，此时当前处理器会根据自身被设置的格式器（如果没有设置则使用默认格式）将这条日志记录进行格式化，最后将格式化后的结果输出到指定位置（文件、网络、类文件的Stream等）；
"""
# import logging
# import logging.handlers
# import datetime
#
# logger = logging.getLogger('mylogger')   #创建一个日志器mylogger
# logger.setLevel(logging.DEBUG)
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))   #创建一个处理器rf_handler
# f_handler = logging.FileHandler('error.log')      #创建一个处理器f_handler
# f_handler.setLevel(logging.ERROR)
#
# rf_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")                               #定义一个格式器rf_formatter
# f_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")    #定义一个格式器f_formatter
#
# rf_handler.setFormatter(rf_formatter)
# f_handler.setFormatter(f_formatter)        #为处理器添加格式器输出
#
# logger.addHandler(rf_handler)      #为日志器mylogger添加处理器rf_handler
# logger.addHandler(f_handler)       #为日志器mylogger添加处理器f_handler
#
# # 日志器mylogger的日志创建部分
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')


"""
3. 创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容：配置logging
(日志配置文件见log.conf，配合使用如下代码实现以上代码功能)
"""
import logging
import logging.config
import logging.handlers
import datetime

# 读取日志配置文件内容
logging.config.fileConfig('log.conf')
# #创建一个日志器mylogger
logger = logging.getLogger('mylogger')

# 日志器mylogger的日志创建部分
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

