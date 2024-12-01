from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 获取用户提交的表单数据
        input_data = request.form.to_dict()

        # 模拟模型预测逻辑
        age = float(input_data.get("age", 0))
        weight = float(input_data.get("weight", 0))
        height = float(input_data.get("height", 0))
        model_choice = input_data.get("model_choice", "model_1")

        # 模拟预测结果
        if model_choice == "model_1":
            prediction = f"Model 1 predicts: {age + weight - height:.2f}"
        elif model_choice == "model_2":
            prediction = f"Model 2 predicts: {age * 0.5 + weight * 0.3 - height * 0.2:.2f}"
        else:
            return jsonify({"error": "Invalid model choice"}), 400

        # 返回预测结果
        return render_template("result.html", prediction=prediction)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)