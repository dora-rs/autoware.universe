# autoware.universe

<details>
<summary>中文</summary>

dora NDT module first version.  This code has to be dora V0.3.2+

**目录说明**：在“~”目录下存放dora 及 autoware.universe文件夹

​                     在 dora_project目录下安装dora运行文件

# 1  安装dora V0.3.2

## 1.1 安装依赖项
```bash
sudo apt  install cargo clang
pip install dora-rs==0.3.2
```
## 1.2 安装 dora V0.3.2   
参考连接：https://blog.csdn.net/crp997576280/article/details/135368894（Dora-rs 机器人框架学习教程（1）—— Dora-rs安装）

```bash
mkdir dora_project && cd dora_project

export DORA_VERSION=v0.3.2 # Check for the latest release
export ARCHITECTURE=$(uname -m)
wget https://github.com/dora-rs/dora/releases/download/${DORA_VERSION}/dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip
unzip dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip
pip install dora-rs==${DORA_VERSION} ## For Python API
export PATH=$PATH:$(pwd) >> ~/.bashrc
dora --help
```

完成上述步骤后把 PATH=$PATH:/home/xxx/dora_project  (例如：PATH="$PATH:/home/crp/dora_project" )加入到 .bashrc中最后一行


## 1.3下载 dora 源码       

原文链接： https://blog.csdn.net/weixin_44112228/article/details/135607575 （Dora-rs 机器人框架学习教程（2）——从零开始编译C++节点）


```bash
cd ~
git clone https://github.com/dora-rs/dora.git
cd dora/examples/c++-dataflow
cargo run --example cxx-dataflow  # compile C++ node
cargo build -p dora-node-api-c --release  # compile dora-node-api-c 

cd ../c++-ros2-dataflow
source /opt/ros/galactic/setup.bash
cargo run --example cxx-ros2-dataflow --features ros2-examples
```
# 2.下载 dora autoware.universe

下载autoware dora分支

```bash
cd ~
git clone -b  feature/autoware_dora https://github.com/ShoreFlower/autoware.universe.git
```

</details>

<details>
<summary>English</summary>

## Welcome to Dora Autoware

This project use DORA as the middleware for autoware.universe. Currently it support a few robot platform. The simulator is still in progress.

dora NDT module first version.  This code has to be dora V0.3.2+


# 1  Install dora V0.3.2

## 1.1 Dependencies
```bash
sudo apt  install cargo clang
pip install dora-rs==0.3.2
```
## 1.2 Install  dora V0.3.2   

```bash
mkdir dora_project && cd dora_project

export DORA_VERSION=v0.3.2 # Check for the latest release
export ARCHITECTURE=$(uname -m)
wget https://github.com/dora-rs/dora/releases/download/${DORA_VERSION}/dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip
unzip dora-${DORA_VERSION}-${ARCHITECTURE}-Linux.zip
pip install dora-rs==${DORA_VERSION} ## For Python API
export PATH=$PATH:$(pwd) >> ~/.bashrc
dora --help
```

After completing the above steps, add PATH=$PATH:/home/xxx/dora_project (for example: PATH="$PATH:/home/crp/dora_project") to the last line of .bashrc


## 1.3 Download dora source code       

Link： https://blog.csdn.net/weixin_44112228/article/details/135607575 


```bash
cd ~
git clone https://github.com/dora-rs/dora.git
cd dora/examples/c++-dataflow
cargo run --example cxx-dataflow  # compile C++ node
cargo build -p dora-node-api-c --release  # compile dora-node-api-c 

cd ../c++-ros2-dataflow
source /opt/ros/galactic/setup.bash
cargo run --example cxx-ros2-dataflow --features ros2-examples
```
# 2.Download dora autoware.universe

Download autoware from main branch

```bash
cd ~
git clone https://github.com/ShoreFlower/autoware.universe.git
```

</details>

