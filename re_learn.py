import re


# search方法；入参pattern, string, flags=0；扫描string，找到匹配样式pattern的第一个位置，并返回一个相应的匹配对象(匹配的位置范围、匹配的子字符串)
n = re.search('([A-Za-z])(\d)[a-zA-Z]+', '0a3Bg4g9')
print(n)
print(n.group(2))  # 匹配的子字符串(pattern有俩括号，故group有俩参数，即1、2)
print(n.span(2))  # 匹配的位置范围(同上)


# match方法；入参pattern, string, flags=0 ;如果string开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的 匹配对象(匹配的位置范围、匹配的子字符串)
n = re.match('[A-Za-z]+', 'a3Bg4g9')


# fullmatch方法；入参pattern, string, flags=0 ;如果整个 string 匹配到正则表达式样式，就返回一个相应的 匹配对象(匹配的位置范围、匹配的子字符串),否则None
n = re.fullmatch('[A-Za-z]+', '0a3Bg4g9')


# split方法；入参pattern, string, maxsplit=0, flags=0；用pattern匹配来分割字符串string，返回分割后的子字符串列表
n = re.split('[A-Za-z]+', '0a3Bgg9', flags=re.IGNORECASE)


# findall方法；入参pattern, string, flags=0；返回string中能匹配上pattern的子字符串列表
n = re.findall('[A-Za-z]+', '0a3Bg4g9')


# sub方法；入参pattern, repl, string, count=0, flags=0；使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串，返回替换后的字符串，count为最大替换次数
n = re.sub(r'AND', '&', 'Baked Beans And Spam And Bob', flags=re.IGNORECASE)


# subn方法；同sub，只是返回元组：（被替换后的字符串，替换次数）
n = re.subn(r'AND', '&', 'Baked Beans And Spam And Bob', flags=re.IGNORECASE)


"""
1、字符组
在同一个位置可能出现的各种字符组成了一个字符组，在正则表达式中用[]表示
正则          待匹配字符   匹配结果        说明
[0123456789]    8           True	    在一个字符组里枚举合法的所有字符，字符组里的任意一个字符和"待匹配字符"相同都视为可以匹配
[0123456789]    a           False	    由于字符组中没有"a"字符，所以不能匹配
[0-9]           7           True	    也可以用-表示范围,[0-9]就和[0123456789]是一个意思
[a-z]           s           True	    同样的如果要匹配所有的小写字母，直接用[a-z]就可以表示 
[A-Z]           B           True	    [A-Z]就表示所有的大写字母
[0-9a-fA-F]     e           True	    可以匹配数字，大小写形式的a～f，用来验证十六进制字符
"""

"""
2、字符  
元字符     匹配内容
. 	    匹配除换行符以外的任意字符
\w	    匹配字母或数字或下划线
\s	    匹配任意的空白符
\d	    匹配数字
\n	    匹配一个换行符
^	    匹配字符串的开始
$	    匹配字符串的结尾
\W	    匹配非字母或数字或下划线
\D	    匹配非数字
\S	    匹配非空白符
a|b	    匹配字符a或字符b
()	    匹配括号内的表达式，也表示一个组
"""

"""
3、量词
量词	用法说明
*	    重复零次或更多次
+	    重复一次或更多次
?	    重复零次或一次
{n} 	重复n次
{n,}	重复n次或更多次
{n,m}	重复n到m次
"""

"""
（二）正则表达式的使用
1、"^ "、"$"
正则  待匹配字符   匹配结果        说明
a.	    abacad	    ab ac ad	匹配所有"a."的字符
^a.	    abacad	    ab	        只从开头匹配"a."
a.$	    abacad	    ad	        只匹配结尾的"a.$"

2、* + ? { }
正则	待匹配字符	匹配结果	说明
a.?	    abefacgad	ab ac ad    ?表示重复零次或一次，即只匹配"a"后面一个任意字符。
a.*	    abefacgad	abefacgad	*表示重复零次或多次，即匹配"a"后面0或多个任意字符。
a.+	    abefacgad	abefacgad	+表示重复一次或多次，即只匹配"a"后面1个或多个任意字符。
a.{1,2}	abefacgad	abe acg ad	{1,2}匹配1到2次任意字符。

注意：前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配

正则	待匹配字符	匹配结果	说明
a.*?	abefacgad	a a	        惰性匹配

3、字符集［］［^］
正则          待匹配字符           匹配结果            说明 
a[befcgd]*      abefacgad       abef acg ad     表示匹配"a"后面[befcgd]的字符任意次
a[^f]*	        abefacgad	    abe acg ad	    表示匹配一个不是"f"的字符任意次
[\d]	        412a3bc	        4 1 2 3	        表示匹配任意一个数字，匹配到4个结果
[\d]+	        412a3bc	        412 3	        表示匹配任意个数字，匹配到2个结果


6、贪婪匹配
贪婪匹配：在满足匹配时，匹配尽可能长的字符串，默认情况下，采用贪婪匹配
加上？为将贪婪匹配模式转为非贪婪匹配模式，会匹配尽量短的字符串
几个常用的非贪婪匹配Pattern
*? 重复任意次，但尽可能少重复
+? 重复1次或更多次，但尽可能少重复
?? 重复0次或1次，但尽可能少重复
{n,m}? 重复n到m次，但尽可能少重复
{n,}? 重复n次以上，但尽可能少重复
.*?的用法
. 是任意字符
* 是取 0 至 无限长度
? 是非贪婪模式。
合在一起就是 取尽量少的任意字符，一般不会这么单独写，他大多用在：
.*?x就是取前面任意长度的字符，直到一个x出现

常用11正则表达式匹配：
1、Email地址：[a-zA-Z0-9_-]+@([a-zA-Z0-9_-]+\.)+[a-zA-Z0-9_-]+
[a-zA-Z0-9_-]+表示基本ym(域名)，邮箱为ym@ym.ym.ym
2、InternetURL：[a-zA-z]+://[^\s]* 或 https?://([\w-]+\.)+[\w-]+
3、手机号码：      1[3-9]\d{9}
4、电话号码("XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXX-XXXXXXX"、"XXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX)：(\d{3,4}-)?\d{7,8}
5、身份证号(15位、18位数字)，最后一位是校验位，可能为数字或字符X：((\d{14})|(\d{17}))[\d|X]
6、帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)：[a-Za-Z]\w{4,15}
7、强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在 8-10 之间)：
(?=.*[A-Z]) 是正则表达式的环视，表示必须满足“在此位置后为 .*[A-Z]）”才能匹配成功。意思是，匹配成功的表达式必须满足：存在大写字母。因为 [A-Z] 前为. * 。所以字母前可以存在任何字符; 注意：环视不消耗正则的匹配字符.
(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10} 
8、强密码(必须包含大小写字母和数字的组合，可以使用特殊字符，长度在8-10之间)： (?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}
9、一年的12个月(01～09和1～12)：(0?[1-9])|(1[0-2])
10、一个月的31天(01～09和1～31)： (0?[1-9])|([1-2]\d)|(3[0-1])  
11、IP地址： “\d|([1-9]\d)|(1\d{2})|(2[0-4]\d)|(25[0-5])  重复4次
\d|([1-9]\d)|(1\d{2})可写成[0-1]?\d{1,2}


"""