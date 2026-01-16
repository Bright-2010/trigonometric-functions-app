# trigonometric-functions-app
trigonometric functions app and API

API链接是: https://api.brightweb.top/trig
调用方法：
- 必须通过json方式传送2个值 type和deg
- type为三角函数类型(sin cos tan)
- deg为度数，单位必须是度，否则返回结果会有错误，传入类型应为数字 然后你会收到json响应
- 你会收到此响应 `{'type': 'sin', 'degree': 30, 'radian': 0.5235987755982988, 'result': 0.5}` 就像这样
- type:你的三角函数类型   degree:你的三角函数度数   radian:你的三角函数结果的精确值（由于计算机计数精度问题可能出现极微小误差，不过这可以忽略不计） result: 你的三角函数值，此值完全正确，没有误差，但是可能只能精确到小数点后几位左右

后续我会给这个API增加更多功能，敬请期待！

example.py是调用此API的示范程序，可以作为参考（由于调用API，所以必须联网）

注意：使用示例程序请安装python环境（如没有）和requests模块，命令为`pip install requests` 如果你是Mac `pip3 install requests`,否则程序可能无法执行

## 我已经开源了API服务部分，可以通过node直接启动服务，服务端口在3000，可以进阶使用pm2管理进程

## 我的API服务在2026年1月15日到1月16日期间不可用，因为我要回老家，需要把服务器带回去，17号恢复API，API关闭时使用示例程序可能无法正常工作
