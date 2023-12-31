import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Hàm để trích chọn đặc trưng MFCC từ tệp âm thanh
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)

# Thư mục chứa dữ liệu giọng nam
male_folder = 'path_to_male_audio_files'
# Thư mục chứa dữ liệu giọng nữ
female_folder = 'path_to_female_audio_files'

# Lấy danh sách tệp giọng nam và giọng nữ
male_files = librosa.util.find_files(male_folder)
female_files = librosa.util.find_files(female_folder)

# Tạo danh sách đặc trưng và nhãn
features = []
labels = []

# Trích chọn đặc trưng từ giọng nam
for file_path in male_files:
    feature = extract_features(file_path)
    features.append(feature)
    labels.append(0)  # 0 đại diện cho giọng nam

# Trích chọn đặc trưng từ giọng nữ
for file_path in female_files:
    feature = extract_features(file_path)
    features.append(feature)
    labels.append(1)  # 1 đại diện cho giọng nữ

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Huấn luyện mô hình KNN
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = knn_model.predict(X_test)

# Đánh giá độ chính xác của mô hình
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
