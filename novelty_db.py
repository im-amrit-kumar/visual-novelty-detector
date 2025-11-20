import cv2, numpy as np, pickle, os
class SeenObjectDB:
    def __init__(self, db_path="seen_db.pkl", match_threshold=20):
        self.orb=cv2.ORB_create(nfeatures=500)
        self.matcher=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.db_path=db_path; self.match_threshold=match_threshold
        self.entries=[]; self.next_id=0
        if os.path.exists(db_path):
            try: self._load()
            except: pass
    def _save(self):
        with open(self.db_path,"wb") as f: pickle.dump((self.next_id,self.entries),f)
    def _load(self):
        with open(self.db_path,"rb") as f: self.next_id,self.entries=pickle.load(f)
    def _desc(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return self.orb.detectAndCompute(gray,None)[1]
    def is_seen(self,img):
        desc=self._desc(img)
        if desc is None or not self.entries: return (False,None,0)
        best=None; bestc=0
        for e in self.entries:
            try:
                m=self.matcher.match(desc,e["desc"])
                good=[x for x in m if x.distance<60]
                if len(good)>bestc: bestc=len(good); best=e
            except: continue
        if bestc>=self.match_threshold: return (True,best["id"],bestc)
        return (False,None,bestc)
    def add(self,img,label=""):
        desc=self._desc(img)
        if desc is None: return None
        e={"id":self.next_id,"desc":desc,"label":label}
        self.entries.append(e); self.next_id+=1; self._save()
        return e["id"]
