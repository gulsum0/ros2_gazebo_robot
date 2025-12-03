import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name='my_bot'

    # 1. Robot State Publisher (RSP)
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 2. Dunya Dosyasi Yolu (obstacle.world)
    world_path = os.path.join(get_package_share_directory(package_name), 'worlds', 'obstacle.world')

    # 3. Gazebo'yu Baslat
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                    launch_arguments={'world': world_path}.items()
             )

    # 4. Robotu Spawn Et (Dogur)
    # x=0, y=0 : Odanin merkezi
    # z=0.5 : Yarim metre yukaridan birak (Sikismamasi icin)
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot',
                                   '-x', '0.0',
                                   '-y', '0.0',
                                   '-z', '0.5'],
                        output='screen')

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])
