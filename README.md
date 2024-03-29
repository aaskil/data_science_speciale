# data_science_speciale



<!-- ---------------------------------------------------------------------- -->
# BOOKS
[Bradski, G. and Kaehler, A. (2008) Learning OpenCV, Learning OpenCV.](https://www.bogotobogo.com/cplusplus/files/OReilly%20Learning%20OpenCV.pdf)

[Concise Computer Vision An Introduction into Theory and Algorithms](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Concise%20Computer%20Vision_%20An%20Introduction%20into%20Theory%20and%20Algorithms%20%5BKlette%202014-01-20%5D.pdf)

[Davies, R. (2012) Computer and Machine Vision, 4th Edition Theory, Algorithms, Practicalities Opsylum, Zhurnal Eksperimental’noi i Teoreticheskoi Fiziki.](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Computer%20and%20Machine%20Vision_%20Theory%2C%20Algorithms%2C%20Practicalities%20%284th%20ed.%29%20%5BDavies%202012-03-19%5D.pdf)

[Krig, S. (2014) Computer vision metrics: Survey, taxonomy, and analysis, Computer Vision Metrics: Survey, Taxonomy, and Analysis.](http://www.r-5.org/files/books/computers/algo-list/image-processing/vision/Scott_Krig-Computer_Vision_Metrics-EN.pdf)

[Stevens, E. and Antiga, L. (2019) Deep Learning with PyTorch Essential Excerpts, PyTorch.](https://isip.piconepress.com/courses/temple/ece_4822/resources/books/Deep-Learning-with-PyTorch.pdf)

[Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://powerunit-ju.com/wp-content/uploads/2021/04/Aurelien-Geron-Hands-On-Machine-Learning-with-Scikit-Learn-Keras-and-Tensorflow_-Concepts-Tools-and-Techniques-to-Build-Intelligent-Systems-OReilly-Media-2019.pdf)

[Hands-On Computer Vision with TensorFlow 2](https://www.wolf.university/hands-oncomputervisionwithtensorflow2/ebook/hands-oncomputervisionwithtensorflow2.pdf)
- chapter 12, has subsection of disparity, and important point on rectifyity



<!-- ---------------------------------------------------------------------- -->
# Research papers
keywords: 
- "stereo vision" AND "distance estimation" AND "neural networks"
- "instance segmentation" AND "neural networks"
- "bin picking" AND "distance" AND "neural Network"
- "computer vision" AND dataset AND (collect OR gather OR generate)


<!-- ---------------------------------------------------------------------- -->
## 3D-2D extrinsic calibration

[Road is Enough! Extrinsic Calibration of Non-overlapping Stereo Camera and LiDAR using Road Information](https://arxiv.org/pdf/1902.10586.pdf)

[VPFNet: Improving 3D Object Detection with Virtual Point based LiDAR and Stereo Data Fusion](https://arxiv.org/pdf/2111.14382v2.pdf)

[Sparse LiDAR and Stereo Fusion (SLS-Fusion) for Depth Estimation and 3D Object Detection](https://e-archivo.uc3m.es/rest/api/core/bitstreams/918fd989-a44d-4958-9606-88b0982c57ee/content)

[Automatic Calibration of Lidar and Camera Images using Normalized Mutual Information](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=fc08d41be320a827c3f045c4429e13495da5a1cc)

[A 3D-2D Registration Method for Stereo Scan Overlay on Structure from Motion Model](https://www.conferences.com.au/wp-content/uploads/2020/09/75_CameraReady.pdf)    


<!-- ---------------------------------------------------------------------- -->
## point cloud
[Myronenko, A. and Song, X. (2010) ‘Point set registration: Coherent point drifts’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 32(12). Available at: https://doi.org/10.1109/TPAMI.2010.46.](https://arxiv.org/pdf/0905.2635.pdf)

[Yang, J., Li, H. and Jia, Y. (2013) ‘Go-ICP: Solving 3D registration efficiently and globally optimally’, in Proceedings of the IEEE International Conference on Computer Vision. Available at: https://doi.org/10.1109/ICCV.2013.184.](http://users.cecs.anu.edu.au/~hongdong/ICCV13goicp.pdf)


<!-- ---------------------------------------------------------------------- -->
## Domain/Case specific papers on bin picking for data size argument
robot arm used to move single calibration object to 6000 locations in regars to calibration of stereo vision camera. using parallell setup:<br>
[Abdelaal, M. et al. (2021) ‘Uncalibrated stereo vision with deep learning for 6-DOF pose estimation for a robot arm system’, Robotics and Autonomous Systems, 145. Available at: https://doi.org/10.1016/j.robot.2021.103847.](https://www.sciencedirect.com/science/article/pii/S0921889021001329)

590 itemsets(l,r,disparity), 12 workpieces <br>
[Khalid, M.U. et al. (2019) ‘Deep workpiece region segmentation for bin picking’, in IEEE International Conference on Automation Science and Engineering. Available at: https://doi.org/10.1109/COASE.2019.8843050.](https://arxiv.org/pdf/1909.03462.pdf)

153 imagesets, 1 workpiece, maching scope of study<br>
[Davies, R. (2012) Computer and Machine Vision, 4th Edition Theory, Algorithms, Practicalities Opsylum, Zhurnal Eksperimental’noi i Teoreticheskoi Fiziki.](https://www.mdpi.com/1424-8220/19/16/3602)


<!-- ---------------------------------------------------------------------- -->
## Stereo vision camera calibration
[Scharstein, D. and Szeliski, R. (2002) ‘A taxonomy and evaluation of dense two-frame stereo correspondence algorithms’, International Journal of Computer Vision, 47(1–3).](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Scharstein-IJCV02.pdf)

[Sun, J. et al. (2005) ‘Symmetric stereo matching for occlusion handling’, in Proceedings - 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, CVPR 2005. Available at: https://doi.org/10.1109/CVPR.2005.337.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/symmetricstereo_cvpr05.pdf)

Proving the importance of parallel setup:<br>
[Loop, C. and Zhang, Z. (1999) ‘Computing rectifying homographies for stereo vision’, Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 1. Available at: https://doi.org/10.1109/cvpr.1999.786928.](http://dev.ipol.im/~morel/Dossier_MVA_2011_Cours_Transparents_Documents/2011_Cours7_Document2_Loop-Zhang-CVPR1999.pdf)

[Zhang, Z. (1998) ‘Determining the Epipolar Geometry and its Uncertainty: A Review’, International Journal of Computer Vision. Available at: https://doi.org/10.1023/A:1007941100561.](https://www.cs.auckland.ac.nz/courses/compsci773s1c/resources/IJCV-Review.pdf)

[Zhang, Z. (2000) ‘A flexible new technique for camera calibration’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 22(11). Available at: https://doi.org/10.1109/34.888718.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr98-71.pdf)

BOOK<br>
[Hartley, R. and Zisserman, A. (2004) Multiple View Geometry in Computer Vision, Multiple View Geometry in Computer Vision. Available at: https://doi.org/10.1017/cbo9780511811685.](https://github.com/DeepRobot2020/books/blob/master/Multiple%20View%20Geometry%20in%20Computer%20Vision%20(Second%20Edition).pdf)

BOOK cannot find pdf<br>
[Faugeras, O. and Luong, Q.-T. (2018) The Geometry of Multiple Images, The Geometry of Multiple Images. Available at: https://doi.org/10.7551/mitpress/3259.001.0001.](https://mitpress.mit.edu/9780262562041/the-geometry-of-multiple-images/)

testing different baseline distances:<br>
[Setyawan, R.A. et al. (2018) ‘Measurement Accuracy Analysis of Distance between Cameras in Stereo Vision’, in 2018 Electrical Power, Electronics, Communications, Controls and Informatics Seminar, EECCIS 2018. Available at: https://doi.org/10.1109/EECCIS.2018.8692999.](https://ieeexplore-ieee-org.proxy1-bib.sdu.dk/stamp/stamp.jsp?tp=&arnumber=8692999)

[Okutomi, M. and Kanade, T. (1993) ‘A Multiple-Baseline Stereo’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 15(4). Available at: https://doi.org/10.1109/34.206955.](https://www.ri.cmu.edu/pub_files/pub2/okutomi_m_1993_1/okutomi_m_1993_1.pdf)


<!-- ---------------------------------------------------------------------- -->
## Instance segmentation papers

[VISION TRANSFORMER ADAPTER FOR DENSE PREDICTIONS](https://arxiv.org/pdf/2205.08534v4.pdf)(https://github.com/czczup/ViT-Adapter)
[EVA: Exploring the Limits of Masked Visual Representation Learning at Scale](https://arxiv.org/pdf/2211.07636v2.pdf)(https://github.com/baaivision/EVA)

### 2015
Fast R-CNN: <br>
[Girshick, R. (2015) ‘Fast R-CNN’, Proceedings of the IEEE International Conference on Computer Vision, 2015 International Conference on Computer Vision, ICCV 2015, pp. 1440–1448. Available at: https://doi.org/10.1109/ICCV.2015.169.](https://arxiv.org/pdf/1506.01497.pdf)

Fast R-CNN: <br>
[Girshick, R. (2015) ‘Fast R-CNN’, Proceedings of the IEEE International Conference on Computer Vision, 2015 International Conference on Computer Vision, ICCV 2015, pp. 1440–1448. Available at: https://doi.org/10.1109/ICCV.2015.169.](https://arxiv.org/pdf/1504.08083.pdf)

### 2017
FCNN: <br>
[Shelhamer, E., Long, J. and Darrell, T. (2017) ‘Fully Convolutional Networks for Semantic Segmentation’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 39(4). Available at: https://doi.org/10.1109/TPAMI.2016.2572683.](https://arxiv.org/pdf/1411.4038.pdf)

### 2020
Mask R-CNN: <br>
[He, K. et al. (2020) ‘Mask R-CNN’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 42(2). Available at: https://doi.org/10.1109/TPAMI.2018.2844175.](https://openaccess.thecvf.com/content_ICCV_2017/papers/He_Mask_R-CNN_ICCV_2017_paper.pdf)

### 2023
Segment Anything: <br>
[Kirillov, A. et al. (2023) ‘Segment Anything’. Available at: http://arxiv.org/abs/2304.02643.](https://arxiv.org/pdf/2304.02643.pdf)<br>
[- Segment Anything github](https://github.com/facebookresearch/segment-anything)

YOLO review: <br>
[Terven, J. and Cordova-Esparza, D. (2023) ‘A Comprehensive Review of YOLO: From YOLOv1 and Beyond’, pp. 1–36. Available at: http://arxiv.org/abs/2304.00501.](https://arxiv.org/pdf/2304.00501.pdf)

Fast Segment Anything: <br>
[Zhao, X. et al. (2023) ‘Fast Segment Anything’, 2. Available at: http://arxiv.org/abs/2306.12156.](https://arxiv.org/pdf/2306.12156.pdf)<br>
[- Fast Segment Anything github](https://github.com/CASIA-IVA-Lab/FastSAM)

### 2024
YOLOv9: <br>
[Wang, C.-Y., Yeh, I.-H. and Liao, H.-Y.M. (2024) ‘YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information’. Available at: http://arxiv.org/abs/2402.13616.](https://arxiv.org/pdf/2402.13616v1.pdf)
[- YOLOv9 github](https://github.com/WongKinYiu/yolov9)


<!-- ---------------------------------------------------------------------- -->
## Instance segmentation dataset papers
coco dataset:<br>
[Lin, T.Y. et al. (2014) ‘Microsoft COCO: Common objects in context’, in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). Available at: https://doi.org/10.1007/978-3-319-10602-1_48.](https://arxiv.org/pdf/1405.0312.pdf)

LVIS dataset:<br>
[Gupta, A., Dollar, P. and Girshick, R. (2019) ‘Lvis: A dataset for large vocabulary instance segmentation’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2019.00550.](https://arxiv.org/pdf/1908.03195.pdf)

SA-1B dataset, same paper for dataset as the model:<br>
[Kirillov, A. et al. (2023) ‘Segment Anything’. Available at: http://arxiv.org/abs/2304.02643.](https://arxiv.org/pdf/2304.02643.pdf)<br>


<!-- ---------------------------------------------------------------------- -->
## Stereo vision disparity estimation papers
[Gidaris, S. and Komodakis, N. (2017) ‘Detect, replace, refine: Deep structured prediction for pixel wise labeling’, in Proceedings - 30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017.](https://openaccess.thecvf.com/content_cvpr_2017/papers/Gidaris_Detect_Replace_Refine_CVPR_2017_paper.pdf)

[Scharstein, D. and Szeliski, R. (2002) ‘A taxonomy and evaluation of dense two-frame stereo correspondence algorithms’, International Journal of Computer Vision, 47(1–3).](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Scharstein-IJCV02.pdf)

[Zaarane, A. et al. (2020) ‘Distance measurement system for autonomous vehicles using stereo camera’, Array, 5.](https://www.sciencedirect.com/science/article/pii/S2590005620300011)

[Seki, A. and Pollefeys, M. (2016) ‘Patch based confidence prediction for dense disparity map’, in British Machine Vision Conference 2016, BMVC 2016.](https://www.cvlibs.net/projects/autonomous_vision_survey/literature/Seki2016BMVC.pdf)


<!-- ---------------------------------------------------------------------- -->
## litterature review READ THIS
[Lahiri, S., Ren, J. and Lin, X. (2024) ‘Deep Learning-Based Stereopsis and Monocular Depth Estimation Techniques : A Review’, pp. 305–351.](https://www.mdpi.com/2624-8921/6/1/13) <br>
this litterature review, compares CRL, SsMNet, PSMNet, EdgeStereo, HSM, MCV-MFC, HITNet, OptStereo, PVSereo, SMAR-Net, CRAR, ACVNet, iRaftStereo, PCW-Net, CGI-Stereo


<!-- ---------------------------------------------------------------------- -->
## traditional stereo vision papers
the beggining of stereo vision:<br>
[Marr, D. and Poggio, T. (1976) ‘Cooperative computation of stereo disparity’](https://apps.dtic.mil/sti/tr/pdf/ADA030748.pdf)

Cross-based cost aggregation:<br>
[https://ieeexplore-ieee-org.proxy1-bib.sdu.dk/stamp/stamp.jsp?tp=&arnumber=4811952](https://ieeexplore-ieee-org.proxy1-bib.sdu.dk/stamp/stamp.jsp?tp=&arnumber=4811952)


<!-- ---------------------------------------------------------------------- -->
## neural network AND stereo imaging papers
    * mentioned in litterature review

### 2015
*MC-CNN 2016 (maybe first deep learning solution):<br>
[Žbontar, J. and LeCun, Y. (2015) ‘Computing the stereo matching cost with a convolutional neural network’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition.](https://openaccess.thecvf.com/content_cvpr_2015/papers/Zbontar_Computing_the_Stereo_2015_CVPR_paper.pdf)<br>
[- MC-CNN github](https://github.com/jzbontar/mc-cnn)

### 2016
Content-CNN 2016:<br>
[Luo, W., Schwing, A.G. and Urtasun, R. (2016) ‘Efficient deep learning for stereo matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition.](https://www.cs.toronto.edu/~urtasun/publications/luo_etal_cvpr16.pdf)

*MC-CNN-acrt/fast: comparison of different stereo matching algorithms, great explanations:<br>
[Žbontar, J. and LeCun, Y. (2016) ‘Stereo matching by training a convolutional neural network to compare image patches’, Journal of Machine Learning Research, 17.](https://www.jmlr.org/papers/volume17/15-535/15-535.pdf)

### 2017
FlowNet 2.0 2017:<br>
[Ilg, E. et al. (2017) ‘FlowNet 2.0: Evolution of optical flow estimation with deep networks’, in Proceedings - 30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017. Available at: https://doi.org/10.1109/CVPR.2017.179.](https://arxiv.org/pdf/1612.01925.pdf)<br>
[- FlowNet 2.0 github](https://github.com/NVIDIA/flownet2-pytorch)

GC-Net 2017:<br>
[Kendall, A. et al. (2017) ‘End-to-End Learning of Geometry and Context for Deep Stereo Regression’, Proceedings of the IEEE International Conference on Computer Vision, 2017-Octob, pp. 66–75.](https://openaccess.thecvf.com/content_ICCV_2017/papers/Kendall_End-To-End_Learning_of_ICCV_2017_paper.pdf)

[Liu, Y. et al. (2017) ‘Richer Convolutional Features for Edge Detection’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 41(8). Available at: https://doi.org/10.1109/TPAMI.2018.2878849.](https://arxiv.org/pdf/1612.02103.pdf)

*CRL: cascade CNN architecture: 1. initial disparity w/ fine details, 2. refine disparity <br>
[Pang, J. et al. (2017) ‘Cascade Residual Learning: A Two-Stage Convolutional Neural Network for Stereo Matching’, in Proceedings - 2017 IEEE International Conference on Computer Vision Workshops, ICCVW 2017.](https://openaccess.thecvf.com/content_ICCV_2017_workshops/papers/w17/Pang_Cascade_Residual_Learning_ICCV_2017_paper.pdf)

*SGM-Net 2017:<br>
[Seki, A. et al. (2017) ‘SGM-Nets: Semi-global matching with neural networks’, in Proceedings - 30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017.](https://openaccess.thecvf.com/content_cvpr_2017/papers/Seki_SGM-Nets_Semi-Global_Matching_CVPR_2017_paper.pdf)

*SsSMnet 2017<br>
[Zhong, Y., Dai, Y. and Li, H. (2017) ‘Self-Supervised Learning for Stereo Matching with Self-Improving Ability’.](https://arxiv.org/pdf/1709.00930.pdf)

### 2018
*PSMnet 2018 w/github :<br>
[Chang, J.R. and Chen, Y.S. (2018) ‘Pyramid Stereo Matching Network’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2018.00567.](https://arxiv.org/pdf/1803.08669.pdf)<br>
[- PSMnet github](https://github.com/JiaRenChang/PSMNet/tree/master)

*CSPN 2018:<br>
[Cheng, X., Wang, P. and Yang, R. (2020) ‘Learning Depth with Convolutional Spatial Propagation Network’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 42(10). Available at: https://doi.org/10.1109/TPAMI.2019.2947374.](https://arxiv.org/pdf/1810.02695.pdf)<br>
[- CSPN github](https://github.com/XinJCheng/CSPN)

*DispNet 2018:<br>
[Mayer, N. et al. (2018) ‘What Makes Good Synthetic Training Data for Learning Disparity and Optical Flow Estimation?’, International Journal of Computer Vision, 126(9). Available at: https://doi.org/10.1007/s11263-018-1082-6.](https://arxiv.org/pdf/1801.06397.pdf)

### 2019
comparing stereo and mono depth estimation:<br>
[Smolyanskiy, N., Kamenev, A. and Birchfield, S. (2018) ‘On the importance of stereo for accurate depth estimation: An efficient semi-supervised deep neural network approach’, in IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops.](https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w14/Smolyanskiy_On_the_Importance_CVPR_2018_paper.pdf)

*EdgeStereo 2019:<br>
[Song, X. et al. (2019) ‘EdgeStereo: A Context Integrated Residual Pyramid Network for Stereo Matching’, in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). Available at: https://doi.org/10.1007/978-3-030-20873-8_2.](https://www.researchgate.net/publication/323771029_EdgeStereo_A_Context_Integrated_Residual_Pyramid_Network_for_Stereo_Matching)

GWC-Net 2019:<br>
[Guo, X. et al. (2019) ‘Group-wise correlation stereo network’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2019.00339.](https://arxiv.org/abs/1903.04025)

*HSM 2019:<br>
[Yang, G. et al. (2019) ‘Hierarchical deep stereo matching on high-resolution images’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2019.00566.](https://openaccess.thecvf.com/content_CVPR_2019/papers/Yang_Hierarchical_Deep_Stereo_Matching_on_High-Resolution_Images_CVPR_2019_paper.pdf)

*GA-Net 2019:<br>
[Zhang, F. et al. (2019) ‘GA-net: Guided aggregation net for end-to-end stereo matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2019.00027.](https://arxiv.org/pdf/1904.06587.pdf)

### 2020
LEAStereo 2020<br>
[Cheng, X. et al. (2020) ‘Hierarchical neural architecture search for deep stereo matching’, in Advances in Neural Information Processing Systems.](https://proceedings.neurips.cc/paper/2020/file/fc146be0b230d7e0a92e66a6114b840d-Paper.pdf)<br>
[- LEAStereo github](https://github.com/XuelianCheng/LEAStereo)

DSMNet 2020:<br>
[Zhang, F. et al. (2020) ‘Domain-Invariant Stereo Matching Networks’, in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). Available at: https://doi.org/10.1007/978-3-030-58536-5_25.](https://arxiv.org/abs/1911.13287)

time efficient cost volume formulation for nnBased disparity:<br>
[Gu, X. et al. (2020) ‘Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition.](https://arxiv.org/pdf/1912.06378.pdf)

*PCW-Net 2020 w/github:<br>
[Shen, Z. et al. (2020) ‘PCW-Net: Pyramid Combination and Warping Cost Volume for Stereo Matching’, in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics).](https://arxiv.org/pdf/2006.12797.pdf)<br>
[- PCW-Net github](https://github.com/gallenszl/PCWNet)

AANET 2020:<br>
[Xu, H. and Zhang, J. (2020) ‘AANET: Adaptive aggregation network for efficient stereo matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR42600.2020.00203.](https://arxiv.org/pdf/2004.09548.pdf)

MVSNet 2020:<br>
[Zaarane, A. et al. (2020) ‘Distance measurement system for autonomous vehicles using stereo camera’, Array, 5.](https://arxiv.org/pdf/1804.02505.pdf)<br>
[- MVSNet github](https://github.com/YoYo000/MVSNet)

### 2021
*MCV-MFC 2021:<br>
[Liang, Z. et al. (2021) ‘Stereo Matching Using Multi-Level Cost Volume and Multi-Scale Feature Constancy’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 43(1). Available at: https://doi.org/10.1109/TPAMI.2019.2928550.](https://ieeexplore.ieee.org/abstract/document/8765737)

*HITNet 2021:<br>
[Tankovich, V. et al. (2021) ‘HitNet: Hierarchical Iterative Tile Refinement Network for Real-time Stereo Matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR46437.2021.01413.](https://openaccess.thecvf.com/content/CVPR2021/papers/Tankovich_HITNet_Hierarchical_Iterative_Tile_Refinement_Network_for_Real-time_Stereo_Matching_CVPR_2021_paper.pdf)<br>
[- HITNet github](https://github.com/ibaiGorordo/HITNET-Stereo-Depth-estimation)

*OptStereo & PVStereo 2021:<br>
[Wang, H. et al. (2021) ‘PVStereo: Pyramid Voting Module for End-to-End Self-Supervised Stereo Matching’, IEEE Robotics and Automation Letters, 6(3). Available at: https://doi.org/10.1109/LRA.2021.3068108.](https://arxiv.org/pdf/2103.07094.pdf)

SMAR-Net 2021:<br>
[Wang, C. et al. (2021) ‘Self-Supervised Multiscale Adversarial Regression Network for Stereo Disparity Estimation’, IEEE Transactions on Cybernetics, 51(10). Available at: https://doi.org/10.1109/TCYB.2020.2999492.](https://ieeexplore.ieee.org/document/9138704)

### 2022
*iRaftStereo 2022:<br>
[Jiang, H., Xu, R. and Jiang, W. (2022) ‘An Improved RaftStereo Trained with A Mixed Dataset for the Robust Vision Challenge 2022’, pp. 1–9. Available at: http://arxiv.org/abs/2210.12785.](https://arxiv.org/pdf/2210.12785.pdf)

*ACVNet 2022:<br>
[Xu, G. et al. (2022) ‘Attention Concatenation Volume for Accurate and Efficient Stereo Matching’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR52688.2022.01264.](https://arxiv.org/pdf/2203.02146.pdf)

*CRAR 2022:<br>
[Zeng, L. and Tian, X. (2022) ‘CRAR: Accelerating Stereo Matching with Cascaded Residual Regression and Adaptive Refinement’, ACM Transactions on Multimedia Computing, Communications and Applications, 18(3). Available at: https://doi.org/10.1145/3488719.]()

### 2023
*CGI-Stereo 2023:<br>
[Xu, G., Zhou, H. and Yang, X. (2023) ‘CGI-Stereo: Accurate and Real-Time Stereo Matching via Context and Geometry Interaction’. Available at: http://arxiv.org/abs/2301.02789.](https://arxiv.org/pdf/2301.02789.pdf)<br>
[- CGI-Stereo github](https://github.com/gangweiX/CGI-Stereo)

### 2024


<!-- ---------------------------------------------------------------------- -->
## Neural network AND stereo imaging dataset papers
KITTI dataset:<br>
[A., Lenz, P. and Urtasun, R. (2012) ‘Are we ready for autonomous driving? the KITTI vision benchmark suite’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2012.6248074.](https://www.cvlibs.net/publications/Geiger2012CVPR.pdf)

[A. et al. (2013) ‘Vision meets robotics: The KITTI dataset’, International Journal of Robotics Research, 32(11). Available at: https://doi.org/10.1177/0278364913491297.Geiger, ](https://www.cvlibs.net/publications/Geiger2013IJRR.pdf)

[J., Kuhnl, T. and Geiger, A. (2013) ‘A new performance measure and evaluation benchmark for road detection algorithms’, in IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC. Available at: https://doi.org/10.1109/ITSC.2013.6728473.Geiger, ](https://www.cvlibs.net/publications/Fritsch2013ITSC.pdf)

[Menze, M. and Geiger, A. (2015) ‘Object scene flow for autonomous vehicles’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2015.7298925.Fritsch, ](https://www.cvlibs.net/publications/Menze2015CVPR.pdf)



DTU dataset:<br>
[Jensen, R. et al. (2014) ‘Large scale multi-view stereopsis evaluation’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2014.59.](https://backend.orbit.dtu.dk/ws/portalfiles/portal/143897869/hkkr_Large_scale_data_for_multiple_view_stereopsis.pdf)

Sceneflow dataset:<br>
[Mayer, N. et al. (2016) ‘A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation’, in Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition. Available at: https://doi.org/10.1109/CVPR.2016.438.](https://lmb.informatik.uni-freiburg.de/Publications/2016/MIFDB16/paper-MIFDB16.pdf)

[Mayer, N. et al. (2018) ‘What Makes Good Synthetic Training Data for Learning Disparity and Optical Flow Estimation?’, International Journal of Computer Vision, 126(9). Available at: https://doi.org/10.1007/s11263-018-1082-6.](https://arxiv.org/abs/1801.06397)

Middlebury dataset:<br>
[Scharstein, D. et al. (2014) ‘High-resolution stereo datasets with subpixel-accurate ground truth’, in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics). Available at: https://doi.org/10.1007/978-3-319-11752-2_3.](https://elib.dlr.de/90624/1/ScharsteinEtal2014.pdf)


ETH3D dataset:<br>
[Schöps, T. et al. (2017) ‘A multi-view stereo benchmark with high-resolution images and multi-camera videos’, in Proceedings - 30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017. Available at: https://doi.org/10.1109/CVPR.2017.272.]()

<!-- ---------------------------------------------------------------------- -->
## 3D imaging not stereo image papers
[Zhou, C. et al. (2015) ‘Exploiting object similarity in 3D reconstruction’, Proceedings of the IEEE International Conference on Computer Vision, 2015 International Conference on Computer Vision, ICCV 2015, pp. 2201–2209.](https://openaccess.thecvf.com/content_iccv_2015/papers/Zhou_Exploiting_Object_Similarity_ICCV_2015_paper.pdf)


<!-- ---------------------------------------------------------------------- -->
# Lectures
Good explanation of the stereo vision disparity problem lecture 8, 9<br>
[Computer vision 1, Penn State University 2007](https://www.cse.psu.edu/~rtc12/CSE486/)

[Computer Vision, Spring 2017, The Robotics Institute Carnegie Mellon University Logo](https://www.cs.cmu.edu/~16385/s17/)

Lecture 15 on stereo correspondence<br>
[Computer Vision for Visual Effects](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUJlKlt84HFqSWfW36MDd5a)


<!-- ---------------------------------------------------------------------- -->
# Non_research links 
[Nielsen, N. (2020) From Beginner to Expert: How to Master Stereo Vision and Depth Estimation with OpenCV C++ and Python.](https://www.youtube.com/watch?v=KOSS24P3_fY)

[A Deep Learning-Enhanced Stereo Matching Method and Its Application to Bin Picking Problems Involving Tiny Cubic Workpieces](https://www.mdpi.com/2079-9292/12/18/3978)

[STEREO VISION SYSTEM FOR A BIN PICKING ADEPT ROBOT](http://ojie.um.edu.my/index.php/MJCS/article/view/6300)

[towards data science dl for depth esitmation](https://towardsdatascience.com/dl-for-depth-estimation-p2-7cb2c9ff325d)

[stereo_vision_repo_no_neural_network](https://github.com/LearnTechWithUs/Stereo-Vision/blob/master/Main_Stereo_Vision_Prog.py)

[m1 pytorch](https://medium.com/analytics-vidhya/distance-estimation-cf2f2fd709d8)

[Depth Camera - Computerphile](https://www.youtube.com/watch?v=bRkUGqsz6SI)

[Stereo-Vision](https://github.com/LearnTechWithUs/Stereo-Vision)

[Stereo camera for object detection](https://www.youtube.com/watch?v=CAVYHlFGpaw)

[Computer_stereo_vision](https://en.wikipedia.org/wiki/Computer_stereo_vision)

[Epipolar_geometr](https://en.wikipedia.org/wiki/Epipolar_geometry)

[m1 pytorch](https://medium.com/mlearning-ai/mac-m1-m2-gpu-support-in-pytorch-a-step-forward-but-slower-than-conventional-nvidia-gpu-40be9293b898)

[kitti](https://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=stereo)

[learn_open_cv](https://learnopencv.com/disparity-estimation-using-deep-learning/)

[CVFX Lecture 15: Stereo correspondence](https://www.youtube.com/watch?v=kxsvG4sSuvA)


<!-- ---------------------------------------------------------------------- -->
## table model overview
| Model | Year | depth method | network | training method | dataset |
| --- | --- | --- | --- | --- | --- |
