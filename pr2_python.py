from ultralytics import YOLO

# Load a model
model = YOLO("yolov8l.pt")

if __name__ == '__main__':
    # Use the model
    results = model.train(data="data.yaml", epochs=30)  # train the model
    results = model.val()  # evaluate model performance on the validation set

    # Use model inferencing on test dataset, save results with confidence scores
    testing = model.predict(source='datasets/test/images', save_txt=True, save_conf=True, conf=0.5)

