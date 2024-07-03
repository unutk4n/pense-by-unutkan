

# CONFIGURING ENVIRONMENT

this is the most important note because it's the first course.

Workspace is a ROS term for the location on your system where you're developing with ROS2.
The core ROS2 workspace is called the underlay.

In every new shell you use or start using you have to run this command

"""
-# Replace ".bash" with your shell if you're not using bash
-# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/jazzy/setup.bash
"""

If you don't want to type this command above everytime you open a new terminal you can automate the process with : 
"""
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
"""

With this command you can find the configs about ROS2:
"""
printenv | grep -i ROS
"""

The ROS_DOMAIN_ID variable

The reason for the ID is that you need to have a connection between things and without this number you won't be able to connect properly (Between 0- 101)
to have more information about this topic : https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Domain-ID.html

Once you determined the number you can set it with the following command:
export ROS_DOMAIN_ID=<your_domain_id>

To maintain this setting between shell sessions, you can type the following command: 
echo "export ROS_DOMAIN_ID=<your_domain_id>" >> ~/.bashrc


The ROS_AUTOMATIC_DISCOVERY_RANGE variable

By default, the communication is not limited to localhost. ROS_AUTOMATIC_DISCOVERY_RANGE environment variable allows you to limit ROS 2 discovery range. This setting is usefull in some cases; like classrooms where multiple robots may working.
For further information check: https://docs.ros.org/en/jazzy/Tutorials/Advanced/Improved-Dynamic-Discovery.html#improveddynamicdiscovery



source: https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html

# USING "turtlesim", "ros2", and "rqt"

## Before starting 
    Turtlesim >> it's a lightweight simulator for beginners. It gives you an idea what ros does.
    ros2 >> it's a tool for user manages, introspects and interacts with ROS system.
    rqt >> it's the graphical user interface for ros. You can do everyting on the command-line as well but rqt being user-friendly makes it charming.


Don't forget that everytime you open a shell or terminal you have to type the previous commands.
to install turtlesim:
sudo apt install ros-jazzy-turtlesim

to check if it's installed :
ros2 pkg executables turtlesim # you should see a few lines of list

start turtlesim:
ros2 run turtlesim turtlesim_node # this will create a window with a turtle in it.

On another terminal type:
ros2 run turtlesim turtle_teleop_key # this command will allow you to control the turte

to install rqt: 
sudo apt install '~nros-jazzy-rqt*'

to run:
rqt # this will open a GUI

When running rqt for the first time, the window will be blank. No worries; just select Plugins > Services > Service Caller from the menu bar at the top.

just some walkthrough:
click on spawn to create another turtle.
NOTE: on the services option, click on the one you want to then edit the properties about the selection then call the service. that's the way.


Now let’s give turtle1 a unique pen using the /set_pen service:
the options named r, g, and b stand for the classic RGB colors.

after configuring the properties call the service and you'll see that the line that turtle creates changed it's color.

In order to control the other turtle you have to open another terminal and type:
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel


https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html

burada kaldik


