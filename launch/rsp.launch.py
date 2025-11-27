import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # 1. Dosya yollarini ayarla
    pkg_name = 'my_bot'
    file_subpath = 'urdf/robot.urdf.xacro'

    # Xacro dosyasinin tam yolunu bul
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)

    # 2. Xacro dosyasini isle (XML formatina cevir)
    doc = xacro.process_file(xacro_file)
    robot_description_config = doc.toxml()

    # 3. Parametreleri ayarla
    use_sim_time = LaunchConfiguration('use_sim_time')

    # 4. Node'u olustur
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config, 'use_sim_time': use_sim_time}]
    )

    # 5. Launch tanimini dondur
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Simülasyon zamani kullanilsin mi?'),
        node_robot_state_publisher
    ])
