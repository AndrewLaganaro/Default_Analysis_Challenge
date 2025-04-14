import streamlit as st
import json
from Modules.Predict import make_prediction, open_model
from Modules.Api import validate_json, process_json_for_prediction
from PIL import Image



st.set_page_config(layout="wide", page_title="X-Health - Predição de Inadimplência")


with st.sidebar:
    
    st.title("Arquivos")
    
    uploaded_file = st.file_uploader("Carregar arquivo JSON", type = ["json"])
    
    analyze_button = st.button("Analisar")
    
    json_data = None
    
    if uploaded_file is not None:
        
        try:
            
            json_data = json.load(uploaded_file)
            
            st.success("Arquivo JSON carregado com sucesso")
            
        except Exception as e:
            
            st.error(f"Erro ao carregar o arquivo: {e}")

col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    
    with col_img2:
        
        image = Image.open("./Assets/Images/X-Health.png")
        width, height = image.size
        
        new_width = int(width * 2/3)
        
        st.image("./Assets/Images/X-Health.png", width=new_width, use_container_width=False)
    st.title("Predição de inadimplência [X-Health]")
    
    if analyze_button and json_data is not None:
        
        is_valid, validation_msg = validate_json(json_data)
        
        if is_valid:
            
            processed_data, process_msg = process_json_for_prediction(json_data)
            
            if processed_data is not None:
                
                model = open_model("XGBoost_Best_Model_Prod", folder = 'Prod/')
                
                if model is not None:
                    try: 
                        prediction_result = make_prediction(model, processed_data)
                    except:
                        st.error(f"Erro ao fazer predição: {e}")
                    if prediction_result is not None:
                        
                        if prediction_result == 1:
                            st.success("✅ O Cliente é um Bom Pagador")
                        else:
                            st.error("❌ O Cliente é um Provável Inadimplente")
                        
                        st.subheader("Dados analisados:")
                        st.json(json_data)
                else:
                    st.error("Não foi possível carregar o modelo")
            else:
                st.error(process_msg)
        else:
            st.error(validation_msg)
    
    elif analyze_button and json_data is None:
        st.warning("Por favor, carregue um arquivo JSON antes de analisar")
    
    else:
        st.info("Carregue um arquivo JSON e clique em Analisar para obter a predição. Ele deve conter apenas 01 registro.")
        st.info("Exemplo de JSON:\n```json\n{\"default_3months\": 0.0, \"ioi_36months\": 22.961318993, \"ioi_3months\": 9.7398055882, \"valor_por_vencer\": 6993.3971923151, \"valor_quitado\": 92981.1128787256, \"valor_total_pedido\": 4545.5232294998}\n```")
        
        