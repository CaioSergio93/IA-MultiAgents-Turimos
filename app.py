import streamlit as st
import datetime 
from main import TripCrew # Assumindo que esta é a sua classe principal

# --- 1. INJEÇÃO DE CSS PARA ESTILO E TEMA (Tonalidade da Logo) ---
# O Streamlit prefere que a injeção de CSS ocorra antes de qualquer outro elemento de UI
st.markdown("""
<style>
/* 1. TEMA GERAL E CORES (Tonalidade da Logo) */
:root {
    --primary-color: #00BCD4; /* Ciano/Turquesa da logo */
    --background-color: #F8F8F8; /* Fundo muito levemente off-white */
    --secondary-background-color: #FFFFFF; /* Fundo dos inputs e sidebar */
    --text-color: #2E3E4E; /* Cinza escuro para o texto */
}

/* 2. BACKGROUND DO CORPO DA PÁGINA */
.stApp {
    background-color: var(--background-color);
}

/* 3. BARRA LATERAL (SIDEBAR) - Mantém o fundo branco para inputs */
.css-1cpxqw2, .css-1dp5ssi, .css-1dj0i83 { 
    background-color: #FFFFFF; 
    border-right: 1px solid #EEEEEE; 
    padding-top: 20px;
    
    /* PROPRIEDADES ADICIONADAS PARA FIXAR A SIDEBAR */
    position: fixed !important;
    height: 100vh;
}
.css-1dp5ssi > div:first-child {
    background-color: #FFFFFF;
}

/* --- NOVO: OCULTA O BOTÃO DE RECOLHER/MENU DA SIDEBAR --- */
/* Oculta o botão de menu/sanduíche na página principal */
[data-testid="stSidebarToggle"] {
    display: none; 
}
/* Oculta o botão de recolher que aparece DENTRO da sidebar (apenas para garantir) */
[data-testid="stSidebarToggleButton"] {
    display: none; 
}


/* 4. BOTÃO PRIMÁRIO (usa a cor principal da logo) */
.stButton>button {
    /* Cor de fundo do botão primário (usa a cor da logo) */
    background-color: var(--primary-color) !important;
    border-color: var(--primary-color) !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
    transition: background-color 0.3s;
    /* Alinha o texto do botão ao centro dentro do container */
    display: block; 
    margin: 0 auto;
    padding: 10px 20px; /* Adiciona padding para parecer maior */
}
.stButton>button:hover {
    background-color: #00A3B5 !important; 
}

/* 5. Inputs (Bordas mais suaves) */
div[data-baseweb="input"], div[data-baseweb="select"], div[data-baseweb="textarea"] {
    border-radius: 6px;
}




</style>
""", unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA PÁGINA ---
# Deve ser o segundo item a ser executado
st.set_page_config(
    page_title="ExplorerIA",
    layout="wide",
    initial_sidebar_state="expanded" # Garante que comece expandida
)

# --- 3. ÁREA DE INPUTS (st.sidebar) ---
with st.sidebar:
    
    # A. Logo no topo da Sidebar 
    st.image(
        "./ExplorerIA.png", 
        width=150
    )
    
    # B. Cabeçalho de Instrução
    st.header("✈️ Insira os Detalhes da Sua Viagem")
    
    # C. Campos de Input
    
    # Campo de Texto - Origem
    origin = st.text_input(
        " 📍 De onde você estará viajando? (Ex: São Paulo, Brasil)",
        value=""
    )
    
    # Campo de Texto - Cidades
    cities = st.text_input(
        " 🗺️ Quais são as opções de cidades que você tem interesse em visitar? (Separe por vírgula, Ex: Paris, Roma, Londres)",
        value=""
    )
    
    # Seletor de Datas (Range de Datas)
    today = datetime.date.today()
    default_start = today + datetime.timedelta(days=30) 
    default_end = default_start + datetime.timedelta(days=7) 
    
    date_range = st.date_input(
        "🗓️ Qual é o período de datas que você tem interesse em viajar?",
        value=(default_start, default_end),
        min_value=today, 
        format="DD/MM/YYYY"
    )
    
    # Campo de Texto - Interesses
    interests = st.text_input(
        "Quais são alguns dos seus interesses e hobbies principais? (Ex:Museus 🏛️, Comida Tipicas 🍽️, Trilhas ⛰️, Festivais 🌃)",
        value=""
    )


# --- 4. CONTEÚDO PRINCIPAL CENTRALIZADO ---

# Cria colunas para centralizar o bloco principal (Título, Subtítulo, Botão)
# Proporção: 1 (Espaço Esquerdo) | 3 (Conteúdo) | 1 (Espaço Direito)
col_left_spacer, col_center_content, col_right_spacer = st.columns([1, 3, 1]) 

with col_center_content:
    
    # A. Ajuste de Espaçamento Vertical no Topo (substitui a margem da imagem)
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    
    # B. Título Principal Centralizado
    st.markdown(
        """
        <h2 style='text-align: center; margin-bottom: 5px; color: var(--text-color); font-size: 2.2em;'>
            Bem-vindo ao Explorer<span style='color:var(--primary-color);'>IA</span>
        </h2>
        <p style='text-align: center; margin-top: 0px; margin-bottom: 40px; font-size: 1.1em; color: var(--text-color);'>
            Use a inteligência artificial para planejar sua viagem dos sonhos com roteiros detalhados e personalizados.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # C. Botão Centralizado e Lógica de Execução
    # Usamos colunas internas para forçar o botão a ocupar uma largura menor e centralizada
    btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])

    with btn_col2:
        # Adicionei um espaço em branco para garantir o alinhamento vertical
        st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        
        if st.button("🚀 Criar Meu Plano de Viagem", type="primary", use_container_width=True):
            
            # --- Início da Lógica de Execução ---
            
            # 1. Validação de Campos
            if not origin or not cities or not interests:
                st.error("🚨 Por favor, preencha a **Origem**, as **Cidades** e seus **Interesses**.")
                st.stop()
                
            if len(date_range) != 2:
                st.error("🚨 Por favor, selecione as **duas** datas (início e fim) no calendário da viagem.")
                st.stop()
                
            # 2. Formatação das Datas para a CrewAI
            start_date = date_range[0].strftime("%Y-%m-%d")
            end_date = date_range[1].strftime("%Y-%m-%d")
            travel_dates = f"De {start_date} a {end_date}" 

            # 3. Execução da CrewAI com Spinner
            try:
                with st.spinner("⏳ A ExplorerIA está buscando os melhores roteiros e informações da sua viagem..."):
                    
                    # Instanciando e Rodando a TripCrew
                    research_crew = TripCrew(origin, cities, travel_dates, interests)
                    result = research_crew.run()
                
                # 4. Exibição do Resultado
                st.success("✅ Seu Plano de Viagem está Completo!")
                st.subheader("📋 Roteiro Detalhado de Viagem")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"❌ Ocorreu um erro ao executar a CrewAI: {e}")
                st.info("Verifique se as variáveis de ambiente (como a `SERPER_API_KEY`) estão configuradas corretamente no seu sistema ou arquivo `.env`.")