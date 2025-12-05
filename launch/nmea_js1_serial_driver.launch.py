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
        'port',
        default_value='/dev/ttyS0',
        description='The serial port to which the GPS is connected.'
    ),
    DeclareLaunchArgument(
        'baud',
        default_value='38400',
        description='The baud rate for the serial connection.'
    ),
    DeclareLaunchArgument(
        'frame_id',
        default_value='gps',
        description='The frame ID to use in the GPS messages.'
    ),
    DeclareLaunchArgument(
        'time_ref_source',
        default_value='gps',
        description='The time reference source for the GPS messages.'
    ),
    DeclareLaunchArgument(
        'useRMC',
        default_value='False',
        description='Whether to use RMC sentences for navigation data.'
    ),
]
    driver_node = actions.Node(
        package='nmea_navsat_driver',
        executable='nmea_serial_driver',
        namespace='garmin',
        output='screen',
        parameters=[{
            'port': LaunchConfiguration('port'),
            'baud': LaunchConfiguration('baud'),
            'frame_id': LaunchConfiguration('frame_id'),
            'time_ref_source': LaunchConfiguration('time_ref_source'),
            'useRMC': LaunchConfiguration('useRMC')
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
