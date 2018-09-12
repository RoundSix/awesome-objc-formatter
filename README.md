# awesome-objc-formatter

> 作者: lu.meng <lu.meng@danatech.com>

![awesome-objc-formatter](http://odqo2zgxm.bkt.clouddn.com/awesome-objc-formatter.png)

### 描述
`awesome-objc-formatter`是一款以`clang-format`为基础的`objc`文件
格式整理工具(包含`.h` `.m` `.hh` `.mm`)。如果需要修改format规则的
话，请查看`.clang-format`文件及其配置。

### 使用
本工具使用`python`，需要`python3`环境。

- 将工程拷贝到iOS项目根目录
- 在工程目录执行
```python
python setup.py
```
- 仅检查哪些需要format的文件并输出，默认直接format
```python
python awesome-objc-formatter.py -c
```
- 如果需要操作所有文件，请加-a，否则默认操作svn有修改的objc文件
```python
python awesome-objc-formatter.py -a
```
- 查看帮助信息
```python
python awesome-objc-formatter.py -h | --help
```
- 查看版本信息
```python
python awesome-objc-formatter.py -v | --version
```
- 如果有需要忽略的文件夹，请将文件夹名称添加到
`.formatting-directory-ignore`中，在检查/格式化过程中会自动忽略