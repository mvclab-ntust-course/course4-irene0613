# Week 4  
## Homework 1 - 車子的物件追蹤  
透過yolov8做車子的物件追蹤  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/car_tracking_demo.png" width="500px"><br>  

## Homework 2 - 利用 roboflow 的資料集訓練 yolov8n 模型  
本次作業主要是按照[How to Train YOLOv8 Object Detection on a Custom Dataset](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=oe9vkEvFABbN)完成的  
  
### Dataset  
由於學校的機器學習課程有類似的作業，其資料集我是放在[Roboflow](https://roboflow.com/)來使用，因此本作業的資料集我是使用自行創建的PCB Defects classification  
* 資料集內容：PCB Defects  
* 資料集目的：自動光學檢測 (AOI) 是一種自動化的視覺檢測技術，應用於印刷電路板 (PCB)（或液晶顯示器、晶體管）的製造過程中。該技術利用攝像機自主掃描被測設備，以檢測嚴重故障（如缺少元件、鼠咬痕跡、開路）和品質缺陷。本資料集適用於探測缺陷並分類缺陷屬於哪種類別。
* 標籤：missing_hole、mouse_bite、open_circuit、short、spur、spurious_copper (共六個)  
* 本資料集的創建步驟  
  * 首先上傳同名稱的圖片與XML檔  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/1.png" width="500px"><br>
  * 根據需求劃分資料集  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/2.png" width="500px"><br>
  * 資料上傳結束後選擇要做的data preprocessing，在這部分我選擇了轉正與調整大小  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/3.png" width="500px"><br>
  * 選擇需要的資料加強，在這部分我使用了 Flip 的技術來增強資料，其方式是增加水平翻轉的圖片來改善模型對主體方向不敏感的問題  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/4.png" width="500px"><br>
  * 設定都好了之後按create  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/5.png" width="500px"><br>
  * 點擊Export Dataset並選擇我們需要的Format後，點擊show download code並複製程式碼到Colab的code中  
  <img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/6.png" width="500px"><br>
  
### Code & Result  
* 將資料集換成我們自己創建的資料集，將yolo train的部分修改成以下程式碼後執行  
```
!yolo task=detect mode=train model=yolov8n.pt data={dataset.location}/data.yaml epochs=25 imgsz=640 plots=True
```  
<img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/7.png" width="500px"><br>
* 訓練完後會產生best.pt，其模型結果如下  
<img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/8.png" width="500px"><br>
* 以下為預測結果  
<img src="https://github.com/mvclab-ntust-course/course4-irene0613/blob/main/image/9.jpg" width="500px"><br>
