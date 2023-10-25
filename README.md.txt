**Real-time GNSS Data Acquisition and Analysis using ROS**


In this project, I implemented a comprehensive system to acquire and analyze data from a GNSS (Global Navigation Satellite System) puck using the Robot Operating System (ROS). The system encapsulates the following key features:

1. **GNSS Puck Initialization**: Successfully connected and set up the USB-based GNSS puck on a computing environment, ensuring its seamless operation with tools like `minicom`.

2. **Custom ROS Device Driver**: Designed and developed a ROS-based device driver to effectively read and process the `$GPGGA` GNSS messages. The driver:
   - Extracts vital navigation details, including latitude, longitude, and altitude.
   - Converts these geodetic coordinates to the UTM (Universal Transverse Mercator) coordinate system.
   - Produces a custom ROS message encompassing the parsed GNSS data and other associated details.

3. **Robust Data Collection**:
   - Stationary Data Collection: Captured GNSS data when the device was stationary, offering insights into the GNSS system's behavior during inactivity.
   - Dynamic Data Collection: Recorded GNSS data during movement, shedding light on how the system perceives and processes motion-based changes.

4. **In-depth Data Analysis**:
   - Stationary Data Insights: Scrutinized the stationary GNSS data, deriving conclusions about the inherent error distributions, their potential sources, and possible error bounds.
   - Movement Data Insights: Analyzed the motion-based GNSS data, determining how the system's error perceptions change based on movement and identifying the inherent noise distribution.

5. **Documentation**: Prepared a detailed report encapsulating all findings, buttressed by well-labeled plots, charts, and inferential remarks.

6. **Repository Organization**: Maintained a clean and structured repository layout, facilitating easy access and understanding of the project components, including the device driver, data analysis scripts, data files, and the comprehensive report.

This project, rooted in ROS, offers invaluable insights into the functioning of GNSS systems, especially in the realms of robotics navigation and outdoor positioning. Through hands-on experience, I gained a deeper understanding of GNSS data intricacies and the potential applications and limitations of such systems in real-world scenarios.