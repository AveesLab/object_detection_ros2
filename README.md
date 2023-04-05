# ROS2 3D bouding box object detection from pointclouds
This is a package for a baseline 3D bounding box detection and tracking using pointcloud data. 

It's based on this package https://github.com/praveen-palanisamy/multiple-object-tracking-lidar

### Design and algorithm

1. Detect from clustering
    Unsupervised euclidean cluster extraction
2. Track
    tracking (object ID & data association) with an ensemble of Kalman Filters
3. Classify static and dynamic object



```
git clone https://github.com/AveesLab/object_detection_ros2.git
```
