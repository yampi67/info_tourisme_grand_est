from dash import Dash,html ,dcc, Input, Output
import dash_bootstrap_components as dbc
from assets.cards.cards import *
import geopandas as gpd
import dash_leaflet as dl
import json
from dash_extensions.javascript import assign
from assets.legende import legende
import geobuf


#   Chemin logos
chemin_logo_datagrandest = 'assets\logos\Logo_DataGrandEst.png'
chemin_logo_data_tourisme = 'assets\logos\Logo_DATAtourisme_PNG.png'
chemin_logo_hotel = 'assets\logos\hotel.svg'


info = "Les dates des évènements ont été obtenues à partir du site DATAtourisme. La date initiale du calendrier est le 13 décembre car c'est le jour du concours "


##############                   connection to geojsons                      ##################


#####################            "departements"                 #############################

# chemin_departements = 'assets/geojson/departements.geojson'
# dpt_geojson = gpd.read_file(chemin_departements,crs="EPSG:4326", geometry='geom')
chemin_dpt_geobuf = 'assets/geojson/departements.pbf'
with open(chemin_dpt_geobuf, 'rb') as f:
        departements_data = geobuf.decode(f.read())

# Create javascript function that filters on feature name.
# dpt_filter = assign("function(feature, context){return context.hideout.includes(feature.properties.libgeo);}")

#   Noms des departements
libgeo_values = set(feature['properties']['libgeo'] for feature in departements_data['features'])
# Crear un GeoDataFrame a partir del GeoJSON decodificado
gdf_dpt = gpd.GeoDataFrame.from_features(departements_data['features'])





#   POI PERMANENT  
# chemin_poi_permanent = 'assets/geojson/poi_permanent.geojson'
# poi_permanent_geojson = gpd.read_file(chemin_poi_permanent,crs="EPSG:4326", geometry='geom')
chemin_poi_geobuf = 'assets/geojson/poi_permanent.pbf'
with open(chemin_poi_geobuf, 'rb') as f:
        poi_permanent_geojson = geobuf.decode(f.read())
gdf_permanents = gpd.GeoDataFrame.from_features(poi_permanent_geojson['features'])




#   POI EVENEMENTS  
# chemin_poi_evenements = 'assets/geojson/poi_evenement.geojson'
# poi_evenement_geojson = gpd.read_file(chemin_poi_evenements,crs="EPSG:4326", geometry='geom')
chemin_evenements_geobuf = 'assets/geojson/poi_evenement.pbf'
with open(chemin_evenements_geobuf, 'rb') as f:
        poi_evenement_geojson = geobuf.decode(f.read())
gdf_evenements = gpd.GeoDataFrame.from_features(poi_evenement_geojson['features'])



#   Nuitées 
# chemin_nuites = 'assets/geojson/nuites.geojson'
# nuites_geojson = gpd.read_file(chemin_nuites,crs="EPSG:4326", geometry='geom')
chemin_nuites_geobuf = 'assets/geojson/nuites.pbf'
with open(chemin_nuites_geobuf, 'rb') as f:
        nuites_geojson = geobuf.decode(f.read())
gdf_nuites = gpd.GeoDataFrame.from_features(nuites_geojson['features'])




app = Dash(
            __name__,
            external_stylesheets=[dbc.themes.FLATLY, 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.6.0/font/bootstrap-icons.css'],
            suppress_callback_exceptions=True,
            )
server = app.server


app.layout =    dbc.Container(
    [
        dcc.Store(id='output_geojson_nuites', storage_type='memory', data={}),
        dcc.Store(id='output_geojson_dpt', storage_type='memory', data={}),
        dcc.Store(id='output_geojson_evenements', storage_type='memory', data={}),
        dcc.Store(id='output_geojson_poi_permanent', storage_type='memory', data={}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A(html.Img(src=chemin_logo_datagrandest, style = {'height':'80px','width': '125px','marginTop' :'0px' , 'marginRight': '25px' }),
                               href = "https://www.datagrandest.fr/portail/fr" 
                            )                

                    ],width={"size": 1,"order": 1}
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Span("INFO TOURISME GRAND EST", style={'color': 'white', 
                                                                    'backgroundColor':'#0C356A',
                                                                    'fontWeight':'bold',
                                                                    'fontSize':'40px',
                                                                    'height': '80px', 
                                                                    'display': 'flex', 
                                                                    'textAlign': 'center', 
                                                                    'alignItems': 'center', 
                                                                    'justifyContent': 'center', }
                                )
                            ]
                        )
                    ],width={"size": 9,"order": 2}, style={"padding": "0px"}
                ),
                dbc.Col(
                    [
                        html.A(html.Img(src=chemin_logo_data_tourisme, style = {'height':'50px','width': '180px','marginTop' :'15px' , 'marginLeft': '25px' }),
                               href = "https://www.datatourisme.fr/" 
                            )                

                    ],width={"size": 1,"order": 3}
                ),
            ],justify="center",className='mb-3 mt-1', 
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Span("Hébergements",style={'fontFamily': 'Lato', 'fontSize': '25px','color': '#0C356A','fontWeight': 'bold'}),
                                                                html.Hr(className="my-2"),
                                                            ],style ={'alignItems': 'center', 'justifyContent': 'center','textAlign': 'center',}
                                                        )
                                                    ],justify="center", className='mb-3'
                                                ),                                
                                                
                                                dbc.Row(
                                                    [                                
                                                        html.Div(
                                                            [
                                                                html.Span('Sélectionner un département', style={'fontFamily': 'Lato', 'fontSize': '13px'})   
                                                            ], style ={'alignItems': 'center', 'justifyContent': 'center','textAlign': 'center',}
                                                        )                                                           
                                                    ],justify="center", className='mb-1 mt-2'
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                dcc.Dropdown(
                                                                    id='dpt_dropdown',
                                                                    # options=[{'label': dpt, 'value': dpt} for dpt in nuites_geojson['libdept'].unique()],
                                                                    options=[{'label': dpt, 'value': dpt} for dpt in libgeo_values],
                                                                    value = "Ardennes",                                            
                                                                    clearable=False,
                                                                )
                                                            ], style={'width':'220px',}
                                                        )
                                                    ],justify="center",className='mb-3'
                                                ),
                                                dbc.Row(
                                                    [                                                             
                                                        html.Div(
                                                            [
                                                                html.Span("Type d'offre", style = {'fontFamily': 'Lato', 'fontSize': '13px','marginRight':'50px'}),
                                                                html.Span("Type d'occupation", style = {'fontFamily': 'Lato', 'fontSize': '13px','marginLeft':'45px'}),                                        
                                                            ], style={'alignItems': 'center', 'justifyContent': 'center','display': 'inline-block','textAlign': 'center',}
                                                        ),
                                                    ],justify="center",className='mb-1'
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                dcc.Dropdown(
                                                                    id='offre_dropdown',                                        
                                                                    clearable=False,
                                                                    style={'width':'170px','marginRight':'10px'}
                                                                ),

                                                                dcc.Dropdown(
                                                                    id='occupation_dropdown',                                        
                                                                    clearable=False,
                                                                    style={'width':'170px'}
                                                                )
                                                            ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}
                                                        ) 
                                                    ],justify="center",className='mb-3'
                                                ),

                                            ],className="h-150 p-5 bg-light border rounded-3",
                                        )
                                    ],width={"size": 11,"order": 1},
                                ),
                            ],align="center", className='mb-3'
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Span("Évènements",style={'fontFamily': 'Lato', 'fontSize': '25px','color': '#0C356A','fontWeight': 'bold'}),
                                                                html.Span(
                                                                        html.I(className="bi bi-info-circle", style={'color': 'black','fontSize': '20px'}),
                                                                        id="info-calendrier",
                                                                        style={'marginLeft': '5px'}
                                                                ),                                                                                  
                                                                dbc.Tooltip(info, target="info-calendrier", placement='right-end'),  
                                                                html.Hr(className="my-2"),
                                                            ],style ={'alignItems': 'center', 'justifyContent': 'center','textAlign': 'center',}
                                                        )
                                                    ],justify="center", className='mb-3'
                                                ),  

                                                dbc.Row(
                                                    [
                                                        html.Div(
                                                            [
                                                                dcc.DatePickerRange(
                                                                    id = 'calendrier',
                                                                    start_date_placeholder_text="Date initiale",
                                                                    end_date_placeholder_text="Date finale",
                                                                    calendar_orientation='vertical',
                                                                    start_date = '2023-12-13',
                                                                    # end_date = '2024-05-28',
                                                                    min_date_allowed = '2023-12-01', 
                                                                    style = {'fontSize':'14px'}
                                                                )
                                                            ],style={'alignItems': 'center', 'justifyContent': 'center','display': 'flex',}
                                                        )                                        
                                                    ],justify="center",className="mt-1"
                                                ),

                                            ],className="h-150 p-5 bg-light border rounded-3",
                                        )

                                    ],width={"size": 11,"order": 1},
                                )

                            ],align="center",
                        )

                    ],width={"size": 3,"order": 1}
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                html.Div(
                                    [
                                        html.Span("Chiffres clés dans le département", style={'color': 'white', 
                                                                            'backgroundColor':'#FFC436',
                                                                            'fontFamily' : 'Lato',
                                                                            # 'backgroundColor':'#D8C4B6',
                                                                            'fontWeight':'bold',
                                                                            'fontSize':'25px',
                                                                            'height': '40px', 
                                                                            'display': 'flex', 
                                                                            'textAlign': 'center', 
                                                                            'alignItems': 'center', 
                                                                            'justifyContent': 'center', }
                                        )
                                    ],style={'width':'1125px'}
                                )
                            ],justify="start",className='mb-2'
                        ),
                        dbc.Row(
                            [
                                dbc.Col([card_1],{"size": 3,"order" :1}),
                                dbc.Col([card_2],{"size": 3,"order" :2}),
                                dbc.Col([card_3],{"size": 3,"order" :3})  
                            ],justify="center",className='mb-3'
                        ),
                        dbc.Row(
                            [
                                html.Div(id='map_div'),                                  
                            ],align="center",justify="center",className='mb-3'
                        ),
                        dbc.Row(
                            [
                                html.Div(
                                    [
                                        html.Button(type="button", className="btn-close", **{"data-bs-dismiss": "alert"}),
                                        html.Strong("Source de données : "),
                                        " Les données utilisées pour cette application ont été assemblées à partir de sources ouvertes et non-ouvertes à l'usage du concours de visualisation de données ",
                                        html.A("Hackaviz de DataGrandEst 2023", href="https://www.datagrandest.fr/portail/fr/agenda/concours-visualisation-datagrandest-que-font-touristes-dans-grand-est", className="alert-link"),
                                        
                                        # dbc.Alert("Les données utilisées pour cette application ont été assemblées à partir de sources ouvertes et non-ouvertes à l'usage du concours de visualisation de données Hackaviz de DataGrandEst 2023", color="light"),
                                    ],style={'width': '1100px', 'textAlign': 'center', 'justifyContent': 'center'}, className='alert alert-dismissible alert-light'
                                )
                            ],align="center",justify="start",
                        )

                    ],width={"size": 8,"order": 2}
                )
            ],justify="center",align="center",
        )
    ], fluid=True
)
    


# # # Link drop down to geojson hideout prop (could be done with a normal callback, but clientside is more performant).
# app.clientside_callback("function(x){return x;}", Output("geojson_dpt", "hideout"), Input("dpt_dropdown", "value"))







#########       Callback TYPE D'OFFRE       ###############

@app.callback(
    Output('offre_dropdown', 'options'),     
    [Input('dpt_dropdown', 'value')]
)
def update_offre(selected_departement):
    nuites_filtered = gdf_nuites[gdf_nuites['libdept'] == selected_departement]
    offre_options = [{'label': offre, 'value': offre} for offre in nuites_filtered['offre'].unique()]    
    return offre_options

@app.callback(
    Output('offre_dropdown', 'value'),
    Input('offre_dropdown', 'options'))
def set_offre_values(available_options):
    return available_options[1]['value']




#########       Callback TYPE D'OCCUPATION       ###############

@app.callback(
    Output('occupation_dropdown', 'options'),     
    [Input('dpt_dropdown', 'value'),Input('offre_dropdown', 'value')]
)
def update_offre(selected_departement,offre_departement):
    nuites_filtered = gdf_nuites[(gdf_nuites['libdept'] == selected_departement) & (gdf_nuites['offre'] == offre_departement)]
    occupation_options = [{'label': occupation, 'value': occupation} for occupation in nuites_filtered['occup'].unique()]    
    return occupation_options

@app.callback(
    Output('occupation_dropdown', 'value'),
    Input('occupation_dropdown', 'options'))
def set_offre_values(available_options):
    return available_options[0]['value']






#######              GEOJSON des nuités l’échelle des dpt          #######

@app.callback(
    Output('output_geojson_nuites', 'data'),
    [Input('dpt_dropdown', 'value'),Input('offre_dropdown', 'value'),Input('occupation_dropdown', 'value')])
def get_filtered_geojson(selected_departement,offre,occupation):      
    
    nuites_filtered_dpt = gdf_nuites[(gdf_nuites['libdept'] == selected_departement)&(gdf_nuites['offre'] == offre)&(gdf_nuites['occup'] == occupation)]  
    nuites_filtered_dpt.crs = {'init': 'epsg:4326'}
    nuites_geojson_string = nuites_filtered_dpt.to_crs(epsg=4326).to_json()
    nuites_geojson_filtered = json.loads(nuites_geojson_string)  # Convertir la chaine JSON en tant qu'objet JSON    

    #Création des listes 
    filtered_features = [] # Cette liste qui est pour l'instat vide sera rempli avec #les valeurs : 'type' et 'crs', ce qui permettra la visualisation d'un geojson dans une carte leaflet 
    for feature in nuites_geojson_filtered['features']:
        # feature['properties']['tooltip'] = feature['properties']['libcom']
        feature['properties']['tooltip'] = f"<b>Type de propriété :</b> {feature['properties']['type']}<br><b>Commune :</b> {feature['properties']['libcom']}"
        filtered_features.append(feature)
      
    geojson_nuites = {
        'type': 'FeatureCollection',
        'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
        'features': filtered_features
    }    
    return geojson_nuites




#######              GEOJSON des EVENEMENTS à l’échelle des dpt          #######

@app.callback(
    Output('output_geojson_evenements', 'data'),
    [Input('dpt_dropdown', 'value'),Input('calendrier', 'start_date'),Input('calendrier', 'end_date')])
def get_filtered_geojson(selected_departement,date_initiale,date_finale):     
   
    evenements_filtered_dpt = gdf_evenements[(gdf_evenements['libdept'] == selected_departement)&(gdf_evenements['date_initial']>= date_initiale)&(gdf_evenements['date_final']<= date_finale)]  
    evenements_filtered_dpt.crs = {'init': 'epsg:4326'}  # Reemplaza 'tu_codigo_epsg' con el EPSG correspondiente a tu sistema de coordenadas
    evenements_geojson_string = evenements_filtered_dpt.to_crs(epsg=4326).to_json()
    evenements_geojson_filtered = json.loads(evenements_geojson_string)  # Convertir la chaine JSON en tant qu'objet JSON    
    
   #Création des listes 
    filtered_features = [] # Cette liste qui est pour l'instat vide sera rempli avec #les valeurs : 'type' et 'crs', ce qui permettra la visualisation d'un geojson dans une carte leaflet 
    for feature in evenements_geojson_filtered['features']:
        feature['properties']['tooltip'] = f"<b>Activité :</b> {feature['properties']['desc']}<br><b>Commune :</b> {feature['properties']['libcom']}"
        filtered_features.append(feature)

    geojson_evenements = {
        'type': 'FeatureCollection',
        'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
        'features': filtered_features
    }    
    return geojson_evenements




#######              GEOJSON des POIS PERMANENTS à l’échelle des dpt          #######

@app.callback(
    Output('output_geojson_poi_permanent', 'data'),
    [Input('dpt_dropdown', 'value')])
def get_filtered_geojson(selected_departement):   
    
    poi_filtered_dpt = gdf_permanents[(gdf_permanents['libdept'] == selected_departement)]  
    poi_filtered_dpt.crs = {'init': 'epsg:4326'}
    poi_geojson_string = poi_filtered_dpt.to_crs(epsg=4326).to_json()
    poi_geojson_filtered = json.loads(poi_geojson_string)  # Convertir la chaine JSON en tant qu'objet JSON    
    
    #Création des listes 
    filtered_features = [] # Cette liste qui est pour l'instat vide sera rempli avec #les valeurs : 'type' et 'crs', ce qui permettra la visualisation d'un geojson dans une carte leaflet 
    for feature in poi_geojson_filtered['features']:
        # category = feature['properties']['reclass']
        # category_color = category_colors.get(category, 'gray')  # Si la categoría no tiene un color definido, usa gris
        feature['properties']['tooltip'] = f"<b>Activité :</b> {feature['properties']['desc']}<br><b> Type de point d’intérêt :</b> {feature['properties']['reclass']}<br><b>Commune :</b> {feature['properties']['libcom']}"
        filtered_features.append(feature)

    geojson_permanents = {
        'type': 'FeatureCollection',
        'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
        'features': filtered_features
    }    
    return geojson_permanents







# #######              GEOJSON des Départements          #######

@app.callback(
    Output('output_geojson_dpt', 'data'),
    [Input('dpt_dropdown', 'value')])
def get_filtered_geojson(selected_departement):   

    dpt_filtered = gdf_dpt[(gdf_dpt['libgeo'] == selected_departement)] 
    dpt_filtered.crs = {'init': 'epsg:4326'} 
    dpt_geojson_string = dpt_filtered.to_crs(epsg=4326).to_json()
    dpt_geojson_filtered = json.loads(dpt_geojson_string)  # Convertir la chaine JSON en tant qu'objet JSON    
    
    #Création de deux listes 
    filtered_features = [] # Cette liste qui est pour l'instat vide sera rempli avec #les valeurs : 'type' et 'crs', ce qui permettra la visualisation d'un geojson dans une carte leaflet 
    for feature in dpt_geojson_filtered['features']:
        filtered_features.append(feature)

    geojson_dpt = {
        'type': 'FeatureCollection',
        'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
        'features': filtered_features
    }    
    return geojson_dpt





###############             CARTE           ###########################

# Create javascript function th at draws a marker with a custom icon, in this case a flag hosted by flagcdn.
icon_nuites = assign("""function(feature, latlng){
const flag = L.icon({iconUrl: 'assets/logos/hotel.svg', iconSize: [25, 25]});
return L.marker(latlng, {icon: flag});
}""")



#       Définition de color_prop dehors le callback
color_prop = 'reclass'  
# Asigna colores específicos a cada categoría
category_colors = {
        'Patrimoine naturel': 'red',
        'Sport': 'orange',
        'Expo et vente': 'yellow',
        'Social et culturel': 'green',
        'Patrimoine historique': 'blue',
        'Divertissement': 'indigo',
        'Non renseigné': 'violet'
    }

point_to_layer = assign("""function(feature, latlng, context){
    const { categoryColors, circleOptions, reclassProp } = context.hideout;
    const category = feature.properties[reclassProp];
    circleOptions.fillColor = categoryColors[category] || 'gray';  // asignar color según la categoría o gris si no hay coincidencia
    return L.circleMarker(latlng, circleOptions);  // renderizar un simple marcador circular
}""")




cluster_to_layer = assign("""function(feature, latlng, index, context){
    const { categoryColors, circleOptions, reclassProp } = context.hideout;
    
    // Obtener la lista de puntos en el cluster.
    const leaves = index.getLeaves(feature.properties.cluster_id);
    
    // Contar la frecuencia de cada categoría en el cluster.
    const categoryCounts = {};
    leaves.forEach(leaf => {
        const category = leaf.properties[reclassProp];
        categoryCounts[category] = (categoryCounts[category] || 0) + 1;
    });
    
    // Encontrar la categoría con la frecuencia máxima.
    const dominantCategory = Object.keys(categoryCounts).reduce((a, b) => categoryCounts[a] > categoryCounts[b] ? a : b);

    // Obtener el color correspondiente a la categoría dominante.
    const clusterColor = categoryColors[dominantCategory] || 'gray';
    
    // Renderizar un círculo con el número de puntos en el centro.
    const scatterIcon = L.DivIcon.extend({
        createIcon: function(oldIcon) {
            let icon = L.DivIcon.prototype.createIcon.call(this, oldIcon);
            icon.style.backgroundColor = this.options.color;
            return icon;
        }
    });

    const icon = new scatterIcon({
        html: '<div style="background-color:white;"><span>' + feature.properties.point_count_abbreviated + '</span></div>',
        className: "marker-cluster",
        iconSize: L.point(40, 40),
        color: clusterColor
    });
    
    return L.marker(latlng, { icon: icon });
}""") 



@app.callback(
    Output('map_div', 'children'),
    [
        Input('output_geojson_nuites', 'data'),
        Input('output_geojson_evenements', 'data'),
        Input('output_geojson_dpt', 'data'),
        Input('output_geojson_poi_permanent', 'data')
    ]
)
def update_map(geojson_nuites, geojson_evenement,geojson_dpt,geojson_permanent):  
   
    dpt =  dl.GeoJSON(
                        data=geojson_dpt,  
                        # filter= dpt_filter,
                        zoomToBoundsOnClick=True,
                        zoomToBounds=True, 
                        id="geojson_dpt"
                )
    
    nuitees = dl.GeoJSON(
                data=geojson_nuites,  
                cluster=True, 
                superClusterOptions={"radius": 100}, 
                zoomToBoundsOnClick=True,
                pointToLayer=icon_nuites,
    )     

    evenements =  dl.GeoJSON(
                        data=geojson_evenement,                                
                        cluster=True, 
                        zoomToBoundsOnClick=True,
                        superClusterOptions={"radius": 100},
                        id="geojson_evenements",
                        pointToLayer=point_to_layer,
                        clusterToLayer=cluster_to_layer,  # how to draw clusters                        
                        hideout=dict(
                            reclassProp='reclass',
                            categoryColors=category_colors,
                            circleOptions=dict(fillOpacity=1, stroke=False, radius=5),)
                )     
        
    poi_permanent = dl.GeoJSON(
                        data=geojson_permanent,                                
                        cluster=True, 
                        zoomToBoundsOnClick=True,
                        superClusterOptions={"radius": 100},
                        id="geojson_permanents",
                        pointToLayer=point_to_layer,
                        clusterToLayer=cluster_to_layer,  # how to draw clusters                        
                        hideout=dict(
                            reclassProp='reclass',
                            categoryColors=category_colors,
                            circleOptions=dict(fillOpacity=1, stroke=False, radius=5),)
        )
    

    return  dl.Map(
            [
                dl.TileLayer(
                            url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png',
                            maxZoom=20,
                            attribution= '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
                ),
                dl.LayersControl(
                                [
                                    dl.Overlay(dl.LayerGroup(nuitees), name="Nuitées", checked=True),
                                    dl.Overlay(dl.LayerGroup(evenements), name="Évènements", checked=False),
                                    dl.Overlay(dl.LayerGroup(poi_permanent), name="Points d'intérêts", checked=True),
                                    dl.Overlay(dl.LayerGroup(dpt), name="Départements", checked=True),
                                ], id='layers-control'
                ),
                legende                              
            ],
            center=(48,6), zoom=8, style={'height': '50vh', 'width': '120vh'}
        )










################                CHIFFRES CLÉS           ################################



                        ######      TYPE D'OFFRE        #######

@app.callback(
    [Output('titre_offre', 'children'),Output('nombre_offre', 'children')],
    [Input('dpt_dropdown', 'value'),Input('offre_dropdown', 'value'),Input('occupation_dropdown', 'value')])
def update_titre(departement,type_offre,type_occupation):

    offres_filtered = gdf_nuites[(gdf_nuites['libdept']== departement) & (gdf_nuites['offre']==type_offre) & (gdf_nuites['occup']==type_occupation)] 
    nb_offre = offres_filtered['offre'].value_counts().sum()
    nb_offre_text = html.Span(f"{nb_offre}", style= {'color': 'white', 'fontSize':'60px', 'fontWeight': 'bold'})

    if type_offre == 'Offre insolite' : 
        titre = html.Span("Offres insolites",style={'color': 'white', 'fontSize':'18px'}) 
    elif type_offre == 'Offre oenologique' : 
        titre = html.Span("Offres oenologiques",style={'color': 'white', 'fontSize':'18px'})
    else : 
        titre = html.Span("Autre type d'offres",style={'color': 'white', 'fontSize':'18px'})

    return [titre, nb_offre_text]







                    ######      NOMBRE DES EVENEMENTS      #######

@app.callback(
    Output('nombre_evenements', 'children'),
    [Input('dpt_dropdown', 'value'),Input('calendrier', 'start_date'),Input('calendrier', 'end_date')])
def update_titre(departement,date_initiale,date_finale):

    if date_initiale is not None and date_finale is not None:

        poi_filtered = gdf_evenements[(gdf_evenements['libdept']== departement)&(gdf_evenements['date_initial']>= date_initiale)&(gdf_evenements['date_final']<= date_finale)] 
        nb_evenements = poi_filtered['gid'].value_counts().sum()
        if nb_evenements == 0 : 
            nb_evenements_text = html.Span("Il n'existe pas d'évènements entre les dates choisies", style= {'color': 'white', 'fontSize':'15px','textAlign':'center'})            
        
        else : 
            nb_evenements_text = html.Span(f"{nb_evenements}", style= {'color': 'white', 'fontSize':'60px', 'fontWeight': 'bold'})

    else : 
        nb_evenements_text = html.Span("Choisir la date finale dans le calendrier situé à gauche", style={'color': 'white', 'fontSize':'15px', 'textAlign':'center'})

        
    return nb_evenements_text




                        ######      NOMBRE DES POINTS D'interets (PERMANENT)       #######

@app.callback(
    Output('nombre_poi', 'children'),
    [Input('dpt_dropdown', 'value')])
def update_titre(departement):

    poi_filtered = gdf_permanents[(gdf_permanents['libdept']== departement)] 
    nb_poi_permanent = poi_filtered['gid'].value_counts().sum()
    nb_poi_permanent_text = html.Span(f"{nb_poi_permanent}", style= {'color': 'white', 'fontSize':'60px', 'fontWeight': 'bold'})

    return nb_poi_permanent_text





if __name__ == '__main__':
    app.run(debug=True,
            dev_tools_hot_reload=False
            )
