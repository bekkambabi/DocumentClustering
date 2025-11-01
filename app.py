from flask import Flask, request, render_template_string
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from collections import defaultdict

app = Flask(__name__)

# Load the Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Professional HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Clustering</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            margin: 0;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding: 40px;
        }
        .container {
            background: #ffffff15;
            backdrop-filter: blur(10px);
            padding: 30px 40px;
            border-radius: 20px;
            width: 700px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
            font-size: 26px;
            letter-spacing: 1px;
            color: #f5f5f5;
        }
        label {
            font-weight: 500;
            display: block;
            margin-bottom: 8px;
            color: #e0e0e0;
        }
        textarea {
            width: 100%;
            height: 150px;
            border-radius: 10px;
            border: none;
            padding: 12px;
            font-size: 15px;
            resize: none;
            background: #ffffff25;
            color: #fff;
        }
        input[type=number] {
            width: 80px;
            border: none;
            border-radius: 8px;
            padding: 6px;
            text-align: center;
            background: #ffffff25;
            color: #fff;
        }
        button {
            background: #00c6ff;
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
            transition: 0.3s ease;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 10px #00c6ff;
        }
        .cluster-box {
            background: #ffffff20;
            border-radius: 12px;
            padding: 15px;
            margin-top: 25px;
        }
        .cluster-title {
            font-size: 18px;
            font-weight: bold;
            color: #ffcc70;
            margin-bottom: 10px;
        }
        .doc {
            background: #ffffff10;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 6px;
            color: #e8e8e8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Document Clustering</h1>
        <form method="POST">
            <label>Enter your documents (one per line):</label>
            <textarea name="documents" placeholder="Enter each document on a new line...">{{ docs or '' }}</textarea><br><br>
            <label>Number of Clusters:</label>
            <input type="number" name="num_clusters" value="{{ num_clusters or 3 }}" min="1" required>
            <br><br>
            <div style="text-align:center;">
                <button type="submit">🔍 Cluster Documents</button>
            </div>
        </form>

        {% if grouped %}
            <h2 style="margin-top:30px;text-align:center;">📊 Cluster Results</h2>
            {% for label, docs in grouped.items() %}
                <div class="cluster-box">
                    <div class="cluster-title">Cluster {{ label }}</div>
                    {% for d in docs %}
                        <div class="doc">{{ d }}</div>
                    {% endfor %}
                </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    grouped = None
    docs = ""
    num_clusters = 3

    if request.method == "POST":
        docs = request.form["documents"].strip()
        num_clusters = int(request.form["num_clusters"])

        # Split input text into documents
        doc_list = [d.strip() for d in docs.split("\n") if d.strip()]

        # Generate semantic embeddings
        embeddings = model.encode(doc_list)

        # Perform K-Means clustering
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        labels = kmeans.fit_predict(embeddings)

        # Group documents by cluster
        grouped = defaultdict(list)
        for label, doc in zip(labels, doc_list):
            grouped[label].append(doc)

    return render_template_string(HTML_TEMPLATE, grouped=grouped, docs=docs, num_clusters=num_clusters)


if __name__ == "__main__":
    app.run(debug=True)
