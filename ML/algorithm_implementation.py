from flask import Flask, request, jsonify
from algorithm import KNNClassifier, RankingAlgorithm

app = Flask(__name__)

knn = KNNClassifier(k=3)

ranking_algo = RankingAlgorithm()

@app.route('/predict_knn', methods=['POST'])
def predict_knn():
    data = request.json['data'] 
    predictions = knn.predict(data)
    return jsonify(predictions=predictions)

@app.route('/rank_items', methods=['POST'])
def rank_items():
    scores = request.json['scores']
    ranked_items = ranking_algo.rank_items(items, scores)
    return jsonify(ranked_items=ranked_items)

if __name__ == '__main__':
    app.run(debug=True)
