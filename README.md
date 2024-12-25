# Melanoma Classification Project

## Table of Content
- [Deskripsi](#deskripsi)
- [Dataset](#dataset)
- [Langkah Instalasi](#langkah-instalasi)
- [Deskripsi Model](#deskripsi-model)
  - [MobileNetV2](#mobilenetv2)
  - [CNN](#cnn)
- [Hasil dan Analisis](#hasil-dan-analisis)
- [Link Live Demo](#link-live-demo)
- [Author](#author)

## Deskripsi 
Melanoma adalah salah satu jenis kanker kulit yang sangat berbahaya dan dapat menyebabkan kematian jika tidak terdeteksi secara dini, bahkan menyumbang hingga 75% dari total kematian akibat kanker kulit. Oleh karena itu, diperlukan solusi yang dapat membantu proses diagnosis secara lebih efisien. 

Proyek ini bertujuan untuk mengembangkan sebuah sistem berbasis teknologi _Convolutional Neural Network_ (CNN) dan _MobileNetV2_ untuk mendeteksi melanoma melalui analisis citra kulit. Dengan adanya sistem ini, diharapkan dapat mengurangi beban kerja manual para dermatolog, sekaligus membantu klinisi dan masyarakat umum mengenali tanda-tanda kanker kulit secara lebih cepat dan akurat, sehingga penanganan dapat dilakukan lebih awal untuk menyelamatkan nyawa.

## Dataset
Dataset ini diambil dari **ISIC (_International Skin Image Collaboration_) Archive**, yang terdiri dari:
- **5352 gambar benign** (jinak).
- **5353 gambar malignant** (ganas).

Semua gambar diubah ukurannya menjadi resolusi rendah (224x224x3) dalam format RGB. Dataset ini seimbang antara kedua kelas, sehingga metrik **accuracy** dapat digunakan untuk evaluasi performa model.

[Link Dataset: Melanoma Skin Cancer Dataset](https://www.kaggle.com/datasets/hasnainjaved/melanoma-skin-cancer-dataset-of-10000-images/code)

---

## Langkah Instalasi
<details>
<summary>Details</summary>
<ol>
  <li>**Clone repository**:
    <pre><code>git clone https://github.com/Jasm1nPtr/Melanoma-Classification.git</code></pre>
  </li>
  <li>**Buat virtual environment (opsional)**:
    <pre><code>python -m venv env<br>source env/bin/activate (Mac/Linux)<br>env\Scripts\activate (Windows)</code></pre>
  </li>
  <li>**Install dependencies**:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>**Jalankan aplikasi Streamlit**:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>
</details>

---

## Deskripsi Model

### MobileNetV2
<details>
<summary>Details</summary>

**MobileNetV2** adalah model deep learning ringan berbasis Convolutional Neural Network (CNN). Model ini dirancang untuk efisiensi pada perangkat dengan sumber daya terbatas. MobileNetV2 menggunakan pendekatan _depthwise separable convolutions_ untuk mengurangi jumlah parameter tanpa mengorbankan performa.

#### Komponen Utama:
- **MobileNetV2 (Pre-trained)**: 
  - Digunakan sebagai _feature extractor_.
  - Pre-trained pada dataset ImageNet.
  - _Frozen_ untuk mengurangi waktu pelatihan.
- **Batch Normalization**: Menormalkan output untuk mempercepat konvergensi.
- **Dense Layers**: 
  - Dense (512 neurons) dengan aktivasi ReLU.
  - Dropout (0.5) untuk regularisasi.
- **Output Layer**: 
  - Softmax untuk klasifikasi ke dua kelas: benign dan malignant.

#### Proses Model:
- **Data Augmentation**: Teknik augmentasi gambar (rotasi, zoom, flipping).
- **Optimizer**: Adam dengan learning rate 1e-4.
- **Loss Function**: Categorical crossentropy untuk klasifikasi multi-kelas.
</details>

### CNN
<details>
<summary>Details</summary>

**Convolutional Neural Network (CNN)** adalah arsitektur deep learning yang dirancang untuk menangani data berbasis citra. CNN digunakan untuk mengekstraksi fitur spasial dari gambar dan telah banyak digunakan dalam tugas klasifikasi gambar.

#### Komponen Utama:
- **Lapisan Convolutional**:
  - Conv2D (32 filters): Menggunakan filter 3x3 dengan aktivasi ReLU.
  - MaxPooling2D: Pooling ukuran 2x2 untuk mengurangi dimensi fitur.
  - Dropout (0.2): Regularisasi untuk menghindari overfitting.
- **Lapisan Convolutional Kedua**:
  - Conv2D (64 filters): Filter 3x3 dengan aktivasi ReLU.
  - MaxPooling2D: Pooling ukuran 2x2.
  - Dropout (0.3): Regularisasi tambahan.
- **Lapisan Fully Connected**:
  - Flatten: Mengubah fitur dua dimensi menjadi vektor satu dimensi.
  - Dense (128 neurons): Fully connected layer dengan aktivasi ReLU.
  - Dropout (0.5): Regularisasi tambahan.
- **Output Layer**:
  - Dense (2 neurons): Softmax untuk klasifikasi ke dua kelas.

#### Proses Model:
- **Data Augmentation**: Rotasi, zoom, flipping, shear, dan rescale.
- **Optimizer**: Adam.
- **Loss Function**: Categorical crossentropy.
</details>

---

## Hasil dan Analisis

#### MobileNetV2
Model MobileNetV2 dan CNN diuji untuk mendeteksi melanoma dan mengklasifikasikannya menjadi dua kelas: benign (jinak) dan malignant (ganas). Berikut adalah hasil perbandingan performa kedua model:

| MobileNetV2 | Precision    | Recall |  F1-Score |
|-------------|--------------|--------|-----------|
| benign      | 82%          | 93%    | 87%       |           
| malignant   | 92%          | 80%    | 85%       |
| accuracy    |                         86%       |

Learning Curve: 
<img width="504" alt="Screenshot 2024-12-26 at 03 48 02" src="https://github.com/user-attachments/assets/477acdb4-cd45-43ab-baa1-09e215f7db25" />
<img width="503" alt="Screenshot 2024-12-26 at 03 48 26" src="https://github.com/user-attachments/assets/41635714-199c-4bfa-ae0f-3f56cd23e37b" />

#### CNN
Model CNN dirancang untuk mendeteksi melanoma dan mengklasifikasikannya menjadi dua kelas: **benign** (jinak) dan **malignant** (ganas). Dengan arsitektur sederhana namun efektif, model CNN ini memberikan hasil prediksi sebagai berikut:

| MobileNetV2 | Precision    | Recall |  F1-Score |
|-------------|--------------|--------|-----------|
| benign      | 88%          | 92%    | 90%       |           
| malignant   | 91%          | 87%    | 89%       |
| accuracy    |                         89%       |

Learning Curve:

<img width="661" alt="Screenshot 2024-12-26 at 03 46 02" src="https://github.com/user-attachments/assets/ca228040-b542-495a-9c99-11aff9c20b36" />

### Analisis
- **MobileNetV2** memberikan performa lebih baik dalam mendeteksi kelas benign, dengan precision mencapai 88% dan recall 93%. Namun, recall untuk kelas malignant lebih rendah (80%), sehingga beberapa kasus malignant tidak terdeteksi.
- **CNN** CNN memiliki arsitektur sederhana namun memberikan hasil yang kompetitif, dengan akurasi total lebih tinggi (89%). Model ini juga lebih seimbang dalam mendeteksi kedua kelas, dengan recall malignant mencapai 87%

---

## Link Live Demo
Aplikasi web ini telah di-deploy dan dapat diakses melalui tautan berikut:

[Live Demo Aplikasi Melanoma Detection](https://your-live-demo-link.com)

---

## Author
Proyek ini dikembangkan oleh [Jasm1nPtr](https://github.com/Jasm1nPtr).
