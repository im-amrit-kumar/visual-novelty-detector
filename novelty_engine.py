import cv2, numpy as np, time, csv, os
from detector import YoloDetector
from tracker import CentroidTracker
from novelty_db import SeenObjectDB

class NoveltyEngine:
    def __init__(self, model_path="yolov8n.pt"):
        self.det=YoloDetector(model_path=model_path)
        self.trk=CentroidTracker()
        self.db=SeenObjectDB()
        self.bg=cv2.createBackgroundSubtractorMOG2(history=500,varThreshold=50)
        self.alerts="alerts.csv"
        if not os.path.exists(self.alerts):
            open(self.alerts,"w").write("timestamp,alert_type,object_id,label,details\n")
    def crop(self,f,b):
        x1,y1,x2,y2=b
        return f[max(0,y1):y2,max(0,x1):x2]
    def log(self,t,oid,l,d):
        ts=time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.alerts,"a") as f: f.write(f"{ts},{t},{oid},{l},{d}\n")
        print("ALERT:",ts,t,oid,l,d)
    def analyze_frame(self,frame,zone=None):
        ann=frame.copy(); alerts=[]
        dets=self.det.detect(frame)
        dets=[d for d in dets if d["label"] in ["person","car","truck","bus","motorcycle","bicycle"]]
        rects=[d["xyxy"] for d in dets]
        tracks=self.trk.update(rects)
        for oid,m in tracks.items():
            b=m["bbox"]; x1,y1,x2,y2=b
            cx,cy=(x1+x2)//2,(y1+y2)//2
            lbl="object"
            for d in dets:
                if d["xyxy"]==b: lbl=d["label"]
            crop=self.crop(frame,b)
            seen,mid,c=self.db.is_seen(crop)
            if not seen:
                self.db.add(crop,lbl)
                self.log("new_object",oid,lbl,f"matches={c}")
                alerts.append(("new_object",oid,lbl))
            if zone is not None:
                if cv2.pointPolygonTest(np.array(zone,np.int32),(cx,cy),False)>=0:
                    self.log("restricted_entry",oid,lbl,"inside_zone")
                    alerts.append(("restricted_entry",oid,lbl))
            cv2.rectangle(ann,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(ann,f"ID {oid}",(x1,y1-5),0,0.5,(0,255,0),1)
        return ann,alerts
