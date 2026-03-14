import fastf1
import pandas as pd
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def getSeasonData(year, gp_list, drivers=['COL', 'GAS']):
    all_laps = []
    
    for gp in gp_list:
        try:
            logger.info(f"--- Iniciando descarga: {gp} {year} ---")
            session = fastf1.get_session(year, gp, 'R')
            session.load(telemetry=False, weather=True)
            
            # .copy() soluciona los SettingWithCopyWarning
            laps = session.laps.pick_drivers(drivers).copy()
            
            if laps.empty:
                logger.warning(f"No hay vueltas para los pilotos en {gp}")
                continue

            # Inyectamos metadatos de forma segura con .loc
            laps.loc[:, 'GP'] = gp
            laps.loc[:, 'Year'] = year
            
            # CORRECCIÓN DEL ERROR 'mean': 
            # Accedemos a los valores numéricos de la temperatura antes de promediar
            try:
                laps.loc[:, 'TrackTemp'] = session.weather_data['TrackTemp'].astype(float).mean()
                laps.loc[:, 'AirTemp'] = session.weather_data['AirTemp'].astype(float).mean()
            except:
                laps.loc[:, 'TrackTemp'] = 0
                laps.loc[:, 'AirTemp'] = 0

            laps.loc[:, 'TyreAge'] = laps['TyreLife']
            
            all_laps.append(laps)
            logger.info(f"Éxito: {len(laps)} vueltas recuperadas de {gp}")
            
        except Exception as e:
            logger.error(f"Error procesando {gp}: {str(e)}")
            continue
            
    if not all_laps:
        return pd.DataFrame()
        
    full_df = pd.concat(all_laps, ignore_index=True)
    return full_df