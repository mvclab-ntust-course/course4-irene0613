import cv2
from ultralytics import YOLO

import torch
model = YOLO('yolov8n.pt')

# 使用CPU
device = torch.device('cpu')
model.to(device)

# 加載影片
video_path = 'argoverse.mp4'  
cap = cv2.VideoCapture(video_path)

# 獲取影片的寬度與高度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定義輸出的影片
output_path = 'output_video.mp4'
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 調整圖像大小為 (640, 640)
    resized_frame = cv2.resize(frame, (640, 640))
    
    # 將圖像從 (H, W, C) 轉換為 (C, H, W)
    frame_tensor = torch.from_numpy(resized_frame).permute(2, 0, 1).unsqueeze(0).float()
    
    # 使用YOLOv8模型进行目标检测
    results = model(frame_tensor)
    
    # 遍歷檢測結果
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # 獲取目標類別
            cls = box.cls
            # 獲取類別標籤
            label = model.names[int(cls)]
            
            # 只保留車輛的標籤 
            if label == 'car': 
                # 獲取邊界座標
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # 繪製邊界框 (需要按比例調整座標)
                x1 = int(x1 * frame_width / 640)
                y1 = int(y1 * frame_height / 640)
                x2 = int(x2 * frame_width / 640)
                y2 = int(y2 * frame_height / 640)
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    out.write(frame)
    
    # 視窗顯示內容
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
out.release()
cv2.destroyAllWindows()

