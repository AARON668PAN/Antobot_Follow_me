# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/ruiqi/Desktop/Antobot/devel_isolated/zed_nodelets;/home/ruiqi/Desktop/Antobot/devel_isolated/zed_interfaces;/home/ruiqi/Desktop/Antobot/devel_isolated/vision_yolo;/home/ruiqi/Desktop/Antobot/devel_isolated/joystick_drivers;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_joystick_teleop;/home/ruiqi/Desktop/Antobot/devel_isolated/joy;/home/ruiqi/Desktop/Antobot/devel_isolated/imu_bno055;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_heading;/home/ruiqi/Desktop/Antobot/devel_isolated/geonav_transform;/home/ruiqi/Desktop/Antobot/devel_isolated/ekf_tracker;/home/ruiqi/Desktop/Antobot/devel_isolated/apf_navigator;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_tel_key;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_tel;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_safety;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_navigation;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_base;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_msgs;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_hmi;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_gps;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_gazebo;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_ekf;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_description;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_datamanager;/home/ruiqi/Desktop/Antobot/devel_isolated/antobot_bringup;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/ruiqi/Desktop/Antobot/devel_isolated/zed_ros/env.sh')

output_filename = '/home/ruiqi/Desktop/Antobot/build_isolated/zed_ros/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
