from dash import Dash, html, Output, Input, dcc



#   Chemin logos
chemin_logo_hotel = 'assets\logos\hotel.svg'
chemin_nuites_icon = 'assets\logos\point_nuites_icon.png'
chemin_poi_divertisement = 'assets\logos\point_divertisement_indigo.png'
chemin_poi_jaune = 'assets\logos\point_Expo et vente_jaune.png'
chemin_poi_pink = 'assets\logos\point_Non renseigne_pink.png'
chemin_poi_red = 'assets\logos\point_Patrimoine naturel_rouge.png'
chemin_poi_blue = 'assets\logos\point_patrimoine_historique_blue.png'
chemin_poi_green = 'assets\logos\point_Social et culturel_green.png'
chemin_poi_orange = 'assets\logos\point_sport_orange.png'

#Legende

legende = html.Div(
    [
        html.Div(
            [                    
                html.A(html.Img(src=chemin_nuites_icon,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),  
                html.A(html.Img(src=chemin_logo_hotel,style={"width": "15px", "height": "15px","marginLeft": "5px","justifyContent": "start",})),                         
                                    
                html.Span("Nuitées", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "15px",}
        ),            

        html.Div(
            [
                html.Span("Points d'intérêts & évènements",style={'fontSize':'13px', 'fontFamily':'Lato',"marginLeft": "5px","justifyContent": "start",'fontWeight': 'Bold'}) 
            ]
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_divertisement,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': '#4b0082','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Divertissement", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_jaune,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'yellow','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Expo et vente", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_pink,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'pink','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Non renseigné", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_blue,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'blue','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Patrimoine historique", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_red,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'red','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Patrimoine naturel", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_green,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'green','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Social et culturel", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),

        html.Div(
            [                    
                html.A(html.Img(src=chemin_poi_orange,style={"width": "15px", "height": "15px","marginLeft": "10px","justifyContent": "start",})),                        
                html.Span(
                        html.I(className="bi bi-circle-fill", style={'color': 'orange','fontSize': '12px'}),
                        style={'marginLeft': '5px'}
                ),                   
                html.Span("Sport", 
                            style={'fontSize':'12px', 'fontFamily':'Lato',"marginLeft": "10px","justifyContent": "start",}
                ),   

            ],style={
                "display": "flex",
                "alignItems": "center",
                "alignContent": "space-around",
                "marginBottom": "5px",
                "marginTop": "5px",}
        ),


    ], style ={"height": "230px",
                "width": "200px",
                "position": "absolute",
                "bottom": "25px",
                "right": "5px",
                "zIndex": "1000",
                "backgroundColor": "white",
                "justifyContent": "center",
                "alignItems": "center"}
)