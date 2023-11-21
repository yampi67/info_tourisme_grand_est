from dash import html
import dash_bootstrap_components as dbc



#           CARDS       #

card_1 = dbc.Card(
    [    
        dbc.CardBody(
            [
                html.Div(
                    [
                        html.Div(id='titre_offre'),  
                        html.Div(id = 'nombre_offre')                        
                    ],style={'marginTop':'10px','alignItems': 'center', 'justifyContent': 'center','display': 'flex','flexDirection': 'column'}
                )            
            ]
        ),
    ], style= {'backgroundColor' : '#0174BE' , 'height' :  '160px' , 'width' :  '250px'  }
)


card_2 = dbc.Card(
    [    
        dbc.CardBody(
                [
                    html.Div(
                        [
                            html.Span("Évènements",style={'color': 'white', 'fontSize':'18px'}),  
                            html.Div(id = 'nombre_evenements', style={'textAlign': 'center'})           
                        ],style={'marginTop':'10px','alignItems': 'center', 'justifyContent': 'center','display': 'flex','flexDirection': 'column'}
                    )            
                ]
        ),
    ], style= {'backgroundColor' : '#0174BE' , 'height' :  '160px' , 'width' :  '250px'  }
)


card_3 = dbc.Card(
    [        
        dbc.CardBody(
            [
                html.Div(
                    [
                        html.Span("Points d'intérêts",style={'color': 'white', 'fontSize':'18px'}),  
                        html.Div(id='nombre_poi')                        
                    ],style={'marginTop':'10px','alignItems': 'center', 'justifyContent': 'center','display': 'flex','flexDirection': 'column'}
                )            
            ]
        ),
    ], style= {'backgroundColor' : '#0174BE' , 'height' :  '160px' , 'width' :  '250px'  }
)

