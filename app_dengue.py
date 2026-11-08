import streamlit as st
import pandas as pd
from datetime import date

# Configuração da página
st.set_page_config(
    page_title="Alerta Dengue - Jardim Aracati", 
    page_icon="🦟", 
    layout="centered"
)

# Cabeçalho do App
st.title("🦟 Alerta Dengue - Vigilância Comunitária")
st.subheader("Projeto de Extensão em Biomedicina (ODS 3)")

# Menu Lateral
menu = ["📍 Mapear Foco (Anônimo)", "📊 Painel de Riscos", "🛡️ Dicas da Biomedicina"]
escolha = st.sidebar.selectbox("Navegue pelo App", menu)
st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido para a comunidade do Jardim Aracati em prol da saúde pública e prevenção de arboviroses.")

# ----------------- ABA 1: MAPEAR FOCO -----------------
if escolha == "📍 Mapear Foco (Anônimo)":
    st.write("Ajude a comunidade relatando possíveis focos de água parada. **Sua identidade será mantida em sigilo absoluto.**")
    
    with st.form("form_foco", clear_on_submit=True):
        local = st.text_input("Endereço aproximado ou Ponto de Referência (Jardim Aracati):")
        
        tipo_foco = st.selectbox(
            "Qual é o tipo de criadouro?", 
            ["Pneu velho", "Caixa d'água destampada", "Vaso de planta", "Lixo acumulado", "Terreno baldio", "Outro"]
        )
        
        obs = st.text_area("Observação adicional (opcional):", placeholder="Ex: Tem muita água acumulada depois da chuva de ontem.")
        
        submitted = st.form_submit_button("Enviar Alerta")
        
        if submitted:
            if local != "":
                st.success("✅ Alerta registrado com sucesso! Obrigado por ajudar a proteger nossa comunidade.")
                st.balloons()
            else:
                st.error("⚠️ Por favor, insira o local ou ponto de referência do foco para podermos registrar.")

# ----------------- ABA 2: PAINEL DE RISCOS -----------------
elif escolha == "📊 Painel de Riscos":
    st.write("### Monitoramento Local - Jardim Aracati")
    st.write("Abaixo estão os focos relatados recentemente na região. A ação conjunta dos moradores é essencial para combater o mosquito.")
    
    dados_mock = {
        "Data": ["05/11/2026", "06/11/2026", "07/11/2026", date.today().strftime("%d/%m/%Y")],
        "Local": ["Rua Principal, perto da padaria", "Terreno baldio na Rua 2", "Praça central", "Calçada da Rua 5"],
        "Criadouro": ["Pneu velho", "Lixo acumulado", "Caixa d'água destampada", "Garrafas viradas para cima"],
        "Status": ["🔴 Pendente", "🟢 Resolvido", "🔴 Pendente", "🔴 Pendente"]
    }
    
    df = pd.DataFrame(dados_mock)
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.info("💡 Juntos, podemos transformar todos os 'Pendentes' em 'Resolvidos' avisando os vizinhos e limpando os espaços!")

# ----------------- ABA 3: DICAS DA BIOMEDICINA -----------------
elif escolha == "🛡️ Dicas da Biomedicina":
    st.write("### Como combater o *Aedes aegypti*")
    st.write("Informações validadas pelas diretrizes de Saúde Pública do Ministério da Saúde:")
    
    st.markdown("""
    * **Tampe os tonéis e caixas d’água:** Mantenha-os sempre muito bem fechados.
    * **Atenção aos vasos de plantas:** Coloque areia até a borda dos pratinhos para evitar o acúmulo de água.
    * **Limpe as calhas:** Remova folhas, galhos e tudo que possa impedir a água de correr perfeitamente.
    * **Garrafas e lixo:** Guarde garrafas sempre viradas para baixo e feche bem os sacos de lixo.
    * **Sintomas:** Em caso de febre alta, dor no corpo e manchas vermelhas, não se automedique. Procure a UBS mais próxima.
    """)
    
    st.warning("🩸 A prevenção ambiental é a medida mais eficaz contra a Dengue, Zika e Chikungunya.")