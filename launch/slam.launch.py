import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')

    # SLAM Toolbox'in varsayilan ayar dosyasini buluyoruz
    slam_config_file = os.path.join(
        get_package_share_directory('slam_toolbox'),
        'config',
        'mapper_params_online_async.yaml'
    )

    start_async_slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
          slam_config_file,  # Varsayilan ayarlari yukle
          {'use_sim_time': use_sim_time}, # Simulasyon zamanini kullan
          {'base_frame': 'base_link'}     # <--- KRITIK DUZELTME BURASI
        ]
    )

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(start_async_slam_toolbox_node)

    return ld
