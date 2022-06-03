import data
from lib import *

#Random Forest is determined best performing model from EDA based on R-squared k-fold cross validation score
#Tunning the model for best performance
def gridsearch(xtrain, ytrain):
    #setting search args
    num_estms=[20,40,80,100]
    max_depth=[5,10]
    criterion=['entropy','gini']
    paramaters=dict(n_estimators=num_estms,max_depth=max_depth, criterion=criterion)

    #model & populating grid attributes
    model=RandomForestClassifier(n_jobs=-1)
    kfold=KFold(n_splits=10)
    grid=GridSearchCV(estimator=model, param_grid=paramaters, scoring='accuracy', cv=kfold)
    grid_result=grid.fit(xtrain, ytrain)

    return grid_result.best_params_


#getting best parameters for the model
bestparams=gridsearch(data.x_train, data.y_train)

#RF model, version X (for model directory tracking)
def model_X(params, xtrain, ytrain):
    model=RandomForestClassifier(**params)
    
    return model.fit(xtrain, ytrain)

#generated model
modelX=model_X(bestparams, data.x_train, data.y_train)

#saving the model for future use 
def export_model(model):
    
    return dump(model, 'TradingStrat/modelX.joblib')

#persisting the model, accessible via Google Cloud ML Engine, AWS 
export_model(modelX)
    