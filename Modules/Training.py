import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score
import pickle



def save_model(model, model_name = 'model', folder = 'Dev/'):
    
    """
    Save a model to disk using pickle.
    
    Parameters
    ----------
    model : object
        The model to save
    model_name : str
        Name to give the saved model file
        
    Returns
    -------
    bool
        True if model was saved successfully
    """
    
    file_name = model_name
    
    if '.pkl' in model_name:
        
        model_name.replace('.pkl', '')
        
    model_name = './Models/' + folder + model_name + '.pkl'
    
    pickle.dump(model, open(model_name, 'wb'))
    
    print(f'{file_name} saved successfully!')
    
    return True


def classification_metrics(model_name, y_test, y_pred, y_proba):
    
    """
    Generates a DataFrame with classification metrics for a trained model.
    
    Parameters
    ----------
    model_name : str
    Name of the model.
    y_test : array-like
    Actual values.
    y_pred : array-like
    Predicted values.
    y_proba : array-like
    Probabilities of the positive class (required for AUC).
    
    Returns
    -------
    metrics_df : pd.DataFrame
    DataFrame with the main metrics (precision, recall, f1 and AUC).
    """
    
    report = classification_report(y_test, y_pred, output_dict=True)
    auc = roc_auc_score(y_test, y_proba)
    
    metrics = {
        'Model': model_name,
        'Accuracy': round(report['accuracy'], 4),
        'Precision_0': round(report['0']['precision'], 4),
        'Recall_0': round(report['0']['recall'], 4),
        'F1_0': round(report['0']['f1-score'], 4),
        'Precision_1': round(report['1']['precision'], 4),
        'Recall_1': round(report['1']['recall'], 4),
        'F1_1': round(report['1']['f1-score'], 4),
        'ROC_AUC': round(auc, 4)
    }
    
    return pd.DataFrame([metrics])


def crossval_xgboost(X_train, y_train, X_test, y_test, param_grid, n_iter=30, cv=3):
    
    """
    Train XGBoost model using RandomizedSearchCV for hyperparameter tuning.
    
    Parameters
    ----------
    X_train : array-like
        Training feature data
    y_train : array-like
        Training labels
    X_test : array-like
        Testing feature data
    y_test : array-like
        Testing labels
    param_grid : dict
        Hyperparameter grid for XGBoost
    n_iter : int, default=30
        Number of parameter settings sampled
    cv : int, default=3
        Number of cross-validation folds
        
    Returns
    -------
    best_model : XGBClassifier
        Best model found during hyperparameter search
    metrics_df : pd.DataFrame
        Classification metrics for the best model
    """
    
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    
    random_search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_grid,
        n_iter=n_iter,
        cv=cv,
        scoring='roc_auc',
        n_jobs=-1,
        random_state=42,
        verbose=1
    )
    
    random_search.fit(X_train, y_train)
    
    best_model = random_search.best_estimator_
    
    print(f"Melhores parâmetros encontrados:\n{random_search.best_params_}\n")
    
    save_model(best_model, "XGBoost_Best_Model_Dev")
    
    y_pred = best_model.predict(X_test)
    y_proba = best_model.predict_proba(X_test)[:, 1]
    
    metrics_df = classification_metrics("XGBoost_Best_Model", y_test, y_pred, y_proba)
    
    return best_model, metrics_df
