februar 12. 
- try to understand cost volume
    - [PCW-Net: Pyramid Combination and Warping Cost Volume for Stereo Matching](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136920280.pdf?fbclid=IwAR1Jf6T8083eKrVd9HBSJO58xv1jI1to0puJ6w7bAdhz_3cUXs2acpH8JcY)
    - [Pyramid Stereo Matching Network](https://arxiv.org/pdf/1803.08669.pdf)
    - [Pyramid Stereo Matching Network](https://github.com/JiaRenChang/PSMNet/tree/master)
    - cost volume is something beeing minimized for optimal pixel matching, for which the disparity map is calculated
    - [Cascade Cost Volume for High-Resolution Multi-View Stereo and Stereo Matching](https://arxiv.org/pdf/1912.06378.pdf)
- written to Christian

februar 12.
- hjemme kontor
- fundet meget litteratur, opdateret readme med masser af kilder. fundet litterature review fra januar 2024

februar 13.
- skolen kort dag. begynt at læse litteratur review

februar 14.
- hjemme kontror, fortsætter læsning af litteratur review

februar 15.
- hovedbiblioteket
- begynt at skrive teori afsnit
- forsøgt at få CGI-CNN til at køre


- forsøgt at få CGI-CNN til at køre

februar 19.
- fået CGI-net op at køre. problem med gpu og 'mps'
- fået SAM op at køre

februar 20.
- trænet CGI-net, 5 epoker, 20 samples
- litteratur review på object segmentation
    - segmentation ikke detection
    - instance segmentation ikke semantic segmentation eller panoptic segmentation

februar 21.
- Jonas
    - Arbejdet på YOLOv8 modellen. Har prøvet at få den til at - træne dog uden held.
    - Oprettet kode til at udtrække masks i png og json format til at generere data.
    - Har genereret preliminary dataset som jeg vil prøve at træne på.
    - https://roboflow.com/models/instance-segmentation Her findes state-of-the-art og most commonly used modeller til instance segmentation, samt guides mm. Roboflow can ligeledes bruges til at generere dataset, lave augmentation og generere test/train/validation sets.

    