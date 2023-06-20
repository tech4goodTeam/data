import pandas as pd

def rename_cols(df):
    """
    Aquesta funció canvia de nom les columnes del df. Converteix les majúscules en minúscules i posa un guió baix entre paraules en cas de no haver-n'hi.
    """
    cols = []
    for i in range(len(df.columns)):
        cols.append(df.columns[i].lower().replace(' ', '_'))
    df.columns = cols
    return df



def select_cols(df):
    """
    Aquesta funció sel·lecciona les columnes específiques pel df final.
    """
    columns = ['id_bcn_2019', 
                'codi_sector_activitat', 
                'nom_sector_activitat', 
               
                'codi_grup_activitat', 
                'nom_grup_activitat',  
               
                'codi_activitat_2019',
                'nom_activitat',
                'nom_local',
               
                'latitud',
                'longitud',
               
                'codi_barri',
                'nom_barri',
               
                'codi_districte',
                'nom_districte',
              
                'v_2011',
                'v_2012',
               'v_2009',
                'v_2008',
              
               'll_2011',
                'll_2012',
               'll_2009',
                'll_2008']
                

    df = df[columns]

    return df
