# TradingStrat_Interview

### Resources used for deployment-prep:

https://towardsdatascience.com/deploying-scikit-learn-models-at-scale-f632f86477b8

https://towardsdatascience.com/deploying-a-scikit-learn-model-on-aws-using-sklearn-estimators-local-jupyter-notebooks-and-the-d94396589498

https://towardsdatascience.com/from-jupyter-notebook-to-deployment-a-straightforward-example-1838c203a437


### Model dumping - future use:

In order to rebuild a similar model with future versions of scikit-learn, additional metadata should be saved along the pickled model:

*The training data, e.g. a reference to an immutable snapshot

*The python source code used to generate the model

*The versions of scikit-learn and its dependencies

*The cross validation score obtained on the training data
