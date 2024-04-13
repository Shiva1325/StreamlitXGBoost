import joblib as jb
import pickle
def predict(data):
    for i in data.keys():
        print(i)
    reg = pickle.load(open('xgb_tune_1.pkl','rb'))
    # reg = jb.load("xgb_tune.sav")
    return reg.predict(data)
