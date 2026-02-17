import streamlit as st

st.title("Calculateur d'Indice de Masse Corporelle(IMC)")
st.markdown("Cette application vous permet de calculer votre imc")
st.subheader("Entrez vos informations")
poids=st.number_input("entrer votre poids (kg):",min_value=1.0,value=100.0,step=0.01) 
taille=st.number_input("entrer votre taille(m):",min_value=0.5,value=1.40,step=0.01)

if st.button ("Calculer"):
    imc = poids/ (taille ** 2)
    st.write("imc")
    if imc <18:
        st.info(" Vous etes tres maigre")
    elif imc<25:
        st.warning("Vous etes en poids normal")
    elif imc<30:
        st.warning("Vous etes en surpoids")
    else:
        st.error("Obésité")

        
    





