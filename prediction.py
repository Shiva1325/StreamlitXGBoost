import joblib as jb
def predict(data):
    reg = pickle.load(open('model.pkl','rb'))
    # reg = jb.load("xgb_tune.sav")
    # return reg.predict(data)
    return 1
