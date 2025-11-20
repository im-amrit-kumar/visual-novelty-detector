import numpy as np
from scipy.spatial import distance as dist
import time
class CentroidTracker:
    def __init__(self, max_disappeared=30, max_distance=60):
        self.nextObjectID=0
        self.objects={}
        self.disappeared={}
        self.metadata={}
        self.max_disappeared=max_disappeared
        self.max_distance=max_distance
    def register(self, centroid, bbox):
        oid=self.nextObjectID
        self.objects[oid]=centroid
        self.disappeared[oid]=0
        self.metadata[oid]={"bbox":bbox,"first_seen":time.time(),"last_seen":time.time(),"centroid_history":[centroid]}
        self.nextObjectID+=1
        return oid
    def deregister(self, oid):
        del self.objects[oid]; del self.disappeared[oid]; del self.metadata[oid]
    def update(self, rects):
        if len(rects)==0:
            for oid in list(self.disappeared.keys()):
                self.disappeared[oid]+=1
                if self.disappeared[oid]>self.max_disappeared: self.deregister(oid)
            return self.metadata
        input_centroids=np.zeros((len(rects),2),dtype="int")
        for i,(x1,y1,x2,y2) in enumerate(rects):
            input_centroids[i]=(int((x1+x2)/2),int((y1+y2)/2))
        if len(self.objects)==0:
            for i in range(len(input_centroids)):
                self.register(tuple(input_centroids[i]), rects[i])
        else:
            objectIDs=list(self.objects.keys())
            objectCentroids=list(self.objects.values())
            D=dist.cdist(np.array(objectCentroids),input_centroids)
            rows=D.min(axis=1).argsort()
            cols=D.argmin(axis=1)[rows]
            usedRows=set(); usedCols=set()
            for (row,col) in zip(rows,cols):
                if row in usedRows or col in usedCols: continue
                if D[row,col]>self.max_distance: continue
                oid=objectIDs[row]
                self.objects[oid]=tuple(input_centroids[col])
                self.disappeared[oid]=0
                self.metadata[oid]["bbox"]=rects[col]
                self.metadata[oid]["last_seen"]=time.time()
                self.metadata[oid]["centroid_history"].append(tuple(input_centroids[col]))
                usedRows.add(row); usedCols.add(col)
            unusedRows=set(range(D.shape[0])).difference(usedRows)
            for row in unusedRows:
                oid=objectIDs[row]
                self.disappeared[oid]+=1
                if self.disappeared[oid]>self.max_disappeared: self.deregister(oid)
            unusedCols=set(range(D.shape[1])).difference(usedCols)
            for col in unusedCols: self.register(tuple(input_centroids[col]), rects[col])
        return self.metadata
