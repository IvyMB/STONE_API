import pandas as pd
import os
import logging


class SoldItemsManager:
    def __init__(self):
        project_directory = os.path.dirname(os.path.abspath(__file__))
        self.csv_file_path = os.path.join(project_directory, 'data', 'mocked_sold_items.csv')
        self.df = None
    
        # Verificar se o arquivo existe
        if not os.path.isfile(self.csv_file_path):
            logging.warning({"message" : f"File not found: {self.csv_file_path}"})
            return None
        else:
            self.df = pd.read_csv(self.csv_file_path)
    
    def top3_best_items_to_sale(self, document_id: str):
        df_filtered = self.df[self.df['document_id'] == int(document_id)]
        
        if df_filtered.empty:
            return {"message": "No data found for the provided document_id"}

        df_filtered['total_revenue_sold'] = df_filtered['qtd'] * df_filtered['price']
        df_filtered['total_quantity_sold'] = df_filtered['qtd']
        
        # Ordenar pelos critérios: receita total e quantidade
        df_sorted_by_revenue = df_filtered.sort_values(by='total_revenue_sold', ascending=False)
        df_sorted_by_quantity = df_filtered.sort_values(by='total_quantity_sold', ascending=False)

        top_3_revenue_items = df_sorted_by_revenue.head(3)
        top_3_quantity_items = df_sorted_by_quantity.head(3)

        # Unir os dois conjuntos e remover duplicatas, priorizando receita total
        combined_items = pd.concat([top_3_revenue_items, top_3_quantity_items])
        combined_items = combined_items.drop_duplicates(subset='item', keep='first').reset_index(drop=True)

        # Se ainda houver menos de 3 itens, preencher com mais itens únicos da receita total
        if len(combined_items) < 3:
            additional_items = df_sorted_by_revenue[~df_sorted_by_revenue['item'].isin(combined_items['item'])]
            combined_items = pd.concat([combined_items, additional_items]).drop_duplicates(subset='item').head(3).reset_index(drop=True)

        top_items = combined_items.sort_values(by='total_revenue_sold', ascending=False).head(3)
        result = top_items[['item', 'total_quantity_sold', 'total_revenue_sold']].to_dict(orient='records')
        
        return result
