#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():


    return LaunchDescription([

        Node(
            package='laser_filters',
            executable='scan_to_scan_filter_chain',
            name='laser_filter_node',
            parameters=[
                PathJoinSubstitution([
                    get_package_share_directory("laser_filters"),
                    "config", "laserfilter_box.yaml",
                ])],

        )
       
    ])

