'''
Object Detection : computer vision technique to identify and locate objects within images and videos.
-> techs used :
    - Mediapipe
    - OpenCV
    - Yolov8
    - Detectron2
    - AWS rekognition
    etc...., 

-> Input : image
-> Output :
    - Bounding Box 
    - Confidence Score
    - Object Category
    - Format : [x1, y1, x2, y2, conf-score,class_name]


-> Object Detection Metrics :
    
    -> Fundamental (data is perfect)
        - Many Samples
        - Equally Distributed
        - Perfect Annotations

        -> Training :
            - Loss function : 
                - related to learning process
                - lower is better
        
        -> Evaluation :
            - IoU :
                - Detection Accuracy
                - Ranges between 0 and 1
                - Higher is better
                - Area of Overlap / Area of Union
            
            - mAP :
                - based on precision recall curve
                - curve is based on IoU and detection confidence score
                - Recall : how effectively we can find objects
                - Precision : how well we perform once we find an object
                - Higher is better
    
    -> Advanced (data is imperfect)
        - Not enough samples
        - Unbalanced dataset
        - Imperfect annatation
        
        













'''

