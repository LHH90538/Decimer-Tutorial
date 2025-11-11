import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # 强制只用 CPU
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"   # 减少日志噪音

from DECIMER import predict_SMILES   # 必须在设置好环境后才导入库，否则会使用GPU

smiles = predict_SMILES("mol_png/Boc保护基.png")
print(f"识别结果: {smiles}")