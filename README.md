# id-card
在Windows环境下，创建Python虚拟环境是一种良好的实践，它可以帮助您在项目之间隔离依赖项和包。以下是在Windows上使用命令行创建Python虚拟环境的步骤：

### 步骤 1: 安装 Python

确保您已经在系统上安装了Python。如果没有安装，请先从 [Python官方网站](https://www.python.org/downloads/) 下载并安装最新的Python版本。

### 步骤 2: 打开命令提示符

按下 `Win + R` 键，输入 `cmd` 并按回车，以打开命令提示符。

### 步骤 3: 定位到项目目录

使用 `cd` 命令切换到您项目的目录。例如：

```bash
cd path\\to\\your\\project

```

### 步骤 4: 创建虚拟环境

在项目目录中运行以下命令来创建虚拟环境：

```bash
python -m venv venv

```

这里 `venv` 是虚拟环境的名称，您可以根据需要自定义。

### 步骤 5: 激活虚拟环境

在命令提示符中运行以下命令以激活虚拟环境：

```bash
source  venv\\Scripts\\activate

```

激活后，命令提示符的前缀会变成虚拟环境的名称，表示虚拟环境已成功激活。

### 步骤 6: 安装依赖项

在虚拟环境激活状态下，您可以使用 `pip` 安装项目所需的依赖项：

```bash
pip install package_name

```



### 广播的执行命令是：
```
python -m pip install Django

python manage.py runserver 0.0.0.0:8000 

pip install -r requirements.txt

idCard/settings.py  // 这个路径里面有的 url路径要改成本机， 限制可以访问的服务器
```