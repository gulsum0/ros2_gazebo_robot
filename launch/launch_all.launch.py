import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_name = 'my_bot'
    
    # 1. Simülasyonu Başlat
    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(pkg_name), 'launch', 'sim.launch.py'
        )])
    )

    # 2. SLAM (Haritalama) - 8 saniye gecikmeli başlasın (Hata vermemesi için)
    slam = TimerAction(
        period=8.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(pkg_name), 'launch', 'slam.launch.py'
                )])
            )
        ]
    )

    # 3. RViz - 10 saniye gecikmeli başlasın
    rviz_config_dir = os.path.join(get_package_share_directory(pkg_name), 'rviz', 'slam.rviz')
    # Not: RViz launch dosyasını daha sonra ekleyebiliriz, şimdilik manuel açacağız.
    
    return LaunchDescription([
        sim,
        slam
    ])
