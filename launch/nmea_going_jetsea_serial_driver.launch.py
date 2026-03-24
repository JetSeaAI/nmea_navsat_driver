# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" A simple launch file for the nmea_serial_driver node. """


import sys

from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription, LaunchIntrospector, LaunchService
from launch_ros import actions
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    """Generate a launch description for a single serial driver."""
    description_actions = [
    DeclareLaunchArgument(
        'gps_ip',
        default_value='0.0.0.0',
        description='The IP address of the GPS device.'
    ),
    DeclareLaunchArgument(
        'gps_port',
        default_value='5106',
        description='The port number for the GPS device.'
    ),
    DeclareLaunchArgument(
        'frame_id',
        default_value='gps',
        description='The frame ID to use in the GPS messages.'
    ),
    DeclareLaunchArgument(
        'buffer_size',
        default_value='1024',
        description='The buffer size for the GPS messages.'
    ),
    DeclareLaunchArgument(
        'tf_prefix',
        default_value='',
        description='A prefix to add to all TF frames published by the driver.'
    )
]
    driver_node = actions.Node(
        package='nmea_navsat_driver',
        executable='nmea_socket_driver',
        namespace='garmin',
        output='screen',
        name='navsat_garmin_node',
        parameters=[{
            'ip': LaunchConfiguration('gps_ip'),
            'port': LaunchConfiguration('gps_port'),
            'frame_id': LaunchConfiguration('frame_id'),
            'buffer_size': LaunchConfiguration('buffer_size'),
            'tf_prefix': LaunchConfiguration('tf_prefix'),
        }]
    )

    return LaunchDescription(description_actions + [driver_node])


def main(argv):
    ld = generate_launch_description()

    print('Starting introspection of launch description...')
    print('')

    print(LaunchIntrospector().format_launch_description(ld))

    print('')
    print('Starting launch of launch description...')
    print('')

    ls = LaunchService()
    ls.include_launch_description(ld)
    return ls.run()


if __name__ == '__main__':
    main(sys.argv)
