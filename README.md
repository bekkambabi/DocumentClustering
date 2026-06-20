# 📄 Document Clustering System

A Machine Learning-based web application that automatically groups similar documents into clusters using the **K-Means Clustering Algorithm**. The project is built with **Python**, **Flask**, and **Scikit-Learn**, providing an intuitive interface for document analysis and unsupervised text classification.

---

## 🚀 Project Overview

Document Clustering is a technique used in Natural Language Processing (NLP) to organize large collections of text documents into meaningful groups based on their content similarity.

This application allows users to upload or input multiple documents, preprocesses the text data, converts it into numerical vectors using TF-IDF, and applies the K-Means clustering algorithm to identify groups of related documents.

---

## ✨ Features

* Upload and analyze text documents
* Text preprocessing and cleaning
* TF-IDF Vectorization
* K-Means Clustering
* Automatic grouping of similar documents
* Cluster visualization and results display
* User-friendly web interface using Flask
* Fast and scalable document organization

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* TF-IDF Vectorizer

### Data Processing

* Pandas
* NumPy
* NLTK

### Frontend

* HTML


### Version Control

* Git
* GitHub

---


```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/bekkambai/document-clustering.git
cd document-clustering
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```


### Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🧠 Working Principle

### 1. Text Preprocessing

* Convert text to lowercase
* Remove punctuation
* Remove stop words
* Tokenization
* Stemming/Lemmatization

### 2. Feature Extraction

The cleaned documents are transformed into numerical vectors using:

```text
TF-IDF (Term Frequency-Inverse Document Frequency)
```

### 3. Clustering

The K-Means algorithm:

* Randomly initializes cluster centroids
* Assigns documents to the nearest centroid
* Recalculates centroids
* Repeats until convergence

### 4. Output

Documents with similar content are grouped into the same cluster.

---

## 📊 Machine Learning Concepts Used

* Unsupervised Learning
* Text Mining
* Natural Language Processing (NLP)
* Feature Engineering
* Vector Space Model
* K-Means Clustering
* Similarity Analysis



## 🎯 Applications

* News Article Classification
* Research Paper Organization
* Document Management Systems
* Search Engine Optimization
* Content Recommendation Systems
* Knowledge Management

---

## 📈 Future Enhancements

* Hierarchical Clustering
* DBSCAN Clustering
* Interactive Cluster Visualization
* Real-time Document Analysis
* Multi-language Support
* Topic Modeling using LDA
* Deployment on Cloud Platforms

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Machine Learning Algorithms
* Unsupervised Learning Techniques
* Natural Language Processing
* Flask Web Development
* Text Vectorization
* Model Integration
* Data Preprocessing
* Git & GitHub Workflow

---

## 👨‍💻 Author

**B S M G Babi**


---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
