from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

with open('model/decision_tree_6_features.pkl', 'rb') as file:
    loaded_model_decision_tree = pickle.load(file)

# with open('model/stacking_model_updated.pkl', 'rb') as file:
#     loaded_model_stacking_model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # 获取用户输入的原始数据
        weight = float(request.form['weight'])  # 用户输入的体重
        weight_unit = request.form['weight-unit']
        height = float(request.form['height'])
        height_unit = request.form['height-unit']
        GenHlth = int(request.form['genhlth'])
        age = int(request.form['age'])
        HighChol = float(request.form['high_cholesterol'])  # 胆固醇水平
        HighBP = float(request.form['high_blood_pressure'])  # 血压值
        CardioRisk = HighBP + HighChol
        sex = request.form['sex']

        # 转换 height 为米 (如果单位是 feet)
        if height_unit == 'feet':
            height = height / 3.28084  # 英尺转换为米
        if height_unit == 'cm':
            height = height / 100  # 英尺转换为米

        if weight_unit == 'lb':
            weight = weight * 0.453592
        
        BMI = round(weight / (height ** 2), 1)
        

        # 将年龄转换为 13-level 分类
        def convert_age_to_category(age):
            if age < 18:
                return 0  # 未成年，未分类
            elif age <= 24:
                return 1
            elif age <= 29:
                return 2
            elif age <= 34:
                return 3
            elif age <= 39:
                return 4
            elif age <= 44:
                return 5
            elif age <= 49:
                return 6
            elif age <= 54:
                return 7
            elif age <= 59:
                return 8
            elif age <= 64:
                return 9
            elif age <= 69:
                return 10
            elif age <= 74:
                return 11
            elif age <= 79:
                return 12
            else:
                return 13  # 80 or older

        Age = convert_age_to_category(age)

        # 将性别映射为模型可接受的数值
        sex_mapping = {
            "male": 0,          # Male 映射为 0
            "female": 1,        # Female 映射为 1
            "non binary": random.choice([0, 1])
        }
        Sex = sex_mapping.get(sex, -1)

        # 生成模型输入数据
        input_data = np.array([[HighBP, HighChol, BMI, GenHlth, Sex, Age,CardioRisk]])

        #模型预测
        prediction1 = loaded_model_decision_tree.predict(input_data)
        prediction_result1 = round(float(prediction1[0]), 2)  # 假设是一个单一数值输出
        # prediction2 = loaded_model_stacking_model.predict(input_data)
        # prediction_result2 = round(float(prediction2[0]), 2)  # 假设是一个单一数值输出
        #prediction_result = 0.4

        # 将结果传递给结果页面
        return render_template('result.html', bmi=BMI, chol=HighChol, bp=HighBP,prediction1=prediction_result1)

    except Exception as e:
        # 如果出错，返回错误信息
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)