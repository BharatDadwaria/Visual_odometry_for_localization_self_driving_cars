# Visual_odometry_for_localizing_self_driving_cars_using_single_monoculer_camera
The goal of this project was to localizing the location of the self driving cars or any mobile vehicle and estimating their trajectory based on a single monoculer camera. In order to done this project, Trajectory of the self driving car was estimated based on the camera pose estimation in the consecutive frames.

<p align="center">
  <img 
    width="300"
    height="300"
    src="https://raw.githubusercontent.com/BharatDadwaria/Visual_odometry_for_localization_self_driving_cars/main/vehicle_trajectory.PNG"
  >
</p>


## Visual Odometry

* Estimation of the pose of the camera based on the motion information of the consecutive images. 
* Computes camera path incrementally - Pose after pose 
* Visual odometry works as detecting, tracking the feature maps of each of the frames and tracking them into consecutive frames. 
* VSLAM is also a kind of visual odometry with having some extra attributes such as loop closure and global optimization.

    * Image sequence ==> Feature Detection ==> Feature Matching & Tracking ==> Motion Estimation ==> Local Optimization
    
* Actual engineering behind the Feature matching and tracking is based on the projection. The solution can be seen as determination of transformation that minimizes reprojection error of the triangulated point each image.
* Triangulation is the process of measuring the same feature movement in the another frames. 
* This can be done using Essential Matrix.

### Fundamental and Essential Matrix
* Essential Matrix is a matrix related to stereo camera's corresponding points assuming that the camera satisfy the pinhole camera model for calibrated camera.
* Fundamental matrix is used for uncalibrated camera.
* These matrix contains the all information about the relative orientation from corrosponding points.
* Both matrices are homogenius matrix 3x3 having ranks of 2. 
* The rank fo these matrix used for formulaiting "Coplanarity constraint" as

&nbsp; $ x'^{T} F x''=0 $ &nbsp;where x' is the points of image 1, x'' are the points in the image 2 and F is Coplanarity constraint.

* Considering F or E as unknown, we can build sstem of linear equation and come up with homogeneous system.
* Coplanarity constraint of observed points lead to $ Af=0$ &nbsp; that can be solved through SVD.
* This can be done using 8-point algorithm (given 8 points, we can estimate F).
* Once we have F or E, then we can decompose into B (Baseline vector) and R (Rotation matrix which can tell us how camera 2 oriented with respect to camera 1.
* We can locate whete camera 2 is w.r.t. camera 1 but cant identify how far it is => Scale ambiguity.
* Knowing F or E, substantially helps us to reduce the our search for corrosponding point in the other image.
* E matrix have 5-DoF and F-matrix have 7-DoF (It contains calbration parameters information too). 
