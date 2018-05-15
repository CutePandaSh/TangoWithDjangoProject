# Testing Tools 测试工具

Django为编写单元测试提供了一小组有用的工具。

## The test client 测试客户端

test client 是一个伪浏览器端的Python 类，让你可以通过编程代码的方式来对基于Django开发的应用程序进行视图和交互测试的。

可以通过test client你可以：

- 对URL模拟发送GET或者POST情况，并监控返回响应 Response的所有信息，从HTTP协议的底层（返回数据的header以及状态码）到页面内容。
- 观察重定向链，并且检查每一步的URL和状态码
- 测试指定的请求是否由指定的模版渲染出来的，而且在该模板的上下文中含有特定的值

请注意Django内置的test client，并不是要取代 **Selenium** 等浏览器模拟类型的框架，test client更关注于其他方面的功能，简单来说：

- 使用 test client 来确认请求使用了正确的模板来进行渲染，并且对该模板传入了正确的数据。
- 类似 **Selenium** 的浏览器模拟框架主要用来测试 _渲染_ 以后的HTML页面，以及页面的 _行为_ 情况（即 JavaScript脚本的功能反馈）。当然Django也提供了类似的测试工具，请访问 **LiveServerTestCase**部分来了解更多细节。

需要做综合测试话，应该结合上述两种不同的测试方法，来进行测试工作。

### 概述及快速入门
