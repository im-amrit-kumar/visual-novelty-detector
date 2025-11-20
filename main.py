import cv2, argparse
from novelty_engine import NoveltyEngine

def parse_zone(s):
    if not s: return None
    pts=[]
    for p in s.split(";"):
        x,y=p.split(",")
        pts.append((int(x),int(y)))
    return pts

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="0")
    ap.add_argument("--model",default="yolov8n.pt")
    ap.add_argument("--zone",default=None)
    a=ap.parse_args()

    cap=cv2.VideoCapture(0 if a.source=="0" else a.source)
    eng=NoveltyEngine(model_path=a.model)
    zone=parse_zone(a.zone)

    while True:
        ok,f=cap.read()
        if not ok: break
        ann,_=eng.analyze_frame(f,zone)
        cv2.imshow("Novelty Detector",ann)
        if cv2.waitKey(1)&0xFF==ord('q'): break
    cap.release()
    cv2.destroyAllWindows()
