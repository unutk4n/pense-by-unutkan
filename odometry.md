# Odometry
eng>> tr : odometry = odometri ( pozisyon degisikligi belirleme)

Basicly Odometry is the use of data from motion sensors to estimate change in position over time.
Temelde Odometri, zaman icerisinde degisen konumun hareket sensorleri ile bulunup kullanilmasidir.

source: https://en.wikipedia.org/wiki/Odometry#:~:text=Odometry%20is%20the%20use%20of,change%20in%20position%20over%20time.


## Computing Odometry for wheeled mobile robots

Odometry a.k.a. dead reckoning is based on the principle that the distance a wheeled robot travels can be determined by measuring the rotation of it's wheels. By measuring the rotational movement of each wheel and applying kinematic equations, it's possible to estimate the robot's change in position and oriation. Odometry is crucial in scenarios where external positioning systems are unavailable -like GPS-


### Tools for computing odometry
To compute odometry, the robot is equipped with wheel encoders, which are sensors that record the rotation of each wheel. These encoders provide precise measurements of the wheel rotations, allowing for precise estimation of the robot's movement.

There are several types of wheel encoders commonly used in robotics:

- Optical Encoders.
- Magnetic Encoders.
- Capacitive Encoders.
- Inductive Encoders.
- Hall Effect Encoders.
- Optical Quadrature Encoders.
- Incremental Encoders.
- Resolvers.
- Rotary Encoders.
- Linear Encoders.

The most common type of encoder used in robotics and automation applications is the Optical Encoder. Optical encoders are widely popular due to their accuracy, reliability, and versatility. They can provide both incremental and absolute position feedback, making them suitable for various tasks.


## Challenges and limitations.

While odometry is a valuable method for estimating a wheeled mobile robot’s position and orientation, it’s essential to be aware of its inherent challenges and limitations. These factors can affect the accuracy of odometry-based localization and navigation.

- Wheel Slip
- Wheel Wear: As a robot’s wheels wear out over time, the circumference may change slightly.
- Sensor Noise: Odometry is highly sensitive to sensor noise, especially in low-cost wheeled robots
- Lack of Global Information: Odometry provides a relative estimate of robot motion but does not consider global information or external landmarks
- External Disturbances: External factors such as bumps, vibrations, or pushes can disrupt odometry calculations.
- Calibration Requirements: Maintaining accurate odometry often requires regular calibration of sensors and wheels
- Computational Load: Real-time odometry calculations can be computationally intensive, depending on the complexity of the robot’s movements and sensor setup. 


Despite these challenges, odometry remains a valueable tool for robotics, especially for short-term, indoor applications. Overcoming these limitations often involves using complementary sensor data, advanced filtering techniques, and considering the specific operational environment to enhance odometry's performance.


Bensel not: hesaplamalar zart zurt iyi hos guzel de, diyelim ki tekerlekler pati cekiyor bunu da hesaplama yetkinligine sahip olacak mi sistem?


source : https://kshitijtiwari.com/all-resources/mobile-robots/odometry/#:~:text=To%20compute%20odometry%2C%20the%20robot,estimation%20of%20the%20robot's%20movement.



## Visual Odometry for UAVs - unmaned aerial vehicles-




source : https://www.uavnavigation.com/company/blog/visual-odometry#:~:text=Visual%20odometry%20is%20based%20on,position%20in%20three%2Ddimensional%20space.