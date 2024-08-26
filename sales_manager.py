import pandas as pd
import os
import logging


class SalesManager:
    def __init__(self, state: str):
        self.state = state
        project_directory = os.path.dirname(os.path.abspath(__file__))
        self.csv_file_path = os.path.join(project_directory, 'data', 'sales_per_mcc.csv')
        self.df = None
    
        # Verificar se o arquivo existe
        if not os.path.isfile(self.csv_file_path):
            logging.warning({"message" : f"File not found: {self.csv_file_path}"})
            return None
        else:
            self.df = pd.read_csv(self.csv_file_path)
    
    def top3_bests_mcc_by_state(self):
        df_state = self.df[self.df['state'] == self.state]
        
         # Verificar se há dados disponíveis para o estado
        if df_state.empty:
            return f'Nenhum dado disponível para o estado {self.state}.'
        
        grouped = df_state.groupby('irs_description').agg(
            total_value=pd.NamedAgg(column='value', aggfunc='sum'),
            transaction_count=pd.NamedAgg(column='value', aggfunc='count')
        ).reset_index()
        
        # Normalizar as métricas para facilitar a combinação entre 0 e 1 
        grouped['total_value_normalized'] = (grouped['total_value'] - grouped['total_value'].min()) / (grouped['total_value'].max() - grouped['total_value'].min())
        grouped['transaction_count_normalized'] = (grouped['transaction_count'] - grouped['transaction_count'].min()) / (grouped['transaction_count'].max() - grouped['transaction_count'].min())
        
        # Métrica combinada com pesos de importancia ajustaveis %
        grouped['combined_score'] = 0.5 * grouped['total_value_normalized'] + 0.7* grouped['transaction_count_normalized']
        grouped = grouped.sort_values(by='combined_score', ascending=False)

        # Obter os top 3 MCCs
        if len(grouped) < 3:
            return grouped
        
        # Obter os top 3 MCCs
        top_3_mccs = grouped.head(3)

        return top_3_mccs