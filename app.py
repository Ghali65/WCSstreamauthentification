import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import json

def menu():
    with st.sidebar:
        selection = option_menu(menu_title=None, options=["Accueil", "Portofolio"], icons=['house', 'palette2'])
        # Retourner la sélection pour afficher le contenu principal
        authenticator.logout("Déconnexion")
        return selection


def accueil():
    titre = "Bienvenue sur ma page 🚀"
    st.markdown(f"<h1 style='text-align: center;'>{titre}</h1>", unsafe_allow_html=True)
    st.title("")
    st.header("Introduction", divider="orange")
    st.subheader("")
    intro_part_1 = '''Cet espace a été créé avec streamlit lors de ma formation **Data Analyst** à la Wild Code School !
    '''
    return_line = ""
    intro_part_2 = "Vous y trouverez à terme quelques projets réalisés mais d'ici là la 🚧**page portofolio est en travaux**🚧 **!**"
    end_intro = "Bonne visite !"
    st.write(intro_part_1)
    st.write(return_line)
    st.write(intro_part_2)
    st.write(return_line)
    st.write(end_intro)


def gallery():
    titre = "🚧 Mon portofolio 🚧"
    st.markdown(f"<h1 style='text-align: center;'>{titre}</h1>", unsafe_allow_html=True)
    # Ajouter de l'espace sous le titre
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    # Appliquer le CSS pour fixer la hauteur des images 
    st.markdown( """ <style> img { height: 200px; object-fit: cover; } </style> """, unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)
    with col1:
        tcol1 = "A cat"
        st.markdown(f"<h4 style='text-align: center;'>{tcol1}</h4>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with col2:
        tcol2 = "A dog"
        st.markdown(f"<h4 style='text-align: center;'>{tcol2}</h4>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with col3:
        tcol3 = "An owl"
        st.markdown(f"<h4 style='text-align: center;'>{tcol3}</h4>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



# Charger les données utilisateurs depuis le fichier JSON
with open('utilisateur.json', 'r') as f:
    lesDonneesDesComptes = json.load(f)

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30  # Le nombre de jours avant que le cookie expire
)

authenticator.login()


# Initialiser l'état de l'authentification dans session_state si absent
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None

# Affichage selon l'état d'authentification
if st.session_state["authentication_status"]:
    selection = menu()
    if selection == "Accueil":
        accueil()
    elif selection == "Portofolio":
        gallery()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
