import joblib as jb
import pickle
def predict(data):
    print(data['CG_airfyer'])
    reg = pickle.load(open('xgb_tune_1.pkl','rb'))
    # reg = jb.load("xgb_tune.sav")
    return reg.predict(data)
