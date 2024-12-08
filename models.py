// 模拟训练好的模型参数（示例数据，需要根据实际模型调整）
const linearModelWeights = [1.2, -0.8, 0.5, 0.3, -0.6]; // 示例线性回归权重
const linearModelIntercept = 2.0;

// 输入数据示例（在实际应用中由用户输入提供）
const sampleInput = [10, 20, 30, 40, 50];

// 线性回归预测函数
function predictLinearRegression(input) {
    if (input.length !== linearModelWeights.length) {
        throw new Error("Input size does not match model size.");
    }

    // 计算加权和并加上截距
    let prediction = linearModelIntercept;
    for (let i = 0; i < input.length; i++) {
        prediction += input[i] * linearModelWeights[i];
    }
    return prediction;
}

