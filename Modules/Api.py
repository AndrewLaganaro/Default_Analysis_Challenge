import pandas as pd
import numpy as np
import inflection



def validate_json(data):
    
    """Verifica se os campos necessários estão presentes no JSON"""
    
    required_fields = ['default_3months', 'ioi_36months', 'ioi_3months', 'valor_por_vencer', 'valor_quitado', 'valor_total_pedido']
    
    for field in required_fields:
        
        if field not in data:
            
            return False, f"Campo obrigatório ausente: {field}"
    
    return True, "JSON válido"


def process_json_for_prediction(data):
    """Processa o JSON para o formato adequado para predição"""
    try:
        
        df_raw = pd.DataFrame([data])
        
        snakecase = lambda column: inflection.underscore(column)
        Colunas_new = list(map(snakecase, df_raw.columns))
        df_raw.columns = Colunas_new
        
        df_raw = df_raw.replace("missing", np.nan)
        
        # valor_vencido, valor_quitado, ioi_3months, ioi_36months
        df_raw['var_ioi'] = df_raw[['ioi_3months', 'ioi_36months']].std(axis=1)
        df_raw['taxa_cresc_quitado'] = df_raw['valor_quitado'] / (df_raw['ioi_3months'] + 1)
        df_raw.columns.name = None
        df_transformed = df_raw.copy()
        # 1. default_3months, ioi_36months, ioi_3months, valor_por_vencer, valor_quitado, valor_total_pedido
        df_transformed['default_3months_transformed'] = np.log1p(df_raw['default_3months'])
        df_transformed['default_3months_scaled'] = (df_transformed['default_3months_transformed'] - df_transformed['default_3months_transformed'].min()) / \
                                                    (df_transformed['default_3months_transformed'].max() - df_transformed['default_3months_transformed'].min())
        # 2. ioi_36months
        df_transformed['ioi_36months_transformed'] = np.log(df_raw['ioi_36months'].replace(0, 0.1))
        df_transformed['ioi_36months_scaled'] = (df_transformed['ioi_36months_transformed'] - df_transformed['ioi_36months_transformed'].min()) / \
                                                (df_transformed['ioi_36months_transformed'].max() - df_transformed['ioi_36months_transformed'].min())
        # 3. ioi_3months
        df_transformed['ioi_3months_transformed'] = np.log(df_raw['ioi_3months'].replace(0, 0.1))
        df_transformed['ioi_3months_scaled'] = (df_transformed['ioi_3months_transformed'] - df_transformed['ioi_3months_transformed'].min()) / \
                                                (df_transformed['ioi_3months_transformed'].max() - df_transformed['ioi_3months_transformed'].min())
        # 4. valor_por_vencer
        df_transformed['valor_por_vencer_transformed'] = np.log1p(df_raw['valor_por_vencer'])
        df_transformed['valor_por_vencer_scaled'] = (df_transformed['valor_por_vencer_transformed'] - df_transformed['valor_por_vencer_transformed'].min()) / \
                                                    (df_transformed['valor_por_vencer_transformed'].max() - df_transformed['valor_por_vencer_transformed'].min())
        # 6. valor_quitado
        df_transformed['valor_quitado_transformed'] = np.log1p(df_raw['valor_quitado'])
        df_transformed['valor_quitado_scaled'] = (df_transformed['valor_quitado_transformed'] - df_transformed['valor_quitado_transformed'].min()) / \
                                                (df_transformed['valor_quitado_transformed'].max() - df_transformed['valor_quitado_transformed'].min())
        # 15. valor_total_pedido
        df_transformed['valor_total_pedido_transformed'] = np.log1p(np.abs(df_raw['valor_total_pedido'])) * np.sign(df_raw['valor_total_pedido'])
        df_transformed['valor_total_pedido_scaled'] = (df_transformed['valor_total_pedido_transformed'] - df_transformed['valor_total_pedido_transformed'].min()) / \
                                                    (df_transformed['valor_total_pedido_transformed'].max() - df_transformed['valor_total_pedido_transformed'].min())
        # 19. var_ioi
        df_transformed['var_ioi_transformed'] = np.log1p(df_raw['var_ioi'])
        df_transformed['var_ioi_scaled'] = (df_transformed['var_ioi_transformed'] - df_transformed['var_ioi_transformed'].min()) / \
                                            (df_transformed['var_ioi_transformed'].max() - df_transformed['var_ioi_transformed'].min())
        # 20. taxa_cresc_quitado
        df_transformed['taxa_cresc_quitado_transformed'] = np.log1p(df_raw['taxa_cresc_quitado'])
        df_transformed['taxa_cresc_quitado_scaled'] = (df_transformed['taxa_cresc_quitado_transformed'] - df_transformed['taxa_cresc_quitado_transformed'].min()) / \
                                                    (df_transformed['taxa_cresc_quitado_transformed'].max() - df_transformed['taxa_cresc_quitado_transformed'].min())
        
        # Substituir infinitos por 0 (caso ocorram em alguma divisão)
        df_transformed = df_transformed.replace([np.inf, -np.inf], 0)
        
        # Ausência de NaN após transformações
        
        if df_transformed.isna().sum().sum() > 0:
            
            df_transformed = df_transformed.fillna(0)
        
        columns_to_keep = [col for col in df_transformed.columns if '_scaled' in col]
        
        df_final = df_transformed[columns_to_keep]
        
        df_final = df_final[['default_3months_scaled', 'ioi_36months_scaled', 'ioi_3months_scaled', 'valor_por_vencer_scaled', 
                                'valor_quitado_scaled', 'valor_total_pedido_scaled', 'var_ioi_scaled', 'taxa_cresc_quitado_scaled']]
                                
        return df_final, "Dados processados com sucesso"
    
    except Exception as e:
        
        return None, f"Erro ao processar dados: {e}"