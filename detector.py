from ultralytics import YOLO
import numpy as np
class YoloDetector:
    def __init__(self, model_path="yolov8n.pt", device="cpu", conf=0.35):
        self.model = YOLO(model_path)
        self.model.overrides = {"conf": conf}
    def detect(self, frame):
        results = self.model(frame, verbose=False)
        dets = []
        r = results[0]
        if r.boxes is None: return dets
        boxes = r.boxes.xyxy.cpu().numpy()
        scores = r.boxes.conf.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy().astype(int)
        for (xyxy, score, cls) in zip(boxes, scores, classes):
            x1,y1,x2,y2 = [int(x) for x in xyxy]
            label = r.names[cls] if hasattr(r,'names') else str(cls)
            dets.append({"xyxy":(x1,y1,x2,y2),"conf":float(score),"cls":int(cls),"label":label})
        return dets
