import pickle



def open_model(model_name, folder = 'Dev/'):
    
    """
    Load a saved model from disk.
    
    Parameters
    ----------
    model_name : str
        Name of the model to load.
        
    Returns
    -------
    model : object
        The loaded model, or None if loading failed.
    """
    
    file_name = model_name
    model_name = './Models/' + folder + model_name + '.pkl'
    
    try:
        
        model = pickle.load(open(model_name, 'rb'))
        print(f'{file_name} loaded successfully!')
        
        return model
    
    except Exception as e:
        
        print(f'Error loading model {file_name}: {str(e)}')
        
        return None


def make_prediction(model, data):
    """Realiza a predição usando o modelo scikit-learn"""
    try:
        # Fazer a predição - usando a interface scikit-learn
        prediction_proba = model.predict_proba(data)
        
        # Obter a classe predita (0 ou 1)
        prediction = model.predict(data)
        
        # Retornar o resultado da primeira amostra
        result = int(prediction[0])
        
        return result
    
    except Exception as e:
        
        raise ValueError(f"Erro ao fazer a predição: {e}")