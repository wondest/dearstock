# 开发过程记录

## 开发环境搭建

* Anaconda3 Python3.7 Study
* Eclipse && Pydev
* /home/tender/Workspace/eclipse-workspace/dearbao
* mysql
    root/xieqin#2018#ROOT
    dearAdmin/xieqin#2018#DBA
    dearApp/dear#2018#APP
    
## Github

* 396934200@qq.com Ilovegithub2012

## 工程目录

Foo/
|-- bin/
|   |-- foo
|
|-- foo/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/
|   |-- conf.py
|   |-- abc.rst
|
|-- setup.py
|-- requirements.txt
|-- README

简要解释一下:

    bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
    foo/: 存放项目的所有源代码。(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。(2) 其子目录tests/存放单元测试代码； (3) 程序的入口最好命名为main.py。
    docs/: 存放一些文档。
    setup.py: 安装、部署、打包的脚本。
    requirements.txt: 存放软件依赖的外部Python包列表。
    README: 项目说明文件。