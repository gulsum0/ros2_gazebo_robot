# ROS 2 Differential Drive Robot

**(Türkçe ve İngilizce açıklama aşağıdadır / Turkish and English descriptions are below)**

---

## 🇹🇷 Türkçe

### Proje Hakkında
Bu proje, **ROS 2 Humble** ve **Gazebo** kullanılarak geliştirilmiş diferansiyel sürüşlü (iki tekerlekli + sarhoş tekerlek) bir mobil robot simülasyonudur.

**Özellikler:**
* URDF ve Xacro ile robot modellemesi.
* Gazebo fizik simülasyonu entegrasyonu.
* `teleop_twist_keyboard` ile klavye kontrolü.
* RViz2 üzerinde görselleştirme.

### Kurulum ve Derleme
Bu projeyi çalıştırmak için bilgisayarınızda ROS 2 Humble yüklü olmalıdır.

1.  Bir workspace oluşturun ve `src` klasörüne gidin:
    ```bash
    mkdir -p ~/robot_ws/src
    cd ~/robot_ws/src
    ```
2.  Bu depoyu klonlayın:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/my_bot_ros2.git](https://github.com/KULLANICI_ADIN/my_bot_ros2.git)
    ```
3.  Derleyin:
    ```bash
    cd ~/robot_ws
    colcon build
    source install/setup.bash
    ```

### Çalıştırma

**1. Simülasyonu Başlatma (Gazebo & Robot):**
```bash
ros2 launch my_bot sim.launch.py








## 🇬🇧 English

### About the Project
This project is a **differential drive** mobile robot simulation (two wheels + caster wheel) developed using **ROS 2 Humble** and **Gazebo**.

**Features:**
* Robot modeling with URDF and Xacro.
* Gazebo physics simulation integration.
* Keyboard control via `teleop_twist_keyboard`.
* Visualization on RViz2.

### Installation and Build
**ROS 2 Humble** is required to run this project.

1.  Create a workspace and navigate to the `src` directory:
    ```bash
    mkdir -p ~/robot_ws/src
    cd ~/robot_ws/src
    ```

2.  Clone this repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/my_bot_ros2.git](https://github.com/YOUR_USERNAME/my_bot_ros2.git)
    ```

3.  Build the package:
    ```bash
    cd ~/robot_ws
    colcon build
    source install/setup.bash
    ```

### Usage

**1. Launching the Simulation (Gazebo & Robot):**
```bash
ros2 launch my_bot sim.launch.py


